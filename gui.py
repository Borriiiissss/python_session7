import data_load_save
def user_request():
    
    print (' 1 - get info')
    print (' 2 - add info')    
    print (' 3 - delete info')
    print (' 4 - import info')
    print (' 5 - export info')
    
    match (int(input(''))):
        case 1:
            data_load_save.find_info()
        case 2:
            data_load_save.add_info()
        case 3:
            data_load_save.delete_info()
        case 4:
            data_load_save.import_info()
        case 5:
            data_load_save.export_info()
    return

