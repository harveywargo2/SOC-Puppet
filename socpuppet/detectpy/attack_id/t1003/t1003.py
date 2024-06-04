import os


def t1003_path():
    """
    :return: Absolute Module Path
    """
    output = os.path.dirname(os.path.abspath(__file__))
    return output


def t1003_mde_path():
    """
    :return: Absolute Path MDE Logic Lib
    """
    output = os.path.join(t1003_path(), 'mde')
    return output

