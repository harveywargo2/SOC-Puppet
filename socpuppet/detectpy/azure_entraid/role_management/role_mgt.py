import yaml
import os
import socpuppet as soc


def rolemgt_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def rolemgt_azmon_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(rolemgt_path(), 'logic_azmon')
    return output


def rolemgt_pid_0001_any_global_admin(*, logic='azmon', lookback='1d'):
    """
    Global Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0001_any_global_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0002_any_global_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Global Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0002_any_global_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0003_any_app_admin(*, logic='azmon', lookback='1d'):
    """
    Application Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0003_any_app_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0004_any_app_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Application Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0004_any_app_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0005_any_app_dev(*, logic='azmon', lookback='1d'):
    """
    Application Developer

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0005_any_app_dev.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0006_any_app_dev_not_pim(*, logic='azmon', lookback='1d'):
    """
    Application Developer

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0006_any_app_dev_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0007_any_auth_admin(*, logic='azmon', lookback='1d'):
    """
    Authentication Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0007_any_auth_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0008_any_auth_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Authentication Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0008_any_auth_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0009_any_auth_policy_admin(*, logic='azmon', lookback='1d'):
    """
    Authentication Policy Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0009_any_auth_policy_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0010_any_auth_policy_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Authentication Policy Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0010_any_auth_policy_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0011_any_auth_extension_admin(*, logic='azmon', lookback='1d'):
    """
    Authentication Extensibility Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0011_any_auth_extension_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0012_any_auth_extension_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Authentication Extensibility Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0012_any_auth_extension_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0013_any_ief_keyset_admin(*, logic='azmon', lookback='1d'):
    """
    B2C IEF Keyset Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0013_any_fed_keyset_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0014_any_ief_keyset_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    B2C IEF Keyset Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0014_any_fed_keyset_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0015_any_billing_admin(*, logic='azmon', lookback='1d'):
    """
    Billing Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0015_any_billing_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0016_any_billing_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Billing Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0016_any_billing_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0017_any_cloudapp_security_admin(*, logic='azmon', lookback='1d'):
    """
    Cloud App Security Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0017_any_cloudapp_security_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0018_any_cloudapp_security_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Cloud App Security Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0018_any_cloudapp_security_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0019_any_cloudapp_admin(*, logic='azmon', lookback='1d'):
    """
    Cloud App Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0019_any_cloudapp_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0020_any_cloudapp_admin(*, logic='azmon', lookback='1d'):
    """
    Cloud App Administrator

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0020_any_cloudapp_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0021_any_cloud_device_admin(*, logic='azmon', lookback='1d'):
    """
    Cloud Device Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0021_any_cloud_device_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0022_any_cloud_device_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Cloud Device Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0022_any_cloud_device_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0023_any_cap_admin(*, logic='azmon', lookback='1d'):
    """
    CAP Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0023_any_cap_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0024_any_cap_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    CAP Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0024_any_cap_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0025_any_directory_reader(*, logic='azmon', lookback='1d'):
    """
    Directory Reader

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0025_any_directory_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0026_any_directory_reader_not_pim(*, logic='azmon', lookback='1d'):
    """
    Directory Reader

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0026_any_directory_reader_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0027_any_directory_writer(*, logic='azmon', lookback='1d'):
    """
    Directory Writer

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0027_any_directory_writer.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0028_any_directory_writer_not_pim(*, logic='azmon', lookback='1d'):
    """
    Directory Writer

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0028_any_directory_writer_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0029_any_domain_name_admin(*, logic='azmon', lookback='1d'):
    """
    Domain Name Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0029_any_domain_name_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0030_any_domain_name_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Domain Name Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0030_any_domain_name_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0031_any_exchange_admin(*, logic='azmon', lookback='1d'):
    """
    Exchange Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0031_any_exchange_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0032_any_exchange_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Exchange Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0032_any_exchange_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0033_any_global_reader(*, logic='azmon', lookback='1d'):
    """
    Global Reader

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0033_any_global_reader.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0034_any_global_reader_not_pim(*, logic='azmon', lookback='1d'):
    """
    Global Reader

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0034_any_global_reader_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0035_any_groups_admin(*, logic='azmon', lookback='1d'):
    """
    Groups Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0035_any_groups_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0036_any_groups_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Groups Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0036_any_groups_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0037_any_helpdesk_admin(*, logic='azmon', lookback='1d'):
    """
    Help Desk Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0037_any_helpdesk_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0038_any_helpdesk_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Help Desk Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0038_any_helpdesk_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0039_any_hybrid_id_admin(*, logic='azmon', lookback='1d'):
    """
    Hybrid Identity Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0039_any_hybrid_id_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0040_any_hybrid_id_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Hybrid Identity Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0040_any_hybrid_id_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0041_any_intune_admin(*, logic='azmon', lookback='1d'):
    """
    Intune Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0041_any_intune_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0042_any_intune_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Intune Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0042_any_intune_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0043_any_password_admin(*, logic='azmon', lookback='1d'):
    """
    Password Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0043_any_password_admin.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query


def rolemgt_pid_0044_any_password_admin_not_pim(*, logic='azmon', lookback='1d'):
    """
    Password Admin

    :param logic: Logic Selection
    :param lookback: Lookback Time
    :return: Pandas Dataframe of Results
    """

    if logic == 'azmon':
        with open(os.path.join(rolemgt_azmon_path(),
                               'rolemgt_pid_0044_any_password_admin_not_pim.yaml'), 'r') as file:
            data = yaml.safe_load(file)

        query = soc.detectpy.azmon_query_builder(data, lookback)

    else:
        query = f'pointer={logic} not supported'

    return query