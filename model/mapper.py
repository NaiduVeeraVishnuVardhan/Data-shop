def get_model_inputs(service_name):
    '''

        Connect To DynamoDB
        Get row based on service_name
        Store the values in dict
        return dict

    '''

    model_maps_list = [
        {"name": "model1", "bucket": "ml-data-shop-store", "key" : "data/input/model1", "endpoint": "something.something.something.com"},
        {"name": "model2", "bucket": "ml-data-shop-store", "key" : "data/input/model2", "endpoint": "something.something.something.com"}
        ]

    for single_model_dict in model_maps_list:
        if (single_model_dict["name"] == service_name):
            return single_model_dict
