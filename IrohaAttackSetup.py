from IrohaCommands import (
    create_native_iroha_keys,
    set_details_to_user,
    create_account,
    user_grants_to_admin_set_account_detail_permission,
)

local_user_name = input("\nEnter New User: ")

user_private_key, user_public_key = create_native_iroha_keys(local_user_name)
print("Public Key: ", user_public_key)
print("Private Key: ", user_private_key)

print("\nCreating new account: ")
create_account(
    local_user_name.split("@")[0], local_user_name.split("@")[1], user_public_key
)


print("Granting permissions: ")
user_grants_to_admin_set_account_detail_permission(local_user_name, user_private_key)


print("Initializing account details: ")
set_details_to_user(local_user_name, "0", "0", "0")

# Attack
local_attacker_name = input("Enter Attacker: ")

attacker_private_key, attacker_public_key = create_native_iroha_keys(
    local_attacker_name
)
print("Public Key: ", attacker_public_key)
print("Private Key: ", attacker_private_key)

print("\nCreating new account: ")
create_account(
    local_attacker_name.split("@")[0],
    local_attacker_name.split("@")[1],
    attacker_public_key,
)

print("Attempting user details overwriting: ")
set_details_to_user(
    local_user_name,
    "0",
    "0",
    "0",
    creator_id=local_attacker_name,
    private_key=attacker_private_key,
)
