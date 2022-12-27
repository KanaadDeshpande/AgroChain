import os
import json
import binascii
import commons

from iroha import IrohaCrypto, Iroha, IrohaGrpc
from iroha.primitive_pb2 import can_set_my_account_detail


IROHA_HOST_ADDR = os.getenv("IROHA_HOST_ADDR", "127.0.0.1")
IROHA_PORT = os.getenv("IROHA_PORT", "50051")
ADMIN_ACCOUNT_ID = os.getenv("ADMIN_ACCOUNT_ID", "admin@test")
ADMIN_PRIVATE_KEY = os.getenv(
    "ADMIN_PRIVATE_KEY",
    "f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70",
)


iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc("{}:{}".format(IROHA_HOST_ADDR, IROHA_PORT))

admin = commons.new_user("admin@test")
iroha = Iroha(admin["id"])


def create_native_iroha_keys(
    account_id, creator_id=ADMIN_ACCOUNT_ID, private_key=ADMIN_PRIVATE_KEY
):
    private_key = IrohaCrypto.private_key()
    public_key = IrohaCrypto.derive_public_key(private_key)
    with open(
        os.path.join(os.getcwd(), "Code", "iroha", "example", f"{account_id}.priv"),
        "wb",
    ) as f:
        f.write(private_key)

    with open(
        os.path.join(os.getcwd(), "Code", "iroha", "example", f"{account_id}.pub"), "wb"
    ) as f:
        f.write(public_key)
    return private_key, public_key


def send_transaction_and_print_status(transaction):
    hex_hash = binascii.hexlify(IrohaCrypto.hash(transaction))
    print(
        "Transaction hash = {}, creator = {}".format(
            hex_hash, transaction.payload.reduced_payload.creator_account_id
        )
    )
    net.send_tx(transaction)
    for status in net.tx_status_stream(transaction):
        print(status)
    print("=" * 100)


def create_account(
    account_id: str,
    domain: str,
    user_public_key: str,
    creator_id=ADMIN_ACCOUNT_ID,
    private_key=ADMIN_PRIVATE_KEY,
):
    tx = iroha.transaction(
        [
            iroha.command(
                "CreateAccount",
                account_name=account_id,
                domain_id=domain,
                public_key=user_public_key,
            )
        ],
        creator_account=creator_id,
    )
    IrohaCrypto.sign_transaction(tx, private_key)
    send_transaction_and_print_status(tx)


def create_domain_and_asset(
    domain: str,
    asset_short_id: str,
    precision=2,
    default_role="user",
    creator_id=ADMIN_ACCOUNT_ID,
    private_key=ADMIN_PRIVATE_KEY,
):
    commands = [
        iroha.command(
            "CreateDomain",
            domain_id=domain,
            default_role=default_role,
            private_key=ADMIN_PRIVATE_KEY,
        ),
        iroha.command(
            "CreateAsset",
            asset_name=asset_short_id,
            domain_id=domain,
            precision=precision,
        ),
    ]
    tx = IrohaCrypto.sign_transaction(
        iroha.transaction(
            commands,
            creator_account=creator_id,
        ),
        private_key,
    )
    send_transaction_and_print_status(tx)


def user_grants_to_admin_set_account_detail_permission(
    creator_id: str, private_key=ADMIN_PRIVATE_KEY
):
    tx = iroha.transaction(
        [
            iroha.command(
                "GrantPermission",
                account_id=ADMIN_ACCOUNT_ID,
                permission=can_set_my_account_detail,
            )
        ],
        creator_account=creator_id,
    )
    IrohaCrypto.sign_transaction(tx, private_key)
    send_transaction_and_print_status(tx)


def set_details_to_user(
    account_id: str,
    temperature: str,
    humidity: str,
    moisture: str,
    creator_id=ADMIN_ACCOUNT_ID,
    private_key=ADMIN_PRIVATE_KEY,
):
    tx = iroha.transaction(
        [
            iroha.command(
                "SetAccountDetail",
                account_id=account_id,
                key="temperature",
                value=temperature,
            ),
            iroha.command(
                "SetAccountDetail",
                account_id=account_id,
                key="humidity",
                value=humidity,
            ),
            iroha.command(
                "SetAccountDetail",
                account_id=account_id,
                key="moisture",
                value=moisture,
            ),
        ],
        creator_account=creator_id,
    )
    IrohaCrypto.sign_transaction(tx, private_key)
    send_transaction_and_print_status(tx)


def get_user_details(
    account_id: str, creator_id=ADMIN_ACCOUNT_ID, private_key=ADMIN_PRIVATE_KEY
):
    query = iroha.query(
        "GetAccountDetail", creator_account=creator_id, account_id=account_id
    )
    IrohaCrypto.sign_query(query, private_key)

    response = net.send_query(query)
    data = response.account_detail_response
    return data.detail


def update_details_of_user(
    account_id: str,
    key: str,
    value: str,
    creator_id=ADMIN_ACCOUNT_ID,
    private_key=ADMIN_PRIVATE_KEY,
):
    tx = iroha.transaction(
        [
            iroha.command(
                "SetAccountDetail", account_id=account_id, key=key, value=value
            )
        ],
        creator_account=creator_id,
    )
    IrohaCrypto.sign_transaction(tx, private_key)
    send_transaction_and_print_status(tx)


def get_data_from_blockchain_account(account_id: str):
    blockchain_account_data = get_user_details(account_id)
    blockchain_account_data = json.loads(blockchain_account_data)
    humidity = blockchain_account_data["admin@test"]["humidity"]
    temperature = blockchain_account_data["admin@test"]["temperature"]
    moisture = blockchain_account_data["admin@test"]["moisture"]
    return humidity, temperature, moisture
