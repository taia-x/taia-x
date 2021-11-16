#!/bin/bash

# Use this as an alternative to deploy.js (change values)

tezos-client originate contract <contract_name> for <user> transferring <amount_tez> from <from_user> running <tz_file> --init '<initial_storage>' --burn-cap <gaz_fee>
