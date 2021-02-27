from Management.models import Settings

def __set_transporter(transporter_size, transporter_key, transporters_count_for_city):
    transporters_count_for_city[transporter_key] = [transporter_size, transporters_count_for_city['soldiers_reminder'] // transporter_size]
    #transporters_count_for_city['%s_count' % transporter_key] = transporters_count_for_city['soldiers_reminder'] // transporter_size
    #transporters_count_for_city['%s_size' % transporter_key] = transporter_size
    transporters_count_for_city['soldiers_reminder'] = transporters_count_for_city['soldiers_reminder'] % transporter_size


def devide(cities_soldiers_count):


    settings = Settings.objects.get_settings()

    for soldiers_count_per_city in cities_soldiers_count:
        soldiers_count_per_city['soldiers_reminder'] = soldiers_count_per_city['soldiers_count']
        __set_transporter(settings.big_transporter_size, 'big_transporter', soldiers_count_per_city)
        __set_transporter(settings.medium_transporter_size, 'medium_transporter', soldiers_count_per_city)
        __set_transporter(settings.small_transporter_size, 'small_transporter', soldiers_count_per_city)


