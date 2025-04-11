import configparser
import os
from babel.core import Locale
import pytest

path_config_file = '/var/opt/kaspersky/config.ini'
config = configparser.ConfigParser()


def test_existence_config_file_and_sections_and_options_uniqueness():
    flag = config.read(path_config_file)
    assert len(flag) != 0


def test_General_section_existence():
    assert config.has_section('General') is True

# Для секции General


@pytest.mark.parametrize("option_name", [
   ('ScanMemoryLimit'),
   ('PackageType'),
   ('ExecArgMax'),
   ('AdditionalDNSLookup'),
   ('CoreDumps'),
   ('RevealSensitiveInfoInTraces'),
   ('ExecEnvMax'),
   ('MaxInotifyWatches'),
   ('CoreDumpsPath'),
   ('UseFanotify'),
   ('KsvlaMode'),
   ('MachineId'),
   ('StartupTraces'),
   ('MaxInotifyInstances'),
   ('Locale'),
])
def test_General_section_option_existence(option_name):
    assert config.has_option('General', option_name) is True


@pytest.mark.parametrize("option_name, range_list", [
   ('ScanMemoryLimit', range(1024, 8193)),
   ('ExecArgMax', range(10, 101)),
   ('ExecEnvMax', range(10, 101)),
   ('MaxInotifyWatches', range(1000, 1000000)),
   ('MaxInotifyInstances', range(1024, 8193))
])
def test_General_section_int_option_value_limit(option_name, range_list):
    option_value = config['General'][option_name]
    assert option_value.isdigit() is True and \
        int(option_value) in range_list


def test_General_section_PackageType_option_value_limit():
    PackageType_value = config['General']['PackageType'].lower()
    assert PackageType_value == 'rpm' or \
        PackageType_value == 'deb'


def test_General_section_AdditionalDNSLookup_option_value_limit():
    AdditionalDNSLookup_value = config['General']['AdditionalDNSLookup'].lower()
    assert AdditionalDNSLookup_value == 'yes' or AdditionalDNSLookup_value == 'no' or\
        AdditionalDNSLookup_value == 'true' or AdditionalDNSLookup_value == 'false'


def test_General_section_CoreDumps_option_value_limit():
    CoreDumps_value = config['General']['CoreDumps'].lower()
    assert CoreDumps_value == 'yes' or CoreDumps_value == 'no' or\
        CoreDumps_value == 'true' or CoreDumps_value == 'false'


def test_General_section_RevealSensitiveInfoInTraces_option_value_limit():
    RevealSensitiveInfoInTraces_value = config['General']['RevealSensitiveInfoInTraces'].lower()
    assert RevealSensitiveInfoInTraces_value == 'yes' or RevealSensitiveInfoInTraces_value == 'no' or\
        RevealSensitiveInfoInTraces_value == 'true' or RevealSensitiveInfoInTraces_value == 'false'


def test_General_section_CoreDumpsPath_option_value_limit():
    CoreDumpsPath_value = config['General']['CoreDumpsPath']
    assert os.path.exists(CoreDumpsPath_value) is True


def test_General_section_UseFanotify_option_value_limit():
    UseFanotify_value = config['General']['UseFanotify'].lower()
    assert UseFanotify_value == 'yes' or UseFanotify_value == 'no' or\
        UseFanotify_value == 'true' or UseFanotify_value == 'false'


def test_General_section_KsvlaMode_option_value_limit():
    KsvlaMode_value = config['General']['KsvlaMode'].lower()
    assert KsvlaMode_value == 'yes' or KsvlaMode_value == 'no' or\
        KsvlaMode_value == 'true' or KsvlaMode_value == 'false'


def test_General_section_MachineIdKsvlaMode_option_value_limit():
    MachineId_value = config['General']['MachineId'].lower()
    assert len(MachineId_value) == 36


def test_General_section_StartupTraces_option_value_limit():
    StartupTraces_value = config['General']['StartupTraces'].lower()
    assert StartupTraces_value == 'yes' or StartupTraces_value == 'no' or\
        StartupTraces_value == 'true' or StartupTraces_value == 'false'


def test_General_section_Locale_option_value_limit():
    MaxInotifyInstances_value = config['General']['Locale']
    assert Locale.parse(MaxInotifyInstances_value)


# Для секции Watchdog

def test_Watchdog_section_existence():
    assert config.has_section('Watchdog') is True


@pytest.mark.parametrize("option_name", [
   ('ConnectTimeout'),
   ('MaxVirtualMemory'),
   ('MaxMemory'),
   ('PingInterval')
])
def test_Watchdog_section_option_existence(option_name):
    assert config.has_option('Watchdog', option_name) is True


def test_Watchdog_section_ConnectTimeout_option_value_limit():
    ConnectTimeout_value = config['Watchdog']['ConnectTimeout']
    assert ConnectTimeout_value[:len(ConnectTimeout_value)-1].isdigit() is True and \
        int(ConnectTimeout_value[:len(ConnectTimeout_value)-1]) in range(1, 121) and \
        ConnectTimeout_value[len(ConnectTimeout_value)-1] == 'm'


def test_Watchdog_section_MaxVirtualMemory_option_value_limit():
    MaxVirtualMemory_value = config['Watchdog']['MaxVirtualMemory']
    assert MaxVirtualMemory_value == 'off' or MaxVirtualMemory_value == 'auto' or \
        (MaxVirtualMemory_value.replace('.', '').isdigit() and float(MaxVirtualMemory_value) > 0 and
         float(MaxVirtualMemory_value) <= 100)


def test_Watchdog_section_MaxMemory_option_value_limit():
    MaxMemory_value = config['Watchdog']['MaxMemory']
    assert MaxMemory_value == 'off' or MaxMemory_value == 'auto' or \
        (MaxMemory_value.replace('.', '').isdigit() and float(MaxMemory_value) > 0 and
         float(MaxMemory_value) <= 100)


def test_Watchdog_section_PingInterval_option_value_limit():
    PingInterval_value = config['Watchdog']['PingInterval']
    assert PingInterval_value.isdigit() is True and \
        int(PingInterval_value) in range(100, 10001)
