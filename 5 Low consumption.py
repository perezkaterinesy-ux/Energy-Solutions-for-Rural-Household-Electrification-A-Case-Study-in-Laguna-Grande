# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 09:28:24 2025

@author: Portatil Toshiba
"""


from ramp.core.core import User

User_list = []

"""
This input file represents a Low Consumption household in Raqaypampa Autonomous Territory
"""

# Create new user classes
LC = User("high consumption", 5)
User_list.append(LC)


# Create new appliances
LC_LED_1 = LC.Appliance(1, 13, 1, 320, 0.2, 120) 
LC_LED_1.windows([1020, 1440], [0, 0], 0.35)

LC_LED_2 = LC.Appliance(2, 7, 2, 300, 0.3, 120)
LC_LED_2.windows([0, 480], [1080, 1440], 0.35)

LC_Phone_charger = LC.Appliance(1, 5, 3, 240, 0.2, 95)
LC_Phone_charger.windows([421, 660], [1190, 1440], 0.35,[0,420])

LC_radio = LC.Appliance(1, 7, 2, 280, 0.2, 120) 
LC_radio.windows([420, 708], [840, 1020], 0.35)

LC_TV = LC.Appliance(1,60,2,120,0.2,60)
LC_TV.windows([840,1080],[1140,1440],0.35)


#----------------------------------------------------------------
from datetime import datetime
if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        date_start=datetime(2023, 1, 1),  # <-- fecha de inicio deseada
        date_end=datetime(2023, 1, 31),   # <-- fecha final deseada
    )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
        
    # this would be a new method using work of @mohammadamint
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'ene_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 2, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 2, 28),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'feb_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 3, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 3, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'mar_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 4, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 4, 30),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'abr_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 5, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 5, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'may_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 6, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 6, 30),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'jun_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 7, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 7, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'jul_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 8, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 8, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'ago_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 9, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 9, 30),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'sep_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 10, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 10, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'oct_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 11, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 11, 30),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'nov_5LC.csv')
    #----------------------------------------------------------------
    if __name__ == "__main__":
        from ramp.core.core import UseCase

        uc = UseCase(
            users=User_list,
            parallel_processing=False,
            date_start=datetime(2023, 12, 1),  # <-- fecha de inicio deseada
            date_end=datetime(2023, 12, 31),   # <-- fecha final deseada
        )
        uc.initialize(peak_enlarge=0.15)

        Profiles_list = uc.generate_daily_load_profiles(flat=False)

        # post-processing
        from ramp.post_process import post_process as pp

        Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
            Profiles_list
        )
        pp.Profile_series_plot(
            Profiles_series
        )  # by default, profiles are plotted as a series
        
        if (
            len(Profiles_list) > 1
        ):  # if more than one daily profile is generated, also cloud plots are shown
            pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
            
        # this would be a new method using work of @mohammadamint
        pp.export_series(Profiles_series, j=None, fname= None, ofname= 'dic_5LC.csv')