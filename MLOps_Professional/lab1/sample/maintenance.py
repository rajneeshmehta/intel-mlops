# maitnenace test business logic

def test_maintenance(temperature:int, hydrolic_pressure_psi:int):
    """_summary_

    Parameters
    ----------
    temperature : int
        test parameter for temperature sensor readings
    hydrolic_pressure_psi : int
        test parameter for hydrolic pressure sensor readings

    Returns
    -------
    str
        'Approved' or 'Denied' based on temperature readings
    """
    maintenance_status = 'Needs Maintenance' if (temperature > 50 or hydrolic_pressure_psi > 2000) else 'No Maintenance Required'
    
    return maintenance_status