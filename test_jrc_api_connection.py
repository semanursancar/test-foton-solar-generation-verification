# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:25:30 2023

@author: SemanurSancar
"""

import unittest
from unittest.mock import patch
from jrc_api_connection import GETSolarAverageDataFromJRC
import json

# New function to load data
def load_test_raw_data_json():
    test_raw_data_json = {
        "inputs": {
            "location": {
                "latitude": 37.0,
                "longitude": 38.0,
                "elevation": 417.0
            },
            "meteo_data": {
                "radiation_db": "PVGIS-SARAH2",
                "meteo_db": "ERA5",
                "year_min": 2005,
                "year_max": 2020,
                "use_horizon": True,
                "horizon_db": "DEM-calculated"
            },
            "mounting_system": {
                "fixed": {
                    "slope": {
                        "value": 35,
                        "optimal": False
                    },
                    "azimuth": {
                        "value": 0,
                        "optimal": False
                    },
                    "type": "free-standing"
                }
            },
            "pv_module": {
                "technology": "c-Si",
                "peak_power": 50.0,
                "system_loss": 0.0
            },
            "economic_data": {
                "system_cost": None,
                "interest": None,
                "lifetime": None
            }
        },
        "outputs": {
            "monthly": {
                "fixed": [
                    {
                        "month": 1,
                        "E_d": 168.65,
                        "E_m": 5228.06,
                        "H(i)_d": 3.51,
                        "H(i)_m": 108.91,
                        "SD_m": 697.84
                    },
                    {
                        "month": 2,
                        "E_d": 201.73,
                        "E_m": 5648.42,
                        "H(i)_d": 4.3,
                        "H(i)_m": 120.3,
                        "SD_m": 1061.84
                    },
                    {
                        "month": 3,
                        "E_d": 241.66,
                        "E_m": 7491.41,
                        "H(i)_d": 5.33,
                        "H(i)_m": 165.17,
                        "SD_m": 687.47
                    },
                    {
                        "month": 4,
                        "E_d": 266.52,
                        "E_m": 7995.56,
                        "H(i)_d": 6.1,
                        "H(i)_m": 182.91,
                        "SD_m": 539.44
                    },
                    {
                        "month": 5,
                        "E_d": 278.53,
                        "E_m": 8634.35,
                        "H(i)_d": 6.61,
                        "H(i)_m": 204.91,
                        "SD_m": 460.23
                    },
                    {
                        "month": 6,
                        "E_d": 293.7,
                        "E_m": 8810.9,
                        "H(i)_d": 7.29,
                        "H(i)_m": 218.74,
                        "SD_m": 175.4
                    },
                    {
                        "month": 7,
                        "E_d": 294.5,
                        "E_m": 9129.6,
                        "H(i)_d": 7.47,
                        "H(i)_m": 231.59,
                        "SD_m": 184.47
                    },
                    {
                        "month": 8,
                        "E_d": 298.16,
                        "E_m": 9242.84,
                        "H(i)_d": 7.35,
                        "H(i)_m": 227.88,
                        "SD_m": 222.23
                    },
                    {
                        "month": 9,
                        "E_d": 295.21,
                        "E_m": 8856.18,
                        "H(i)_d": 7.05,
                        "H(i)_m": 211.4,
                        "SD_m": 286.54
                    },
                    {
                        "month": 10,
                        "E_d": 246.72,
                        "E_m": 7648.21,
                        "H(i)_d": 5.65,
                        "H(i)_m": 175.14,
                        "SD_m": 563.51
                    },
                    {
                        "month": 11,
                        "E_d": 212.22,
                        "E_m": 6366.48,
                        "H(i)_d": 4.56,
                        "H(i)_m": 136.69,
                        "SD_m": 807.11
                    },
                    {
                        "month": 12,
                        "E_d": 173.16,
                        "E_m": 5367.88,
                        "H(i)_d": 3.64,
                        "H(i)_m": 112.7,
                        "SD_m": 1237.17
                    }
                ]
            },
            "totals": {
                "fixed": {
                    "E_d": 247.73,
                    "E_m": 7534.99,
                    "E_y": 90419.86,
                    "H(i)_d": 5.74,
                    "H(i)_m": 174.69,
                    "H(i)_y": 2096.34,
                    "SD_m": 220.27,
                    "SD_y": 2643.22,
                    "l_aoi": -2.59,
                    "l_spec": "-0.52",
                    "l_tg": -10.98,
                    "l_total": -13.74
                }
            }
        },
        "meta": {
            "inputs": {
                "location": {
                    "description": "Selected location",
                    "variables": {
                        "latitude": {
                            "description": "Latitude",
                            "units": "decimal degree"
                        },
                        "longitude": {
                            "description": "Longitude",
                            "units": "decimal degree"
                        },
                        "elevation": {
                            "description": "Elevation",
                            "units": "m"
                        }
                    }
                },
                "meteo_data": {
                    "description": "Sources of meteorological data",
                    "variables": {
                        "radiation_db": {
                            "description": "Solar radiation database"
                        },
                        "meteo_db": {
                            "description": "Database used for meteorological variables other than solar radiation"
                        },
                        "year_min": {
                            "description": "First year of the calculations"
                        },
                        "year_max": {
                            "description": "Last year of the calculations"
                        },
                        "use_horizon": {
                            "description": "Include horizon shadows"
                        },
                        "horizon_db": {
                            "description": "Source of horizon data"
                        }
                    }
                },
                "mounting_system": {
                    "description": "Mounting system",
                    "choices": "fixed, vertical_axis, inclined_axis, two_axis",
                    "fields": {
                        "slope": {
                            "description": "Inclination angle from the horizontal plane",
                            "units": "degree"
                        },
                        "azimuth": {
                            "description": "Orientation (azimuth) angle of the (fixed) PV system (0 = S, 90 = W, -90 = E)",
                            "units": "degree"
                        }
                    }
                },
                "pv_module": {
                    "description": "PV module parameters",
                    "variables": {
                        "technology": {
                            "description": "PV technology"
                        },
                        "peak_power": {
                            "description": "Nominal (peak) power of the PV module",
                            "units": "kW"
                        },
                        "system_loss": {
                            "description": "Sum of system losses",
                            "units": "%"
                        }
                    }
                },
                "economic_data": {
                    "description": "Economic inputs",
                    "variables": {
                        "system_cost": {
                            "description": "Total cost of the PV system",
                            "units": "user-defined currency"
                        },
                        "interest": {
                            "description": "Annual interest",
                            "units": "%/y"
                        },
                        "lifetime": {
                            "description": "Expected lifetime of the PV system",
                            "units": "y"
                        }
                    }
                }
            },
            "outputs": {
                "monthly": {
                    "type": "time series",
                    "timestamp": "monthly averages",
                    "variables": {
                        "E_d": {
                            "description": "Average daily energy production from the given system",
                            "units": "kWh/d"
                        },
                        "E_m": {
                            "description": "Average monthly energy production from the given system",
                            "units": "kWh/mo"
                        },
                        "H(i)_d": {
                            "description": "Average daily sum of global irradiation per square meter received by the modules of the given system",
                            "units": "kWh/m2/d"
                        },
                        "H(i)_m": {
                            "description": "Average monthly sum of global irradiation per square meter received by the modules of the given system",
                            "units": "kWh/m2/mo"
                        },
                        "SD_m": {
                            "description": "Standard deviation of the monthly energy production due to year-to-year variation",
                            "units": "kWh"
                        }
                    }
                },
                "totals": {
                    "type": "time series totals",
                    "variables": {
                        "E_d": {
                            "description": "Average daily energy production from the given system",
                            "units": "kWh/d"
                        },
                        "E_m": {
                            "description": "Average monthly energy production from the given system",
                            "units": "kWh/mo"
                        },
                        "E_y": {
                            "description": "Average annual energy production from the given system",
                            "units": "kWh/y"
                        },
                        "H(i)_d": {
                            "description": "Average daily sum of global irradiation per square meter received by the modules of the given system",
                            "units": "kWh/m2/d"
                        },
                        "H(i)_m": {
                            "description": "Average monthly sum of global irradiation per square meter received by the modules of the given system",
                            "units": "kWh/m2/mo"
                        },
                        "H(i)_y": {
                            "description": "Average annual sum of global irradiation per square meter received by the modules of the given system",
                            "units": "kWh/m2/y"
                        },
                        "SD_m": {
                            "description": "Standard deviation of the monthly energy production due to year-to-year variation",
                            "units": "kWh"
                        },
                        "SD_y": {
                            "description": "Standard deviation of the annual energy production due to year-to-year variation",
                            "units": "kWh"
                        },
                        "l_aoi": {
                            "description": "Angle of incidence loss",
                            "units": "%"
                        },
                        "l_spec": {
                            "description": "Spectral loss",
                            "units": "%"
                        },
                        "l_tg": {
                            "description": "Temperature and irradiance loss",
                            "units": "%"
                        },
                        "l_total": {
                            "description": "Total loss",
                            "units": "%"
                        }
                    }
                }
            }
        }
    }
    return test_raw_data_json

class TestJrcApiConnection(unittest.TestCase):

    @patch('jrc_api_connection.requests.get')
    def test_successful_api_request(self, mock_get):
        # Load test data
        test_raw_data_json = load_test_raw_data_json()

        # Simulated response for a successful API request
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        # Use the loaded test data as the mock response text
        mock_response.text = json.dumps(test_raw_data_json)
        mock_get.return_value = mock_response

        # Test data
        lat = 37
        lon = 38
        peakpower = 50

        # Call the function
        result = GETSolarAverageDataFromJRC(lat, lon, peakpower)

        # Expected result: Use the loaded test data as the expected result
        expected_result = test_raw_data_json

        # Verify the test result
        self.assertEqual(result, expected_result)

    @patch('jrc_api_connection.requests.get')
    def test_unsuccessful_api_request(self, mock_get):
        # Simulated response for an unsuccessful API request
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Test data
        lat = 37
        lon = 38
        peakpower = 50

        # Call the function
        result = GETSolarAverageDataFromJRC(lat, lon, peakpower)

        # Verify that the result is None, indicating an unsuccessful API request
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
