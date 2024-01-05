# maitnenace test business logic

def test_supportbot(message:str):
    """_summary_

    Parameters
    ----------
    message : str
        test parameter for message
    Returns
    -------
    str
        'bring the harvester in for maintenance' based on promted text
    """
    supportbot_status = 'bring the harvester in for maintenance' if 'help' in message else ''
    
    return supportbot_status