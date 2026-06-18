import os
import io
import re
from dataclasses import dataclass, field
from typing import List, Optional, Iterable
from datetime import datetime

filtered_PE_entries_tmp_file = "filtered_tmp_file.log"

@dataclass
class SubTest:
    description: str
    start_time: datetime
    end_time: Optional[datetime] = None


@dataclass
class DeviceTest:
    start_time: datetime
    end_time: Optional[datetime] = None
    subtests: List[SubTest] = field(default_factory=list)


@dataclass
class Device:
    device_id: str
    insertion_time: datetime
    removal_time: Optional[datetime] = None
    tests: List[DeviceTest] = field(default_factory=list)
    # Holds error messages specific to this device tree structure
    validation_errors: List[str] = field(default_factory=list)


def parse_PE_entries() -> List[Device]:

    devices: List[Device] = []
    current_device: Optional[Device] = None
    current_test: Optional[DeviceTest] = None
    
    print("Construct nested device tree while validating structure integrity.")

    log_pattern = re.compile(
        r'^#PE\[(?P<timestamp>[^\]]+)\] : (?P<action>BEGIN|END) (?P<type>\S+)(?P<arg> .*)?$'
    )

    # Safely open and read the file internally
    with open(filtered_PE_entries_tmp_file, 'r', encoding='utf-8') as file_stream:
        for line_num, line in enumerate(file_stream, 1):
            match = log_pattern.match(line.strip())
            if not match:
                continue

            data = match.groupdict()
            try:
                timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                print(f"[Line {line_num}] Global Error: Invalid timestamp format.")
                continue

            action = data['action']
            element_type = data['type']
            arg = data['arg'].strip().strip('"') if data['arg'] else ""

            if action == "BEGIN":
                if element_type == "INSERTION":
                    if current_device and not current_device.removal_time:
                        current_device.validation_errors.append(
                            f"Missing REMOVAL block before a new device insertion began."
                        )
                    current_device = Device(device_id=arg, insertion_time=timestamp)
                    devices.append(current_device)
                    current_test = None

                elif element_type == "DEVICE_TEST":
                    if not current_device:
                        print(f"[Line {line_num}] Orphan Error: DEVICE_TEST started without an active Device.")
                        continue
                    if current_test and not current_test.end_time:
                        current_device.validation_errors.append(
                            f"Line {line_num}: Nested DEVICE_TEST started before previous test closed."
                        )
                    current_test = DeviceTest(start_time=timestamp)
                    current_device.tests.append(current_test)

                elif element_type == "DEVICE_TEST.SUBTEST":
                    if not current_device:
                        continue
                    if not current_test:
                        current_device.validation_errors.append(
                            f"Line {line_num}: SUBTEST '{arg}' started outside of an active DEVICE_TEST block."
                        )
                        continue
                    if current_test.subtests and current_test.subtests[-1].end_time is None:
                        current_device.validation_errors.append(
                            f"Line {line_num}: SUBTEST '{arg}' started before previous SUBTEST closed."
                        )
                    subtest = SubTest(description=arg, start_time=timestamp)
                    current_test.subtests.append(subtest)

            elif action == "END":
                if element_type == "INSERTION":
                    pass 

                elif element_type == "DEVICE_TEST":
                    if current_device and current_test:
                        current_test.end_time = timestamp
                        if not current_test.subtests:
                            current_device.validation_errors.append(
                                f"Line {line_num}: DEVICE_TEST completed but contained zero subtests."
                            )
                    elif current_device:
                        current_device.validation_errors.append(
                            f"Line {line_num}: END DEVICE_TEST found with no matching active test block."
                        )

                elif element_type == "DEVICE_TEST.SUBTEST":
                    if current_device and current_test and current_test.subtests:
                        last_subtest = current_test.subtests[-1]
                        if last_subtest.end_time is None:
                            last_subtest.end_time = timestamp
                        else:
                            current_device.validation_errors.append(
                                f"Line {line_num}: Duplicate END SUBTEST block detected."
                            )
                    elif current_device:
                        current_device.validation_errors.append(
                            f"Line {line_num}: END SUBTEST found but no subtests were registered."
                        )

            elif element_type == "REMOVAL":
                if current_device:
                    current_device.removal_time = timestamp
                    if not current_device.tests:
                        current_device.validation_errors.append(
                            "Device session completed without running any DEVICE_TEST profiles."
                        )
                    current_device = None
                    current_test = None

    if current_device and not current_device.removal_time:
        current_device.validation_errors.append("Log file ended unexpectedly before REMOVAL could be executed.")

    return devices


def filter_PE_entries(input_file: str):

    print(f"Filter '#PE' (Profiling Event) entries from \'{input_file}\'.")
    
    prefix = "#PE"

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return
    
    with open(input_file, "r", encoding="utf-8") as infile, \
        open(filtered_PE_entries_tmp_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if line.startswith(prefix):
                outfile.write(line)


def build_PE_entries_tree(PE_entries):
    return "not implemented yet"

def parse_PE_entries_for_completeness(tree): 
    # Status status = check_order_of_PE_entries(tree)
    return "not implemented yet"

def parse_PE_entries_for_times(tree):
    return "not implemented yet"

def analyze_diagnostic_log(diagnostic_log_file) -> bool:
    filter_PE_entries(diagnostic_log_file)
    devices = parse_PE_entries()
    for device in devices:
        print(f"Device: {device.device_id} | Validation Errors: {len(device.validation_errors)}")

    # status = parse_PE_entries_for_completeness(tree)
    # status = parse_PE_entries_for_times(tree)

    diagnostic_log_is_healthy = False

    return diagnostic_log_is_healthy

