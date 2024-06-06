import yaml
import os
import socpuppet as soc
from socpuppet.detectpy.attack_id.t1003.t1003 import t1003_mde_path as mde_path


def builtin_pid_0001_edr_steal_creds_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0001_edr_steal_creds_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0002_edr_process_memory_dump_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0002_edr_process_memory_dump_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0003_edr_cred_memory_read_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE EDR

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0003_edr_cred_memory_read_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0004_av_hacktool_atpminidump_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0004_av_hacktool_atpminidump_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0005_av_hacktool_atpminidump_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0005_av_hacktool_atpminidump_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0006_av_hacktool_atpminidump_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0006_av_hacktool_atpminidump_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0007_av_rundlllolbin_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0007_av_rundlllolbin_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0008_av_rundlllolbin_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0008_av_rundlllolbin_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0009_av_rundlllolbin_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0009_av_rundlllolbin_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0010_av_hacktool_gsecdump_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0010_av_hacktool_gsecdump_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0011_av_hacktool_gsecdump_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0011_av_hacktool_gsecdump_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0012_av_hacktool_gsecdump_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0012_av_hacktool_gsecdump_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0013_edr_suspicious_access_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0013_edr_suspicious_access_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0014_av_hacktool_dumplsass_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0014_av_hacktool_dumplsass_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0015_av_hacktool_dumplsass_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0015_av_hacktool_dumplsass_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0016_av_hacktool_dumplsass_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0016_av_hacktool_dumplsass_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0017_av_pua_presenoker_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0017_av_pua_presenoker_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0018_av_pua_presenoker_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0018_av_pua_presenoker_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0019_av_pua_presenoker_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0019_av_pua_presenoker_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0020_av_hacktool_mimikatz_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0020_av_hacktool_mimikatz_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0021_av_hacktool_mimikatz_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0021_av_hacktool_mimikatz_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0022_av_hacktool_mimikatz_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0022_av_hacktool_mimikatz_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0023_av_registryexfil_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0023_av_registryexfil_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0024_av_registryexfil_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0024_av_registryexfil_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0025_av_registryexfil_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0025_av_registryexfil_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0026_edr_registry_extract_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0026_edr_registry_extract_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0027_edr_sensitive_info_lookup_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0026_edr_registry_extract_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0028_edr_sam_info_theft_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0028_edr_sam_info_theft_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0029_edr_registry_export_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0029_edr_registry_export_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0030_av_hacktool_pypykatz_alert(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0030_av_hacktool_pypykatz_alert.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0031_av_hacktool_pypykatz_dynamic(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0031_av_hacktool_pypykatz_dynamic.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def builtin_pid_0032_av_hacktool_pypykatz_event(*, logic='mde', lookback='1d'):
    """
    builtin MDE AV

    param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'mde':
        with open(os.path.join(mde_path(),
                               'builtin_pid_0032_av_hacktool_pypykatz_event.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.mde_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query