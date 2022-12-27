docker run --name some-postgres ^
-e POSTGRES_USER=postgres ^
-e POSTGRES_PASSWORD=mysecretpassword ^
-p 5432:5432 ^
--network=iroha-network ^
-d postgres:9.5 
