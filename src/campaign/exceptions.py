from fastapi import HTTPException


def campaing_not_found(type, id):
    return HTTPException(
        status_code=404, detail=f"The {type} with the id {id} doesn't exist"
    )


def invalid_user_role_exception(name):
    return HTTPException(
        status_code=403, detail=f"User {name} doesn't have the required role"
    )

def invalid_user_exception(id_list):
    return HTTPException(
        status_code=404, detail=f"The campaing can't be created because the user(s) with the id {id_list} doesn't exist"
    )

def invalid_user_exception_on_update(id_list):
    return HTTPException(
        status_code=404, detail=f"The campaing can't be updated because the user(s) with the id {id_list} doesn't exist"
    )


duplicated_name_exception = HTTPException(
    403, "The name of the campaign you're trying to create already exist"
)
grouping_not_found_exception = HTTPException(404, "Client not found")
user_not_found_exception = HTTPException(404, "Users not found")
campaigns_not_found_by_grouping_id = HTTPException(
    404, "There are no campaigns associated to the grouping's id passed"
)
campaigns_not_found_by_agent_id = HTTPException(
    404, "There are no campaigns associated to the agent's id passed"
)

create_campaign_exception = HTTPException(
    500, "There was an error trying to create the campaign"
)
update_campaign_exception = HTTPException(
    500, "There was an error trying to update the campaign"
)
get_campaign_by_id_exception = HTTPException(
    500, "There was an error trying to find the campaign by id"
)
get_campaigns_exception = HTTPException(
    500, "There was an error trying to find the campaigns"
)
add_users_to_campaing_exception = HTTPException(
    500, "There was an error trying to add the users to the campaign"
)
validate_user_exception = HTTPException(
    500, "There was an error trying to find the user"
)
get_groupings_campaigns_exception = HTTPException(
    500, "There was an error trying to find the grouping's campaings"
)
get_agents_campaigns_exception = HTTPException(
    500, "There was an error trying to find the agent's campaings"
)
