

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


def query_histories():
    """
    Build query for histories.
    """
    query = f'''
    {{
        histories {{
            id
            event_date_unix
            event_date_utc
            title
        }}
    }}
    '''

    return query


def query_history(id):
    """
    Build query for single history event.
    """
    query = f'''
    {{
        history(id: "{id}") {{
            details
            event_date_utc
            links {{
                article
                reddit
                wikipedia
            }}
            title
            flight {{
                details
                is_tentative
                launch_date_local
                launch_date_unix
                launch_date_utc
                launch_site {{
                    site_id
                    site_name_long
                    site_name
                }}
                launch_success
                launch_year
                links {{
                    video_link
                }}
                mission_name
                rocket {{
                    rocket_name
                    rocket_type
                }}
            }}
        }}
    }}
    '''

    return query
def query_rockets():

    """
    request all rockets
    """
    query = '''
    {
      rockets {
       id
      }
    }

    '''
    return query
def query_rocket(id):
    """
    request a single rocket
    """
    query = f"""
        {{
            rocket(id: "{id}") {{
                active
                company
                cost_per_launch
                country
                description
                type
                success_rate_pct
                name
                height {{
                  feet
                  meters
                }}
              }}
        }}
    """


    return query




