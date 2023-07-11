#saves the user listing image into a specific dierectory
def user_listing_path(instance,filename):
    return 'user_{0}/listings '.format(instance.user.id ,filename)