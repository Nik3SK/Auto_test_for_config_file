import configparser
import os
from babel.core import Locale

path_config_file = './config_file.ini'
config = configparser.ConfigParser()


def test_existence_config_file_and_sections_and_options_uniqueness():
    flag = config.read(path_config_file)
    assert len(flag) != 0


def test_General_section_existence():
    assert config.has_section('General') is True

# Для секции General


def test_General_section_ScanMemoryLimit_option_existence():
    assert config.has_option('General', 'ScanMemoryLimit') is True


def test_General_section_ScanMemoryLimit_option_value_limit():
    ScanMemoryLimit_value = config['General']['ScanMemoryLimit']
    assert ScanMemoryLimit_value.isdigit() is True and \
        int(ScanMemoryLimit_value) in range(1024, 8193)


def test_General_section_PackageType_option_existence():
    assert config.has_option('General', 'PackageType') is True


def test_General_section_PackageType_option_value_limit():
    PackageType_value = config['General']['PackageType'].lower()
    assert PackageType_value == 'rpm' or \
        PackageType_value == 'deb'


def test_General_section_ExecArgMax_option_existence():
    assert config.has_option('General', 'ExecArgMax') is True


def test_General_section_ExecArgMax_option_value_limit():
    ExecArgMax_value = config['General']['ExecArgMax']
    assert ExecArgMax_value.isdigit() is True and \
        int(ExecArgMax_value) in range(10, 101)
    

def test_General_section_AdditionalDNSLookup_option_existence():
    assert config.has_option('General', 'AdditionalDNSLookup') is True


def test_General_section_AdditionalDNSLookup_option_value_limit():
    AdditionalDNSLookup_value = config['General']['AdditionalDNSLookup'].lower()
    assert AdditionalDNSLookup_value == 'yes' or AdditionalDNSLookup_value == 'no' or\
        AdditionalDNSLookup_value == 'true' or AdditionalDNSLookup_value == 'false'


def test_General_section_CoreDumps_option_existence():
    assert config.has_option('General', 'CoreDumps') is True


def test_General_section_CoreDumps_option_value_limit():
    CoreDumps_value = config['General']['CoreDumps'].lower()
    assert CoreDumps_value == 'yes' or CoreDumps_value == 'no' or\
        CoreDumps_value == 'true' or CoreDumps_value == 'false'


def test_General_section_RevealSensitiveInfoInTraces_option_existence():
    assert config.has_option('General', 'RevealSensitiveInfoInTraces') is True


def test_General_section_RevealSensitiveInfoInTraces_option_value_limit():
    RevealSensitiveInfoInTraces_value = config['General']['RevealSensitiveInfoInTraces'].lower()
    assert RevealSensitiveInfoInTraces_value == 'yes' or RevealSensitiveInfoInTraces_value == 'no' or\
        RevealSensitiveInfoInTraces_value == 'true' or RevealSensitiveInfoInTraces_value == 'false'


def test_General_section_ExecEnvMax_option_existence():
    assert config.has_option('General', 'ExecEnvMax') is True


def test_General_section_ExecEnvMax_option_value_limit():
    ExecEnvMax_value = config['General']['ExecEnvMax']
    assert ExecEnvMax_value.isdigit() is True and \
        int(ExecEnvMax_value) in range(10, 101)


def test_General_section_MaxInotifyWatches_option_existence():
    assert config.has_option('General', 'MaxInotifyWatches') is True


def test_General_section_MaxInotifyWatches_option_value_limit():
    MaxInotifyWatches_value = config['General']['MaxInotifyWatches']
    assert MaxInotifyWatches_value.isdigit() is True and \
        int(MaxInotifyWatches_value) in range(100, 1000001)


def test_General_section_CoreDumpsPath_option_existence():
    assert config.has_option('General', 'CoreDumpsPath') is True


def test_General_section_CoreDumpsPath_option_value_limit():
    CoreDumpsPath_value = config['General']['CoreDumpsPath']
    assert os.path.exists(CoreDumpsPath_value) is True


def test_General_section_UseFanotify_option_existence():
    assert config.has_option('General', 'UseFanotify') is True


