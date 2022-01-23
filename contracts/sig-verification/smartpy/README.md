**Intended to be run on SmartPy´s [IDE](https://smartpy.io/ide).** 

The last scenario test,


`c1.verifySig3(pbk=ferdinand.public_key, provider_sig=sig3).run(valid=True)
`

inside sig_verification_v2 will only work if there was a previously added certificate.
The **_verifySig3()_** -function tests whether a certifier added a certificate for a dataset that is being bought by a consumer.