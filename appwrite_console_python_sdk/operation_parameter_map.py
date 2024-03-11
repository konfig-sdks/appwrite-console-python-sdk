operation_parameter_map = {
    '/account/mfa/authenticators/{type}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/account/verification-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa/challenge-PUT': {
        'parameters': [
            {
                'name': 'challengeId'
            },
            {
                'name': 'otp'
            },
        ]
    },
    '/account/recovery-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/verification/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/sessions/anonymous-POST': {
        'parameters': [
        ]
    },
    '/account/sessions/email-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/tokens/email-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account/verification-POST': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/account/jwt-POST': {
        'parameters': [
        ]
    },
    '/account/tokens/magic-url-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account/mfa/challenge-POST': {
        'parameters': [
            {
                'name': 'factor'
            },
        ]
    },
    '/account-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/account/sessions/oauth2/{provider}-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'success'
            },
            {
                'name': 'failure'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/account/tokens/oauth2/{provider}-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'success'
            },
            {
                'name': 'failure'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/account/recovery-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/account/tokens/phone-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/account/targets/push-POST': {
        'parameters': [
            {
                'name': 'targetId'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'providerId'
            },
        ]
    },
    '/account/sessions/token-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa/authenticators/{type}-DELETE': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/account/identities/{identityId}-DELETE': {
        'parameters': [
            {
                'name': 'identityId'
            },
        ]
    },
    '/account/targets/{targetId}/push-DELETE': {
        'parameters': [
            {
                'name': 'targetId'
            },
        ]
    },
    '/account/sessions-DELETE': {
        'parameters': [
        ]
    },
    '/account-DELETE': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-PATCH': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/mfa/recovery-codes-POST': {
        'parameters': [
        ]
    },
    '/account/mfa/recovery-codes-GET': {
        'parameters': [
        ]
    },
    '/account/prefs-GET': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account-GET': {
        'parameters': [
        ]
    },
    '/account/identities-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/mfa/factors-GET': {
        'parameters': [
        ]
    },
    '/account/sessions-GET': {
        'parameters': [
        ]
    },
    '/account/logs-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/mfa/recovery-codes-PATCH': {
        'parameters': [
        ]
    },
    '/account/verification/phone-POST': {
        'parameters': [
        ]
    },
    '/account/email-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/sessions/magic-url-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa-PATCH': {
        'parameters': [
            {
                'name': 'mfa'
            },
        ]
    },
    '/account/name-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/account/password-PATCH': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'oldPassword'
            },
        ]
    },
    '/account/phone-PATCH': {
        'parameters': [
            {
                'name': 'phone'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/sessions/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/prefs-PATCH': {
        'parameters': [
            {
                'name': 'prefs'
            },
        ]
    },
    '/account/targets/{targetId}/push-PUT': {
        'parameters': [
            {
                'name': 'identifier'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/account/status-PATCH': {
        'parameters': [
        ]
    },
    '/account/mfa/authenticators/{type}-PUT': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/console/assistant-POST': {
        'parameters': [
            {
                'name': 'prompt'
            },
        ]
    },
    '/avatars/qr-GET': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'size'
            },
            {
                'name': 'margin'
            },
            {
                'name': 'download'
            },
        ]
    },
    '/avatars/browsers/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/credit-cards/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/favicon-GET': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/avatars/flags/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/image-GET': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
        ]
    },
    '/avatars/initials-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'background'
            },
        ]
    },
    '/console/variables-GET': {
        'parameters': [
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/boolean-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections-POST': {
        'parameters': [
            {
                'name': 'collectionId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'documentSecurity'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/datetime-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-POST': {
        'parameters': [
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/email-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/enum-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'elements'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/float-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'type'
            },
            {
                'name': 'attributes'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'orders'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/integer-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/ip-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases-POST': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/relationship-POST': {
        'parameters': [
            {
                'name': 'relatedCollectionId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'twoWay'
            },
            {
                'name': 'key'
            },
            {
                'name': 'twoWayKey'
            },
            {
                'name': 'onDelete'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/string-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'size'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
            {
                'name': 'encrypt'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/url-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes/{key}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/usage-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'range'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes/{key}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/usage-GET': {
        'parameters': [
            {
                'name': 'range'
            },
        ]
    },
    '/databases/{databaseId}/usage-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'range'
            },
        ]
    },
    '/databases-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/logs-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}/logs-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/logs-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'documentSecurity'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-PATCH': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}-PATCH': {
        'parameters': [
            {
                'name': 'elements'
            },
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship-PATCH': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'onDelete'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/functions/{functionId}/deployments-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'activate'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
        ]
    },
    '/functions-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'runtime'
            },
            {
                'name': 'execute'
            },
            {
                'name': 'events'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'logging'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
            {
                'name': 'providerBranch'
            },
            {
                'name': 'providerSilentMode'
            },
            {
                'name': 'providerRootDirectory'
            },
            {
                'name': 'templateRepository'
            },
            {
                'name': 'templateOwner'
            },
            {
                'name': 'templateRootDirectory'
            },
            {
                'name': 'templateBranch'
            },
        ]
    },
    '/functions/{functionId}/variables-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'value'
            },
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}/download-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/executions/{executionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'executionId'
            },
        ]
    },
    '/functions/{functionId}/usage-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'range'
            },
        ]
    },
    '/functions/usage-GET': {
        'parameters': [
            {
                'name': 'range'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
        ]
    },
    '/functions-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/{functionId}/deployments-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/{functionId}/executions-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/runtimes-GET': {
        'parameters': [
        ]
    },
    '/functions/{functionId}/variables-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
            {
                'name': 'buildId'
            },
        ]
    },
    '/functions/{functionId}/executions-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'async'
            },
            {
                'name': 'path'
            },
            {
                'name': 'method'
            },
            {
                'name': 'headers'
            },
        ]
    },
    '/functions/{functionId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'runtime'
            },
            {
                'name': 'execute'
            },
            {
                'name': 'events'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'logging'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
            {
                'name': 'providerBranch'
            },
            {
                'name': 'providerSilentMode'
            },
            {
                'name': 'providerRootDirectory'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-PATCH': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/graphql-POST': {
        'parameters': [
        ]
    },
    '/graphql/mutation-POST': {
        'parameters': [
        ]
    },
    '/health/queue/certificates-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/health/anti-virus-GET': {
        'parameters': [
        ]
    },
    '/health/cache-GET': {
        'parameters': [
        ]
    },
    '/health/db-GET': {
        'parameters': [
        ]
    },
    '/health/storage/local-GET': {
        'parameters': [
        ]
    },
    '/health/queue-GET': {
        'parameters': [
        ]
    },
    '/health/storage-GET': {
        'parameters': [
        ]
    },
    '/health/queue/functions-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/builds-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/databases-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/failed/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/mails-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/messaging-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/migrations-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/deletes-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/logs-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/usage-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/certificate-GET': {
        'parameters': [
            {
                'name': 'domain'
            },
        ]
    },
    '/health/queue/usage-dump-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/pubsub-GET': {
        'parameters': [
        ]
    },
    '/health/time-GET': {
        'parameters': [
        ]
    },
    '/health/queue/webhooks-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/locale-GET': {
        'parameters': [
        ]
    },
    '/locale/codes-GET': {
        'parameters': [
        ]
    },
    '/locale/continents-GET': {
        'parameters': [
        ]
    },
    '/locale/countries-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/phones-GET': {
        'parameters': [
        ]
    },
    '/locale/currencies-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/eu-GET': {
        'parameters': [
        ]
    },
    '/locale/languages-GET': {
        'parameters': [
        ]
    },
    '/messaging/providers/apns-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'authKeyId'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'bundleId'
            },
            {
                'name': 'sandbox'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/email-POST': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'html'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/fcm-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'serviceAccountJSON'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/mailgun-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'isEuRegion'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/msg91-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'senderId'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/topics-POST': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subscribe'
            },
        ]
    },
    '/messaging/messages/push-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'messageId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'data'
            },
            {
                'name': 'action'
            },
            {
                'name': 'image'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'sound'
            },
            {
                'name': 'color'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'badge'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/sendgrid-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/sms-POST': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'content'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/smtp-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'host'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'autoTLS'
            },
            {
                'name': 'mailer'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers-POST': {
        'parameters': [
            {
                'name': 'subscriberId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/providers/telesign-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/textmagic-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'username'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/twilio-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'accountSid'
            },
            {
                'name': 'authToken'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/vonage-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'apiSecret'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/{messageId}-DELETE': {
        'parameters': [
            {
                'name': 'messageId'
            },
        ]
    },
    '/messaging/providers/{providerId}-DELETE': {
        'parameters': [
            {
                'name': 'providerId'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers/{subscriberId}-DELETE': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'subscriberId'
            },
        ]
    },
    '/messaging/topics/{topicId}-DELETE': {
        'parameters': [
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/messages/{messageId}-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
        ]
    },
    '/messaging/providers/{providerId}-GET': {
        'parameters': [
            {
                'name': 'providerId'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers/{subscriberId}-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'subscriberId'
            },
        ]
    },
    '/messaging/topics/{topicId}-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/messages-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/messages/{messageId}/logs-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/providers/{providerId}/logs-GET': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/providers-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/subscribers/{subscriberId}/logs-GET': {
        'parameters': [
            {
                'name': 'subscriberId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/messages/{messageId}/targets-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/topics/{topicId}/logs-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/topics-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/providers/apns/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'authKeyId'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'bundleId'
            },
            {
                'name': 'sandbox'
            },
        ]
    },
    '/messaging/messages/email/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'html'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/fcm/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'serviceAccountJSON'
            },
        ]
    },
    '/messaging/providers/mailgun/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'isEuRegion'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
        ]
    },
    '/messaging/providers/msg91/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'senderId'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/messages/push/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'body'
            },
            {
                'name': 'data'
            },
            {
                'name': 'action'
            },
            {
                'name': 'image'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'sound'
            },
            {
                'name': 'color'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'badge'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/sendgrid/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
        ]
    },
    '/messaging/messages/sms/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'content'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/smtp/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'host'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'autoTLS'
            },
            {
                'name': 'mailer'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/telesign/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/providers/textmagic/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'username'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/topics/{topicId}-PATCH': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subscribe'
            },
        ]
    },
    '/messaging/providers/twilio/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'accountSid'
            },
            {
                'name': 'authToken'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/providers/vonage/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'apiSecret'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/migrations/appwrite-POST': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'endpoint'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'apiKey'
            },
        ]
    },
    '/migrations/nhost-POST': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'subdomain'
            },
            {
                'name': 'region'
            },
            {
                'name': 'adminSecret'
            },
            {
                'name': 'database'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'port'
            },
        ]
    },
    '/migrations/{migrationId}-DELETE': {
        'parameters': [
            {
                'name': 'migrationId'
            },
        ]
    },
    '/migrations/firebase-POST': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'serviceAccount'
            },
        ]
    },
    '/migrations/firebase/oauth-POST': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/migrations/firebase/report-GET': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'serviceAccount'
            },
        ]
    },
    '/migrations/firebase/report/oauth-GET': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/migrations/nhost/report-GET': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'subdomain'
            },
            {
                'name': 'region'
            },
            {
                'name': 'adminSecret'
            },
            {
                'name': 'database'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'port'
            },
        ]
    },
    '/migrations/appwrite/report-GET': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'endpoint'
            },
            {
                'name': 'projectID'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/migrations/supabase/report-GET': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'endpoint'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'databaseHost'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'port'
            },
        ]
    },
    '/migrations/{migrationId}-GET': {
        'parameters': [
            {
                'name': 'migrationId'
            },
        ]
    },
    '/migrations/firebase/projects-GET': {
        'parameters': [
        ]
    },
    '/migrations-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/migrations/supabase-POST': {
        'parameters': [
            {
                'name': 'resources'
            },
            {
                'name': 'endpoint'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'databaseHost'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'port'
            },
        ]
    },
    '/migrations/{migrationId}-PATCH': {
        'parameters': [
            {
                'name': 'migrationId'
            },
        ]
    },
    '/migrations/firebase/deauthorize-GET': {
        'parameters': [
        ]
    },
    '/project/variables-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/project/variables/{variableId}-DELETE': {
        'parameters': [
            {
                'name': 'variableId'
            },
        ]
    },
    '/project/usage-GET': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'period'
            },
        ]
    },
    '/project/variables-GET': {
        'parameters': [
        ]
    },
    '/project/variables/{variableId}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'variableId'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/project/variables/{variableId}-GET': {
        'parameters': [
            {
                'name': 'variableId'
            },
        ]
    },
    '/projects/{projectId}/keys-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'expire'
            },
        ]
    },
    '/projects-POST': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'region'
            },
            {
                'name': 'logo'
            },
            {
                'name': 'url'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'legalCountry'
            },
            {
                'name': 'legalState'
            },
            {
                'name': 'legalCity'
            },
            {
                'name': 'legalAddress'
            },
            {
                'name': 'legalTaxId'
            },
        ]
    },
    '/projects/{projectId}/platforms-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'name'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'store'
            },
            {
                'name': 'hostname'
            },
        ]
    },
    '/projects/{projectId}/smtp/tests-POST': {
        'parameters': [
            {
                'name': 'emails'
            },
            {
                'name': 'senderName'
            },
            {
                'name': 'senderEmail'
            },
            {
                'name': 'host'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'replyTo'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'secure'
            },
        ]
    },
    '/projects/{projectId}/webhooks-POST': {
        'parameters': [
            {
                'name': 'security'
            },
            {
                'name': 'name'
            },
            {
                'name': 'events'
            },
            {
                'name': 'url'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'httpUser'
            },
            {
                'name': 'httpPass'
            },
        ]
    },
    '/projects/{projectId}/keys/{keyId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'keyId'
            },
        ]
    },
    '/projects/{projectId}/platforms/{platformId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'platformId'
            },
        ]
    },
    '/projects/{projectId}/webhooks/{webhookId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'webhookId'
            },
        ]
    },
    '/projects/{projectId}/auth/personal-data-PATCH': {
        'parameters': [
            {
                'name': 'enabled'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/templates/email/{type}/{locale}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/projects/{projectId}/keys/{keyId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'keyId'
            },
        ]
    },
    '/projects/{projectId}/platforms/{platformId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'platformId'
            },
        ]
    },
    '/projects/{projectId}/templates/sms/{type}/{locale}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/projects/{projectId}/webhooks/{webhookId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'webhookId'
            },
        ]
    },
    '/projects/{projectId}/keys-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/platforms-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/projects/{projectId}/webhooks-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/templates/email/{type}/{locale}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/projects/{projectId}/templates/sms/{type}/{locale}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/projects/{projectId}/api/all-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/service/all-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/api-PATCH': {
        'parameters': [
            {
                'name': 'api'
            },
            {
                'name': 'status'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/auth/duration-PATCH': {
        'parameters': [
            {
                'name': 'duration'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/auth/{method}-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'method'
            },
        ]
    },
    '/projects/{projectId}/auth/password-dictionary-PATCH': {
        'parameters': [
            {
                'name': 'enabled'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/auth/password-history-PATCH': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/templates/email/{type}/{locale}-PATCH': {
        'parameters': [
            {
                'name': 'subject'
            },
            {
                'name': 'message'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'senderName'
            },
            {
                'name': 'senderEmail'
            },
            {
                'name': 'replyTo'
            },
        ]
    },
    '/projects/{projectId}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'logo'
            },
            {
                'name': 'url'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'legalCountry'
            },
            {
                'name': 'legalState'
            },
            {
                'name': 'legalCity'
            },
            {
                'name': 'legalAddress'
            },
            {
                'name': 'legalTaxId'
            },
        ]
    },
    '/projects/{projectId}/keys/{keyId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'keyId'
            },
            {
                'name': 'expire'
            },
        ]
    },
    '/projects/{projectId}/auth/max-sessions-PATCH': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/oauth2-PATCH': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'appId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/projects/{projectId}/platforms/{platformId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'platformId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'store'
            },
            {
                'name': 'hostname'
            },
        ]
    },
    '/projects/{projectId}/service-PATCH': {
        'parameters': [
            {
                'name': 'service'
            },
            {
                'name': 'status'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/templates/sms/{type}/{locale}-PATCH': {
        'parameters': [
            {
                'name': 'message'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'locale'
            },
        ]
    },
    '/projects/{projectId}/smtp-PATCH': {
        'parameters': [
            {
                'name': 'enabled'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'senderName'
            },
            {
                'name': 'senderEmail'
            },
            {
                'name': 'replyTo'
            },
            {
                'name': 'host'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'secure'
            },
        ]
    },
    '/projects/{projectId}/team-PATCH': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/auth/limit-PATCH': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/projects/{projectId}/webhooks/{webhookId}-PUT': {
        'parameters': [
            {
                'name': 'security'
            },
            {
                'name': 'name'
            },
            {
                'name': 'events'
            },
            {
                'name': 'url'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'webhookId'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'httpUser'
            },
            {
                'name': 'httpPass'
            },
        ]
    },
    '/projects/{projectId}/webhooks/{webhookId}/signature-PATCH': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'webhookId'
            },
        ]
    },
    '/proxy/rules-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'resourceType'
            },
            {
                'name': 'resourceId'
            },
        ]
    },
    '/proxy/rules/{ruleId}-DELETE': {
        'parameters': [
            {
                'name': 'ruleId'
            },
        ]
    },
    '/proxy/rules/{ruleId}-GET': {
        'parameters': [
            {
                'name': 'ruleId'
            },
        ]
    },
    '/proxy/rules-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/proxy/rules/{ruleId}/verification-PATCH': {
        'parameters': [
            {
                'name': 'ruleId'
            },
        ]
    },
    '/storage/buckets-POST': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'fileSecurity'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'maximumFileSize'
            },
            {
                'name': 'allowedFileExtensions'
            },
            {
                'name': 'compression'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'antivirus'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-POST': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/storage/buckets/{bucketId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/storage/{bucketId}/usage-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'range'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/download-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/preview-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'gravity'
            },
            {
                'name': 'quality'
            },
            {
                'name': 'borderWidth'
            },
            {
                'name': 'borderColor'
            },
            {
                'name': 'borderRadius'
            },
            {
                'name': 'opacity'
            },
            {
                'name': 'rotation'
            },
            {
                'name': 'background'
            },
            {
                'name': 'output'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/view-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/usage-GET': {
        'parameters': [
            {
                'name': 'range'
            },
        ]
    },
    '/storage/buckets-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/storage/buckets/{bucketId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'bucketId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'fileSecurity'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'maximumFileSize'
            },
            {
                'name': 'allowedFileExtensions'
            },
            {
                'name': 'compression'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'antivirus'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-PUT': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/teams/{teamId}/memberships-POST': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'url'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'roles'
            },
        ]
    },
    '/teams/{teamId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/prefs-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/logs-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/teams/{teamId}/memberships-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-PATCH': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}/status-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/prefs-PUT': {
        'parameters': [
            {
                'name': 'prefs'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/users/argon2-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/bcrypt-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/md5-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/targets-POST': {
        'parameters': [
            {
                'name': 'targetId'
            },
            {
                'name': 'providerType'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/scrypt-modified-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordSalt'
            },
            {
                'name': 'passwordSaltSeparator'
            },
            {
                'name': 'passwordSignerKey'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/scrypt-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordSalt'
            },
            {
                'name': 'passwordCpu'
            },
            {
                'name': 'passwordMemory'
            },
            {
                'name': 'passwordParallel'
            },
            {
                'name': 'passwordLength'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/sessions-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/phpass-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/sha-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordVersion'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/mfa/authenticators/{type}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/identities/{identityId}-DELETE': {
        'parameters': [
            {
                'name': 'identityId'
            },
        ]
    },
    '/users/{userId}/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sessionId'
            },
        ]
    },
    '/users/{userId}/sessions-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/users/{userId}/tokens-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'length'
            },
            {
                'name': 'expire'
            },
        ]
    },
    '/users/{userId}/logs-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/users/{userId}/memberships-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/users/usage-GET': {
        'parameters': [
            {
                'name': 'range'
            },
        ]
    },
    '/users/{userId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/prefs-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/users/identities-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/users/{userId}/mfa/factors-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/sessions-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/email-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/verification-PATCH': {
        'parameters': [
            {
                'name': 'emailVerification'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/labels-PUT': {
        'parameters': [
            {
                'name': 'labels'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/mfa-PATCH': {
        'parameters': [
            {
                'name': 'mfa'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/name-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/password-PATCH': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/phone-PATCH': {
        'parameters': [
            {
                'name': 'number'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/verification/phone-PATCH': {
        'parameters': [
            {
                'name': 'phoneVerification'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/prefs-PATCH': {
        'parameters': [
            {
                'name': 'prefs'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/status-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/repositories/{repositoryId}-PATCH': {
        'parameters': [
            {
                'name': 'providerPullRequestId'
            },
            {
                'name': 'installationId'
            },
            {
                'name': 'repositoryId'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/providerRepositories-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'private'
            },
            {
                'name': 'installationId'
            },
        ]
    },
    '/vcs/installations/{installationId}-DELETE': {
        'parameters': [
            {
                'name': 'installationId'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}/detection-POST': {
        'parameters': [
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
            {
                'name': 'providerRootDirectory'
            },
        ]
    },
    '/vcs/installations/{installationId}-GET': {
        'parameters': [
            {
                'name': 'installationId'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}-GET': {
        'parameters': [
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
        ]
    },
    '/vcs/installations-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/providerRepositories-GET': {
        'parameters': [
            {
                'name': 'installationId'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/vcs/github/installations/{installationId}/providerRepositories/{providerRepositoryId}/branches-GET': {
        'parameters': [
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
        ]
    },
};