def test_General_section_UseFanotify_option_value_limit():
    UseFanotify_value = config['General']['UseFanotify'].lower()
    assert UseFanotify_value == 'yes' or UseFanotify_value == 'no' or\
        UseFanotify_value == 'true' or UseFanotify_value == 'false'


def test_General_section_KsvlaMode_option_existence():
    assert config.has_option('General', 'KsvlaMode') is True


def test_General_section_KsvlaMode_option_value_limit():
    KsvlaMode_value = config['General']['KsvlaMode'].lower()
    assert KsvlaMode_value == 'yes' or KsvlaMode_value == 'no' or\
        KsvlaMode_value == 'true' or KsvlaMode_value == 'false'


def test_General_section_MachineId_option_existence():
    assert config.has_option('General', 'MachineId') is True


def test_General_section_MachineIdKsvlaMode_option_value_limit():
    MachineId_value = config['General']['MachineId'].lower()
    assert len(MachineId_value) == 36


def test_General_section_StartupTraces_option_existence():
    assert config.has_option('General', 'StartupTraces') is True


def test_General_section_StartupTraces_option_value_limit():
    StartupTraces_value = config['General']['StartupTraces'].lower()
    assert StartupTraces_value == 'yes' or StartupTraces_value == 'no' or\
        StartupTraces_value == 'true' or StartupTraces_value == 'false'


def test_General_section_MaxInotifyInstances_option_existence():
    assert config.has_option('General', 'MaxInotifyInstances') is True


def test_General_section_MaxInotifyInstances_option_value_limit():
    MaxInotifyInstances_value = config['General']['MaxInotifyInstances']
    assert MaxInotifyInstances_value.isdigit() is True and \
        int(MaxInotifyInstances_value) in range(1024, 8193)


def test_General_section_Locale_option_existence():
    assert config.has_option('General', 'Locale') is True


def test_General_section_Locale_option_value_limit():
    MaxInotifyInstances_value = config['General']['Locale']
    assert Locale.parse(MaxInotifyInstances_value)


def test_Watchdog_section_existence():
    assert config.has_section('Watchdog') is True


# Для секции Watchdog


def test_Watchdog_section_ConnectTimeout_option_existence():
    assert config.has_option('Watchdog', 'ConnectTimeout') is True


def test_Watchdog_section_ConnectTimeout_option_value_limit():
    ConnectTimeout_value = config['Watchdog']['ConnectTimeout']
    assert ConnectTimeout_value[:len(ConnectTimeout_value)-1].isdigit() is True and \
        int(ConnectTimeout_value[:len(ConnectTimeout_value)-1]) in range(1, 121) and \
        ConnectTimeout_value[len(ConnectTimeout_value)-1] == 'm'


def test_Watchdog_section_MaxVirtualMemory_option_existence():
    assert config.has_option('Watchdog', 'MaxVirtualMemory') is True


def test_Watchdog_section_MaxVirtualMemory_option_value_limit():
    MaxVirtualMemory_value = config['Watchdog']['MaxVirtualMemory']
    assert MaxVirtualMemory_value == 'off' or MaxVirtualMemory_value == 'auto' or \
        (MaxVirtualMemory_value.replace('.', '').isdigit() and float(MaxVirtualMemory_value) > 0 and \
         float(MaxVirtualMemory_value) <= 100)


def test_Watchdog_section_MaxMemory_option_existence():
    assert config.has_option('Watchdog', 'MaxMemory') is True


def test_Watchdog_section_MaxMemory_option_value_limit():
    MaxMemory_value = config['Watchdog']['MaxMemory']
    assert MaxMemory_value == 'off' or MaxMemory_value == 'auto' or \
        (MaxMemory_value.replace('.', '').isdigit() and float(MaxMemory_value) > 0 and \
         float(MaxMemory_value) <= 100)


def test_Watchdog_section_PingInterval_option_existence():
    assert config.has_option('Watchdog', 'PingInterval') is True


def test_Watchdog_section_PingInterval_option_value_limit():
    PingInterval_value = config['Watchdog']['PingInterval']
    assert PingInterval_value.isdigit() is True and \
        int(PingInterval_value) in range(100, 10001)
