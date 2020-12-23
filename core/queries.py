

def query_capsules():
    """
    Build capsules query.
    """
    query = f'''
    {{
        capsules {{
            id
            landings
            missions {{
                flight
                name
            }}
            reuse_count
            status
            type
        }}
    }}
    '''

    return query


def query_capsule(id):
    """
    build capsule query by id.
    """
    query = f'''
    {{
        capsule (id: "{id}") {{
            id
            landings
            original_launch
            reuse_count
            status
            type
            missions {{
                flight
                name
            }}
            dragon{{
                active
                crew_capacity
                description
                diameter {{
                    feet
                    meters
                }}
                dry_mass_kg
                dry_mass_lb
                first_flight
                heat_shield {{
                    dev_partner
                    material
                    size_meters
                    temp_degrees
                }}
                height_w_trunk {{
                    feet
                    meters
                }}
                launch_payload_mass {{
                    kg
                    lb
                }}
                name
                orbit_duration_yr
                pressurized_capsule{{
                    payload_volume{{
                    cubic_feet
                    cubic_meters
                    }}
                }}
                return_payload_mass {{
                    kg
                    lb
                }}
                return_payload_vol {{
                    cubic_feet
                    cubic_meters
                }}
                sidewall_angle_deg
                thrusters {{
                    amount
                    fuel_1
                    fuel_2
                    pods
                    type
                }}
                trunk{{
                    cargo{{
                        solar_array
                        unpressurized_cargo
                    }}
                    trunk_volume{{
                        cubic_feet
                        cubic_meters
                    }}
                }}
            }}
        }}
    }}
    '''

    return query


def query_company():
    """
    Builds company query.
    """
    query = f'''
    {{
        company {{
            ceo
            coo
            cto_propulsion
            cto
            employees
            founded
            founder
            launch_sites
            name
            summary
            test_sites
            valuation
            vehicles
        }}
    }}
    '''

    return query
