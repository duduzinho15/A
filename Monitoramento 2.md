2026-02-15T20:10:50.184Z | info  | Initializing n8n process {"file":"start.js","function":"init"}
2026-02-15T20:10:50.378Z | debug | Lazy-loading nodes and credentials from n8n-nodes-base {"nodes":477,"credentials":385,"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.396Z | debug | Lazy-loading nodes and credentials from @n8n/n8n-nodes-langchain {"nodes":114,"credentials":28,"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.427Z | debug | Can't enable lazy-loading {"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.539Z | debug | No codex available for: googleSearchConsole {"file":"directory-loader.js","function":"addCodex"}
2026-02-15T20:10:50.564Z | debug | Loaded all credentials and nodes from n8n-nodes-google-search-console {"credentials":1,"nodes":1,"file":"package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.583Z | debug | Can't enable lazy-loading {"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.743Z | debug | No codex available for: blotato {"file":"directory-loader.js","function":"addCodex"}
2026-02-15T20:10:50.770Z | debug | Loaded all credentials and nodes from @blotato/n8n-nodes-blotato {"credentials":1,"nodes":1,"file":"package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:50.787Z | debug | Can't enable lazy-loading {"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:51.094Z | debug | Loaded all credentials and nodes from @searchapi/n8n-nodes-searchapi {"credentials":1,"nodes":1,"file":"package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:51.110Z | debug | Can't enable lazy-loading {"file":"lazy-package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:52.681Z | debug | Loaded all credentials and nodes from @brave/n8n-nodes-brave-search {"credentials":1,"nodes":1,"file":"package-directory-loader.js","function":"loadAll"}
2026-02-15T20:10:52.835Z | debug | Context establishment hooks feature is disabled {"file":"load-nodes-and-credentials.js","function":"injectContextEstablishmentHooks"}
2026-02-15T20:10:53.026Z | info  | n8n ready on ::, port 5678 {"file":"abstract-server.js","function":"init"}
2026-02-15T20:10:53.106Z | debug | Initializing AuthRolesService... {"file":"auth.roles.service.js","function":"init"}
2026-02-15T20:10:53.124Z | debug | No scopes to update. {"file":"auth.roles.service.js","function":"syncScopes"}
2026-02-15T20:10:53.124Z | debug | No obsolete scopes to delete. {"file":"auth.roles.service.js","function":"syncScopes"}
2026-02-15T20:10:53.179Z | debug | No global roles to update. {"file":"auth.roles.service.js","function":"syncRoles"}
2026-02-15T20:10:53.179Z | debug | No project roles to update. {"file":"auth.roles.service.js","function":"syncRoles"}
2026-02-15T20:10:53.179Z | debug | No credential roles to update. {"file":"auth.roles.service.js","function":"syncRoles"}
2026-02-15T20:10:53.179Z | debug | No workflow roles to update. {"file":"auth.roles.service.js","function":"syncRoles"}
2026-02-15T20:10:53.179Z | debug | AuthRolesService initialized successfully. {"file":"auth.roles.service.js","function":"init"}
2026-02-15T20:10:53.199Z | warn  | n8n detected that some packages are missing. For more information, visit <https://docs.n8n.io/integrations/community-nodes/troubleshooting/> {"file":"community-packages.service.js","function":"checkForMissingPackages"}
2026-02-15T20:10:53.221Z | info  | n8n Task Broker ready on 127.0.0.1, port 5679 {"file":"task-broker-server.js","function":"setupHttpServer"}
2026-02-15T20:10:53.285Z | warn  | Failed to start Python task runner in internal mode. because Python 3 is missing from this system. Launching a Python runner in internal mode is intended only for debugging and is not recommended for production. Users are encouraged to deploy in external mode. See: <https://docs.n8n.io/hosting/configuration/task-runners/#setting-up-external-mode> {"scopes":["task-runner"],"file":"task-runner-module.js","function":"startInternalTaskRunners"}
2026-02-15T20:10:53.333Z | debug | [license SDK] initializing for deviceFingerprint 3812d373830822120641f24942341cb1c44f224eadbf0c02c4eadaa9c57e8918 {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:53.362Z | info  | [license SDK] attempting license renewal {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:53.363Z | debug | License initialized {"scopes":["license"],"file":"license.js","function":"init"}
2026-02-15T20:10:53.364Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:10:53.366Z | debug | Started tracking waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"startTracking"}
2026-02-15T20:10:53.366Z | debug | Wait tracker init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.367Z | debug | Loading overwrite credentials from static envvar {"file":"credentials-overwrites.js","function":"init"}
2026-02-15T20:10:53.367Z | debug | Credentials overwrites init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.375Z | debug | Binary data service init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.376Z | debug | Data deduplication service init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.376Z | debug | External hooks init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.377Z | debug | Workflow history init complete {"file":"start.js","function":"init"}
2026-02-15T20:10:53.473Z | debug | Test runner cleanup complete {"file":"start.js","function":"init"}
2026-02-15T20:10:55.740Z | info  | Registered runner "JS Task Runner" (5N_l8_MIIVgtRVwMBRTyF)  {"file":"task-broker-ws-server.js","function":"onMessage"}
2026-02-15T20:10:55.902Z | debug | Started flushing timer {"scopes":["insights"],"file":"insights-collection.service.js","function":"init"}
2026-02-15T20:10:55.903Z | debug | Started compaction timer {"scopes":["insights"],"file":"insights-compaction.service.js","function":"startCompactionTimer"}
2026-02-15T20:10:55.903Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.903Z | debug | Started pruning timer {"scopes":["insights"],"file":"insights-pruning.service.js","function":"startPruningTimer"}
2026-02-15T20:10:55.907Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.907Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.907Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.907Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.907Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.907Z | debug | Initialized module "insights" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:55.908Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:55.908Z | debug | Skipped init for unlicensed module "external-secrets" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:55.913Z | debug | Initialized module "community-packages" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:55.977Z | debug | Initialized module "data-table" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.246Z | debug | Initialized module "mcp" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.246Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.246Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.246Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.246Z | debug | Skipped init for unlicensed module "provisioning" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.267Z | debug | Initialized module "breaking-changes" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.268Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.268Z | debug | Skipped init for unlicensed module "source-control" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.268Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.268Z | debug | Skipped init for unlicensed module "dynamic-credentials" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.306Z | debug | Initialized module "chat-hub" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.306Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.306Z | debug | Skipped init for unlicensed module "sso-oidc" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.306Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.306Z | debug | Skipped init for unlicensed module "sso-saml" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.306Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.307Z | debug | Skipped init for unlicensed module "log-streaming" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.307Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:56.307Z | debug | Skipped init for unlicensed module "ldap" {"file":"module-registry.js","function":"initModules"}
2026-02-15T20:10:56.308Z | debug | Registering 1 execution context hooks. {"file":"execution-context-hook-registry.service.js","function":"init"}
2026-02-15T20:10:56.437Z | debug | Context establishment hooks feature is disabled {"file":"load-nodes-and-credentials.js","function":"injectContextEstablishmentHooks"}
2026-02-15T20:10:57.050Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.222Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.223Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.223Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.223Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.224Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.230Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.231Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.231Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.231Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.231Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.231Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.232Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.232Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.232Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.232Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.233Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.235Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.237Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.417Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.847Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.847Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.847Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.847Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.848Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.849Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.850Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.851Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.852Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:10:57.899Z | debug | Registered a "reload-license" event handler on License#reload {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.899Z | debug | Registered a "relay-execution-lifecycle-event" event handler on Push#handleRelayExecutionLifecycleEvent {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.899Z | debug | Registered a "reload-overwrite-credentials" event handler on CredentialsOverwrites#reloadOverwriteCredentials {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.900Z | debug | Registered a "clear-test-webhooks" event handler on TestWebhooks#handleClearTestWebhooks {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.900Z | debug | Registered a "display-workflow-activation" event handler on ActiveWorkflowManager#handleDisplayWorkflowActivation {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.900Z | debug | Registered a "display-workflow-deactivation" event handler on ActiveWorkflowManager#handleDisplayWorkflowDeactivation {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.900Z | debug | Registered a "display-workflow-activation-error" event handler on ActiveWorkflowManager#handleDisplayWorkflowActivationError {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.900Z | debug | Registered a "add-webhooks-triggers-and-pollers" event handler on ActiveWorkflowManager#handleAddWebhooksTriggersAndPollers {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.901Z | debug | Registered a "remove-triggers-and-pollers" event handler on ActiveWorkflowManager#handleRemoveTriggersAndPollers {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.902Z | debug | Registered a "response-to-get-worker-status" event handler on WorkerStatusService#handleWorkerStatusResponse {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.902Z | debug | Registered a "community-package-update" event handler on CommunityPackagesService#handleInstallEvent {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.902Z | debug | Registered a "community-package-install" event handler on CommunityPackagesService#handleInstallEvent {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.902Z | debug | Registered a "community-package-uninstall" event handler on CommunityPackagesService#handleUninstallEvent {"scopes":["pubsub"],"file":"pubsub.registry.js","function":"init"}
2026-02-15T20:10:57.946Z | debug | Registered rule: removed-nodes-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.946Z | debug | Registered rule: process-env-access-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.946Z | debug | Registered rule: pyodide-removed-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.946Z | debug | Registered rule: file-access-restriction-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.947Z | debug | Registered rule: disabled-nodes-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.947Z | debug | Registered rule: wait-node-subworkflow-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.947Z | debug | Registered rule: start-node-removed-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.947Z | debug | Registered rule: dotenv-upgrade-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.948Z | debug | Registered rule: oauth-callback-auth-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.948Z | debug | Registered rule: cli-activate-all-workflows-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.948Z | debug | Registered rule: workflow-hooks-deprecated-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.949Z | debug | Registered rule: queue-worker-max-stalled-count-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.949Z | debug | Registered rule: tunnel-option-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.949Z | debug | Registered rule: removed-database-types-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.949Z | debug | Registered rule: settings-file-permissions-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.950Z | debug | Registered rule: task-runners-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.950Z | debug | Registered rule: task-runner-docker-image-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.950Z | debug | Registered rule: binary-data-storage-v2 {"scopes":["breaking-changes"],"file":"breaking-changes.rule-registry.service.js","function":"register"}
2026-02-15T20:10:57.967Z | debug | Initializing event bus... {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:10:57.967Z | debug | Initializing event writer {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:10:57.972Z | debug | Checking for unsent event messages {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:10:59.630Z | debug | Start logging into /home/node/.n8n/.n8n/n8nEventLog.log  {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.034Z | info  | Currently active workflows: {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.035Z | info  |    - 00 - Proxy RSS (Via Flaresolverr) (ID: 4auQBC2bRYwCGkRMzPpAO) {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.035Z | info  |    - 01 - Coletor Limpo (ID: 6vM1reKwp7N8gzDwieX_X) {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.035Z | info  |    - Save Log File (ID: log-extractor-enhanced) {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.035Z | info  |    - workflow_producao_v6_timeout (ID: TP_RFBFPlmwik3ug0txZJ) {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:00.514Z | info  | [Recovery] Logs available, amended execution {"executionId":"754","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:00.809Z | debug | Executing hook (hookFunctionsSave) {"executionId":"754","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:00.811Z | debug | Save execution data to database for execution ID 754 {"executionId":"754","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T02:10:21.518Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:01.381Z | info  | [Recovery] Logs available, amended execution {"executionId":"755","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:01.607Z | debug | Executing hook (hookFunctionsSave) {"executionId":"755","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:01.607Z | debug | Save execution data to database for execution ID 755 {"executionId":"755","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T03:40:21.420Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:03.655Z | debug | Skipped browserId check on /rest/push {"file":"auth.service.js","function":"resolveJwt"}
2026-02-15T20:11:03.656Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:03.659Z | debug | Add editor-UI session {"pushRef":"gskldamqp0","file":"abstract.push.js","function":"add"}
2026-02-15T20:11:03.673Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:04.200Z | info  | [Recovery] Logs available, amended execution {"executionId":"760","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:04.321Z | debug | Received message from editor-UI {"pushRef":"gskldamqp0","msg":{"type":"workflowOpened","workflowId":"TP_RFBFPlmwik3ug0txZJ"},"file":"abstract.push.js","function":"onMessageReceived"}
2026-02-15T20:11:04.343Z | debug | Pushed to frontend: collaboratorsChanged {"dataType":"collaboratorsChanged","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:04.453Z | debug | Executing hook (hookFunctionsSave) {"executionId":"760","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:04.453Z | debug | Save execution data to database for execution ID 760 {"executionId":"760","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T08:10:57.381Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:04.660Z | debug | Pushed to frontend: executionRecovered {"dataType":"executionRecovered","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:04.661Z | debug | Pushed to frontend: executionRecovered {"dataType":"executionRecovered","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:04.938Z | info  | [Recovery] Logs available, amended execution {"executionId":"761","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:05.103Z | debug | Executing hook (hookFunctionsSave) {"executionId":"761","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:05.103Z | debug | Save execution data to database for execution ID 761 {"executionId":"761","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T09:40:57.403Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:05.701Z | info  | [Recovery] Logs available, amended execution {"executionId":"762","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:05.952Z | debug | Executing hook (hookFunctionsSave) {"executionId":"762","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:05.952Z | debug | Save execution data to database for execution ID 762 {"executionId":"762","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T11:10:57.472Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:06.693Z | info  | [Recovery] Logs available, amended execution {"executionId":"763","file":"execution-recovery.service.js","function":"recoverFromLogs"}
(node:7) [DEP0060] DeprecationWarning: The `util._extend` API is deprecated. Please use Object.assign() instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
2026-02-15T20:11:06.917Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:06.918Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:08.333Z | debug | Executing hook (hookFunctionsSave) {"executionId":"763","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:08.333Z | debug | Save execution data to database for execution ID 763 {"executionId":"763","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T12:40:57.457Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:08.503Z | debug | Execution added {"executionId":"780","file":"active-executions.js","function":"add"}
2026-02-15T20:11:08.552Z | debug | Execution for workflow workflow_producao_v6_timeout was assigned id 780 {"executionId":"780","file":"workflow-runner.js","function":"runMainProcess"}
2026-02-15T20:11:08.560Z | debug | Execution ID 780 will run executing all nodes. {"executionId":"780","file":"manual-execution.service.js","function":"runManually"}
2026-02-15T20:11:08.563Z | debug | Workflow execution started {"workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:08.609Z | debug | Executing hook (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:08.610Z | debug | Pushed to frontend: executionStarted {"dataType":"executionStarted","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:08.613Z | debug | Start executing node "Monitora FreshRSS" {"node":"Monitora FreshRSS","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:08.615Z | debug | Executing hook on node "Monitora FreshRSS" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:08.616Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:08.617Z | debug | Running node "Monitora FreshRSS" started {"node":"Monitora FreshRSS","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.006Z | info  | [Recovery] Logs available, amended execution {"executionId":"766","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:09.096Z | debug | Running node "Monitora FreshRSS" finished successfully {"node":"Monitora FreshRSS","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.097Z | debug | Executing hook on node "Monitora FreshRSS" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:09.098Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.098Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.099Z | debug | Start executing node "É Novo?" {"node":"É Novo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.099Z | debug | Executing hook on node "É Novo?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:09.099Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.100Z | debug | Running node "É Novo?" started {"node":"É Novo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.133Z | debug | Running node "É Novo?" finished successfully {"node":"É Novo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.133Z | debug | Executing hook on node "É Novo?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:09.134Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.134Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.135Z | debug | Start executing node "IA Triagem" {"node":"IA Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.135Z | debug | Executing hook on node "IA Triagem" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:09.135Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:11:09.135Z | debug | Running node "IA Triagem" started {"node":"IA Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:11:09.329Z | debug | Executing hook (hookFunctionsSave) {"executionId":"766","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:09.330Z | debug | Save execution data to database for execution ID 766 {"executionId":"766","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T14:10:43.382Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:09.844Z | info  | [Recovery] Logs available, amended execution {"executionId":"769","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:10.053Z | debug | Executing hook (hookFunctionsSave) {"executionId":"769","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:10.054Z | debug | Save execution data to database for execution ID 769 {"executionId":"769","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T16:10:06.347Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:10.610Z | info  | [Recovery] Logs available, amended execution {"executionId":"770","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:10.854Z | debug | Executing hook (hookFunctionsSave) {"executionId":"770","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:10.854Z | debug | Save execution data to database for execution ID 770 {"executionId":"770","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T16:40:06.415Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:11.502Z | info  | [Recovery] Logs available, amended execution {"executionId":"773","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:11.785Z | debug | Executing hook (hookFunctionsSave) {"executionId":"773","workflowId":"F6siU1iJzcr0DsqD","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:11.785Z | debug | Save execution data to database for execution ID 773 {"executionId":"773","workflowId":"F6siU1iJzcr0DsqD","finished":false,"stoppedAt":"2026-02-15T18:10:06.651Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:12.118Z | info  | [Recovery] Logs available, amended execution {"executionId":"777","file":"execution-recovery.service.js","function":"recoverFromLogs"}
2026-02-15T20:11:12.174Z | debug | Executing hook (hookFunctionsSave) {"executionId":"777","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:11:12.175Z | debug | Save execution data to database for execution ID 777 {"executionId":"777","workflowId":"TP_RFBFPlmwik3ug0txZJ","finished":false,"stoppedAt":"2026-02-15T19:40:50.306Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:11:12.230Z | warn  | Found unfinished executions: 754, 755, 760, 761, 762, 763, 766, 769, 770, 773, 777 {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:12.231Z | info  | This could be due to a crash of an active workflow or a restart of n8n {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:12.231Z | debug | MessageEventBus initialized {"file":"message-event-bus.js","function":"initialize"}
2026-02-15T20:11:12.234Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:12.234Z | info  | Version: 2.6.4 {"file":"abstract-server.js","function":"start"}
2026-02-15T20:11:12.234Z | debug | Server ID: main-960a00dc076a {"file":"server.js","function":"start"}
2026-02-15T20:11:12.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:12.236Z | error | [license SDK] cert is invalid because it has expired: (autorenewalsEnabled: true, expiredAt: Tue Feb 10 2026 19:16:15 GMT-0300 (Brasilia Standard Time), issuedAt: Sat Jan 31 2026 19:16:15 GMT-0300 (Brasilia Standard Time)) {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:11:12.237Z | debug | Soft-deletion every 60 minutes {"scopes":["pruning"],"file":"executions-pruning.service.js","function":"scheduleRollingSoftDeletions"}
2026-02-15T20:11:12.238Z | debug | Hard-deletion in next 15 minutes {"scopes":["pruning"],"file":"executions-pruning.service.js","function":"scheduleNextHardDeletion"}
2026-02-15T20:11:12.238Z | debug | Started pruning timers {"scopes":["pruning"],"file":"executions-pruning.service.js","function":"startPruning"}
2026-02-15T20:11:12.240Z | debug | Started workflow histories optimization and trimming {"scopes":["workflow-history-compaction"],"optimizingMinimumAgeHours":0.25,"optimizingTimeWindowHours":2,"trimmingMinimumAgeDays":7,"trimmingTimeWindowDays":2,"batchSize":100,"batchDelayMs":1000,"trimOnStartUp":false,"file":"workflow-history-compaction.service.js","function":"startCompacting"}
2026-02-15T20:11:12.240Z | debug | Optimizing histories every 1 hour(s) {"scopes":["workflow-history-compaction"],"file":"workflow-history-compaction.service.js","function":"scheduleOptimization"}
2026-02-15T20:11:12.241Z | debug | Starting workflow history compaction {"scopes":["workflow-history-compaction"],"dateRange":{"start":"2026-02-15T17:56:12.241Z","end":"2026-02-15T19:56:12.241Z"},"config":{"optimizingMinimumAgeHours":0.25,"optimizingTimeWindowHours":2,"trimmingMinimumAgeDays":7,"trimmingTimeWindowDays":2,"batchSize":100,"batchDelayMs":1000,"trimOnStartUp":false},"file":"workflow-history-compaction.service.js","function":"compactHistories"}
2026-02-15T20:11:12.242Z | debug | Trimming histories once a day at 3am server time {"scopes":["workflow-history-compaction"],"file":"workflow-history-compaction.service.js","function":"scheduleTrimming"}
2026-02-15T20:11:12.248Z [Rudder] debug: in flush
2026-02-15T20:11:12.258Z [Rudder] debug: no existing flush timer, creating new one
2026-02-15T20:11:12.282Z | debug | Found 2 workflows with versions between 2026-02-15T17:56:12.241Z and 2026-02-15T19:56:12.241Z {"scopes":["workflow-history-compaction"],"file":"workflow-history-compaction.service.js","function":"compactHistories"}
2026-02-15T20:11:12.285Z | info  | Start Active Workflows: {"scopes":["workflow-activation"],"file":"active-workflow-manager.js","function":"addActiveWorkflows"}
2026-02-15T20:11:12.326Z | debug | Deleted 0 of 1 versions of workflow F6siU1iJzcr0DsqD between 2026-02-15T17:56:12.241Z and 2026-02-15T19:56:12.241Z {"scopes":["workflow-history-compaction"],"file":"workflow-history-compaction.service.js","function":"compactHistories"}
2026-02-15T20:11:12.352Z | debug | Added webhooks for workflow "01 - Coletor Limpo" (ID 6vM1reKwp7N8gzDwieX_X) {"scopes":["workflow-activation"],"workflowId":"6vM1reKwp7N8gzDwieX_X","file":"active-workflow-manager.js","function":"addWebhooks"}
2026-02-15T20:11:12.393Z | info  | Activated workflow "01 - Coletor Limpo" (ID: 6vM1reKwp7N8gzDwieX_X) {"scopes":["workflow-activation"],"workflowName":"01 - Coletor Limpo","workflowId":"6vM1reKwp7N8gzDwieX_X","file":"active-workflow-manager.js","function":"activateWorkflow"}
2026-02-15T20:11:12.400Z | debug | Deleted 5 of 18 versions of workflow TP_RFBFPlmwik3ug0txZJ between 2026-02-15T17:56:12.241Z and 2026-02-15T19:56:12.241Z {"scopes":["workflow-history-compaction"],"file":"workflow-history-compaction.service.js","function":"compactHistories"}
2026-02-15T20:11:12.401Z | debug | Workflow history compaction complete {"scopes":["workflow-history-compaction"],"workflowsProcessed":2,"totalVersionsSeen":19,"totalVersionsDeleted":5,"errorCount":0,"durationMs":160,"compactionStartTime":"2026-02-15T20:11:12.241Z","windowStartIso":"2026-02-15T17:56:12.241Z","windowEndIso":"2026-02-15T19:56:12.241Z","file":"workflow-history-compaction.service.js","function":"compactHistories"}
2026-02-15T20:11:12.417Z | debug | Added webhooks for workflow "00 - Proxy RSS (Via Flaresolverr)" (ID 4auQBC2bRYwCGkRMzPpAO) {"scopes":["workflow-activation"],"workflowId":"4auQBC2bRYwCGkRMzPpAO","file":"active-workflow-manager.js","function":"addWebhooks"}
2026-02-15T20:11:12.423Z | info  | Activated workflow "00 - Proxy RSS (Via Flaresolverr)" (ID: 4auQBC2bRYwCGkRMzPpAO) {"scopes":["workflow-activation"],"workflowName":"00 - Proxy RSS (Via Flaresolverr)","workflowId":"4auQBC2bRYwCGkRMzPpAO","file":"active-workflow-manager.js","function":"activateWorkflow"}
2026-02-15T20:11:12.448Z | debug | Polling trigger initiated for workflow "workflow_producao_v6_timeout" {"workflowName":"workflow_producao_v6_timeout","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"active-workflows.js","function":"executeTrigger"}
2026-02-15T20:11:12.699Z | debug | Registered cron for workflow {"scopes":["cron"],"workflowId":"TP_RFBFPlmwik3ug0txZJ","cron":"28 */10* ** *","instanceRole":"leader","file":"scheduled-task-manager.js","function":"registerCron"}
2026-02-15T20:11:12.699Z | debug | Added triggers and pollers for workflow "workflow_producao_v6_timeout" (ID: TP_RFBFPlmwik3ug0txZJ) {"scopes":["workflow-activation"],"file":"active-workflow-manager.js","function":"addTriggersAndPollers"}
2026-02-15T20:11:12.704Z | info  | Activated workflow "workflow_producao_v6_timeout" (ID: TP_RFBFPlmwik3ug0txZJ) {"scopes":["workflow-activation"],"workflowName":"workflow_producao_v6_timeout","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"active-workflow-manager.js","function":"activateWorkflow"}
2026-02-15T20:11:12.789Z | debug | Added webhooks for workflow "Save Log File" (ID log-extractor-enhanced) {"scopes":["workflow-activation"],"workflowId":"log-extractor-enhanced","file":"active-workflow-manager.js","function":"addWebhooks"}
2026-02-15T20:11:12.790Z | debug | Added triggers and pollers for workflow "Save Log File" (ID: log-extractor-enhanced) {"scopes":["workflow-activation"],"file":"active-workflow-manager.js","function":"addTriggersAndPollers"}
2026-02-15T20:11:12.797Z | info  | Activated workflow "Save Log File" (ID: log-extractor-enhanced) {"scopes":["workflow-activation"],"workflowName":"Save Log File","workflowId":"log-extractor-enhanced","file":"active-workflow-manager.js","function":"activateWorkflow"}
2026-02-15T20:11:12.797Z | debug | Finished activating all workflows {"scopes":["workflow-activation"],"file":"active-workflow-manager.js","function":"addActiveWorkflows"}
2026-02-15T20:11:12.798Z | info  |
Editor is now accessible via:
<http://localhost:5679> {"file":"base-command.js","function":"log"}
2026-02-15T20:11:22.258Z [Rudder] debug: in flush
2026-02-15T20:11:22.258Z [Rudder] debug: cancelling existing flushTimer...
2026-02-15T20:11:25.901Z | debug | Flushing 22 insights {"scopes":["insights"],"file":"insights-collection.service.js","function":"saveInsightsMetadataAndRaw"}
2026-02-15T20:11:25.907Z | debug | Saving 2 insights metadata for workflows {"scopes":["insights"],"file":"insights-collection.service.js","function":"saveInsightsMetadataAndRaw"}
2026-02-15T20:11:25.932Z | debug | Inserting 22 insights raw {"scopes":["insights"],"file":"insights-collection.service.js","function":"saveInsightsMetadataAndRaw"}
2026-02-15T20:11:53.361Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:12:04.043Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.047Z | debug | Running node "IA Triagem" finished successfully {"node":"IA Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.048Z | debug | Executing hook on node "IA Triagem" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.048Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.049Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.049Z | debug | Start executing node "Parse Triagem" {"node":"Parse Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.050Z | debug | Executing hook on node "Parse Triagem" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.050Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.051Z | debug | Running node "Parse Triagem" started {"node":"Parse Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.145Z | debug | Running node "Parse Triagem" finished successfully {"node":"Parse Triagem","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.146Z | debug | Executing hook on node "Parse Triagem" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.146Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.146Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.147Z | debug | Start executing node "Vale Vídeo?" {"node":"Vale Vídeo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.147Z | debug | Executing hook on node "Vale Vídeo?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.147Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.148Z | debug | Running node "Vale Vídeo?" started {"node":"Vale Vídeo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.160Z | debug | Running node "Vale Vídeo?" finished successfully {"node":"Vale Vídeo?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.161Z | debug | Executing hook on node "Vale Vídeo?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.161Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.162Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.162Z | debug | Start executing node "Definir Prioridade" {"node":"Definir Prioridade","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.163Z | debug | Executing hook on node "Definir Prioridade" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.163Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.163Z | debug | Running node "Definir Prioridade" started {"node":"Definir Prioridade","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.165Z | debug | Running node "Definir Prioridade" finished successfully {"node":"Definir Prioridade","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.166Z | debug | Executing hook on node "Definir Prioridade" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.166Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.166Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.167Z | debug | Start executing node "Descobre Link Real" {"node":"Descobre Link Real","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:04.167Z | debug | Executing hook on node "Descobre Link Real" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:04.168Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:04.168Z | debug | Running node "Descobre Link Real" started {"node":"Descobre Link Real","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.203Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.204Z | debug | Running node "Descobre Link Real" finished successfully {"node":"Descobre Link Real","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.204Z | debug | Executing hook on node "Descobre Link Real" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:05.204Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.205Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.213Z | debug | Start executing node "Extrai Link Real do Google" {"node":"Extrai Link Real do Google","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.213Z | debug | Executing hook on node "Extrai Link Real do Google" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:05.213Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.213Z | debug | Running node "Extrai Link Real do Google" started {"node":"Extrai Link Real do Google","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.312Z | debug | Running node "Extrai Link Real do Google" finished successfully {"node":"Extrai Link Real do Google","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.314Z | debug | Executing hook on node "Extrai Link Real do Google" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:05.314Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.315Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.315Z | debug | Start executing node "Leitor Trafilatura" {"node":"Leitor Trafilatura","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:05.316Z | debug | Executing hook on node "Leitor Trafilatura" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:05.316Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:05.317Z | debug | Running node "Leitor Trafilatura" started {"node":"Leitor Trafilatura","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.279Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.281Z | debug | Running node "Leitor Trafilatura" finished successfully {"node":"Leitor Trafilatura","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.282Z | debug | Executing hook on node "Leitor Trafilatura" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:10.282Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.282Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.282Z | debug | Start executing node "Extrai Midias" {"node":"Extrai Midias","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.283Z | debug | Executing hook on node "Extrai Midias" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:10.283Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.283Z | debug | Running node "Extrai Midias" started {"node":"Extrai Midias","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.343Z | debug | Running node "Extrai Midias" finished successfully {"node":"Extrai Midias","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.343Z | debug | Executing hook on node "Extrai Midias" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:10.344Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.344Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.345Z | debug | Start executing node "Delay Rate Limit" {"node":"Delay Rate Limit","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:10.345Z | debug | Executing hook on node "Delay Rate Limit" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:10.345Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:10.346Z | debug | Running node "Delay Rate Limit" started {"node":"Delay Rate Limit","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:15.360Z | debug | Running node "Delay Rate Limit" finished successfully {"node":"Delay Rate Limit","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:15.360Z | debug | Executing hook on node "Delay Rate Limit" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:15.360Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:15.361Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:15.361Z | debug | Start executing node "Google Suggest" {"node":"Google Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:15.362Z | debug | Executing hook on node "Google Suggest" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:15.362Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:15.362Z | debug | Running node "Google Suggest" started {"node":"Google Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:15.692Z | debug | Request proxied to Axios failed {"status":400,"file":"request-helper-functions.js","function":"proxyRequestToAxios"}
2026-02-15T20:12:15.694Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:20.844Z | debug | Request proxied to Axios failed {"status":400,"file":"request-helper-functions.js","function":"proxyRequestToAxios"}
2026-02-15T20:12:20.845Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.015Z | debug | Request proxied to Axios failed {"status":400,"file":"request-helper-functions.js","function":"proxyRequestToAxios"}
2026-02-15T20:12:26.017Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.018Z | debug | Running node "Google Suggest" finished successfully {"node":"Google Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.018Z | debug | Executing hook on node "Google Suggest" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.019Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.019Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.020Z | debug | Start executing node "IF Erro Suggest" {"node":"IF Erro Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.021Z | debug | Executing hook on node "IF Erro Suggest" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.021Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.023Z | debug | Running node "IF Erro Suggest" started {"node":"IF Erro Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.032Z | debug | Running node "IF Erro Suggest" finished successfully {"node":"IF Erro Suggest","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.035Z | debug | Executing hook on node "IF Erro Suggest" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.035Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.036Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.036Z | debug | Start executing node "ScoreBat (Python)" {"node":"ScoreBat (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.038Z | debug | Executing hook on node "ScoreBat (Python)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.038Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.039Z | debug | Running node "ScoreBat (Python)" started {"node":"ScoreBat (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.536Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.537Z | debug | Running node "ScoreBat (Python)" finished successfully {"node":"ScoreBat (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.538Z | debug | Executing hook on node "ScoreBat (Python)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.538Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.539Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.540Z | debug | Start executing node "IA Roteiro Master" {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:26.540Z | debug | Executing hook on node "IA Roteiro Master" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:12:26.540Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:12:26.541Z | debug | Running node "IA Roteiro Master" started {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:12:53.355Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:13:06.858Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.860Z | debug | Running node "IA Roteiro Master" finished successfully {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:06.861Z | debug | Executing hook on node "IA Roteiro Master" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:06.861Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.862Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.862Z | debug | Start executing node "Parse Roteiro" {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:06.862Z | debug | Executing hook on node "Parse Roteiro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:06.863Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.863Z | debug | Running node "Parse Roteiro" started {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:06.899Z | debug | Running node "Parse Roteiro" finished successfully {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:06.899Z | debug | Executing hook on node "Parse Roteiro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:06.899Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.900Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.900Z | debug | Start executing node "Brave Images" {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:06.900Z | debug | Executing hook on node "Brave Images" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:06.900Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:06.901Z | debug | Running node "Brave Images" started {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.214Z | debug | Running node "Brave Images" finished successfully {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.215Z | debug | Executing hook on node "Brave Images" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:08.215Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.215Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.219Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.220Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:08.220Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.220Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.223Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.223Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:08.223Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.224Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.224Z | debug | Start executing node "Serper Videos" {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:08.225Z | debug | Executing hook on node "Serper Videos" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:08.225Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:08.225Z | debug | Running node "Serper Videos" started {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.205Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.207Z | debug | Running node "Serper Videos" finished successfully {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.207Z | debug | Executing hook on node "Serper Videos" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:09.207Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.208Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.208Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.209Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:09.209Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.210Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.210Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.211Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:09.211Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.211Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.212Z | debug | Start executing node "Brave Web" {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:09.212Z | debug | Executing hook on node "Brave Web" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:09.212Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:09.213Z | debug | Running node "Brave Web" started {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.385Z | debug | Running node "Brave Web" finished successfully {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.385Z | debug | Executing hook on node "Brave Web" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:10.386Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.386Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.387Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.387Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:10.387Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.387Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.388Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.388Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:10.388Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.388Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.389Z | debug | Start executing node "Serper News" {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:10.389Z | debug | Executing hook on node "Serper News" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:10.389Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:10.390Z | debug | Running node "Serper News" started {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.106Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.108Z | debug | Running node "Serper News" finished successfully {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.109Z | debug | Executing hook on node "Serper News" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:11.109Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.109Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.110Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.110Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:11.111Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.111Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.111Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.112Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:11.112Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.112Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.113Z | debug | Start executing node "Tavily AI" {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:11.113Z | debug | Executing hook on node "Tavily AI" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:11.114Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:11.114Z | debug | Running node "Tavily AI" started {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.180Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.182Z | debug | Running node "Tavily AI" finished successfully {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.182Z | debug | Executing hook on node "Tavily AI" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:13.182Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.183Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.183Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.184Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:13.184Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.184Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.185Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.186Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:13.186Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.186Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.187Z | debug | Start executing node "IA Metadata" {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:13.187Z | debug | Executing hook on node "IA Metadata" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:13:13.188Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:13:13.188Z | debug | Running node "IA Metadata" started {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:13:53.352Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:14:07.670Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.671Z | debug | Running node "IA Metadata" finished successfully {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.671Z | debug | Executing hook on node "IA Metadata" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.672Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.672Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.672Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.673Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.673Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.673Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.674Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.674Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.674Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.675Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.675Z | debug | Start executing node "Pexels API" {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.675Z | debug | Executing hook on node "Pexels API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.676Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.676Z | debug | Running node "Pexels API" started {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.736Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.740Z | debug | Running node "Pexels API" finished successfully {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.740Z | debug | Executing hook on node "Pexels API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.740Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.741Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.743Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.743Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.744Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.744Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.745Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.745Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.745Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.746Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.747Z | debug | Start executing node "Serper Search" {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:07.747Z | debug | Executing hook on node "Serper Search" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:07.747Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:07.748Z | debug | Running node "Serper Search" started {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.599Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.601Z | debug | Running node "Serper Search" finished successfully {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.601Z | debug | Executing hook on node "Serper Search" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:08.602Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.602Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.603Z | debug | Start executing node "Agrupador Master Assets" {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.603Z | debug | Executing hook on node "Agrupador Master Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:08.603Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.604Z | debug | Running node "Agrupador Master Assets" started {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.663Z | debug | Running node "Agrupador Master Assets" finished successfully {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.663Z | debug | Executing hook on node "Agrupador Master Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:08.664Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.664Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.665Z | debug | Start executing node "Baixa Capa" {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:08.665Z | debug | Executing hook on node "Baixa Capa" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:08.665Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:08.665Z | debug | Running node "Baixa Capa" started {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.105Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.217Z | debug | Running node "Baixa Capa" finished successfully {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.218Z | debug | Executing hook on node "Baixa Capa" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:09.218Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.219Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.219Z | debug | Start executing node "Espera Randomica" {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.220Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:09.220Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.220Z | debug | Running node "Espera Randomica" started {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.227Z | debug | Setting execution status for 780 to "waiting" {"file":"workflow-execute-additional-data.js","function":"setExecutionStatus"}
2026-02-15T20:14:09.227Z | debug | Running node "Espera Randomica" finished successfully {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.228Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:09.228Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.228Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.230Z | debug | Workflow execution will wait until Sun Feb 15 2026 17:15:55 GMT-0300 (Brasilia Standard Time) {"workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:14:09.230Z | debug | Executing hook (hookFunctionsSave) {"executionId":"780","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:09.230Z | debug | Save execution data to database for execution ID 780 {"executionId":"780","workflowId":"TP_RFBFPlmwik3ug0txZJ","finished":false,"stoppedAt":"2026-02-15T20:14:09.230Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:14:09.328Z | debug | Executing hook (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:14:09.329Z | debug | Pushed to frontend: executionWaiting {"dataType":"executionWaiting","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:14:09.329Z | debug | Execution finalized {"executionId":"780","file":"active-executions.js","function":"finalizeExecution"}
2026-02-15T20:14:53.346Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:14:53.350Z | debug | Found 1 executions. Setting timer for IDs: 780 {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:15:53.342Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:15:53.344Z | debug | Found 1 executions. Setting timer for IDs: 780 {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:15:55.223Z | debug | Resuming execution 780 {"scopes":["waiting-executions"],"executionId":"780","file":"wait-tracker.js","function":"startExecution"}
2026-02-15T20:15:55.332Z | debug | Execution added {"executionId":"780","file":"active-executions.js","function":"add"}
2026-02-15T20:15:55.341Z | debug | Execution for workflow workflow_producao_v6_timeout was assigned id 780 {"executionId":"780","file":"workflow-runner.js","function":"runMainProcess"}
2026-02-15T20:15:55.347Z | debug | Execution ID 780 had Execution data. Running with payload. {"executionId":"780","file":"workflow-runner.js","function":"runMainProcess"}
2026-02-15T20:15:55.348Z | debug | Workflow execution started {"workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.350Z | debug | Start executing node "Espera Randomica" {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.350Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:15:55.350Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.351Z | debug | Running node "Espera Randomica" started {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.351Z | debug | Running node "Espera Randomica" finished successfully {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.352Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:15:55.352Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.352Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.353Z | debug | Start executing node "Gera Vídeo Híbrido" {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.354Z | debug | Executing hook on node "Gera Vídeo Híbrido" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:15:55.354Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.354Z | debug | Running node "Gera Vídeo Híbrido" started {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.474Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.476Z | debug | Running node "Gera Vídeo Híbrido" finished successfully {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.476Z | debug | Executing hook on node "Gera Vídeo Híbrido" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:15:55.476Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.477Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.477Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:15:55.478Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:15:55.478Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:15:55.478Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.477Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.478Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.478Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.478Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.479Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.479Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.479Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.480Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.550Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.552Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.552Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.552Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.553Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.553Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.554Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.554Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.554Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.608Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.609Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.609Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.609Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.610Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.611Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.611Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.611Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.616Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.616Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.616Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.617Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.617Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:25.617Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:25.618Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:25.618Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:53.337Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:16:55.618Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.618Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.618Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.619Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.619Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.620Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.620Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.621Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.687Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.688Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.688Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.689Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.689Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.690Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.690Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.690Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.690Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.757Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.757Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.758Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.758Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.759Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.759Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.759Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.759Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.761Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.761Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.762Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.762Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.763Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:16:55.763Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:16:55.764Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:16:55.764Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.763Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.763Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.764Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.764Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.765Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.765Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.765Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.766Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.843Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.845Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.845Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.846Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.846Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.846Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.847Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.847Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.848Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.920Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.921Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.921Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.922Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.922Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.923Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.923Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.923Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.924Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.924Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.924Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.925Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.925Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:25.926Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:25.926Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:25.926Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:53.333Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:17:55.925Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:55.925Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:55.925Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.926Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.926Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:55.927Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:55.927Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.927Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:55.990Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.991Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:55.991Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:55.991Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.992Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.992Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:55.993Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:55.993Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:55.994Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.062Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.062Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:56.063Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.063Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.064Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.064Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:56.065Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.065Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.066Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.067Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:56.067Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.068Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.071Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:17:56.072Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:17:56.072Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:17:56.073Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.070Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.071Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.071Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.072Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.072Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.073Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.073Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.074Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.137Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.139Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.139Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.139Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.139Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.140Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.140Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.141Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.141Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.198Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.198Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.198Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.199Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.199Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.200Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.200Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.200Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.201Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.202Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.202Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.203Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.203Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:26.204Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:26.204Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:26.204Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:53.329Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:18:56.203Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.204Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.205Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.205Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.207Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.207Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.207Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.208Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.279Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.281Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.281Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.282Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.282Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.283Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.283Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.284Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.284Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.356Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.356Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.357Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.357Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.358Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.358Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.358Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.358Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.360Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.360Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.360Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.361Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.362Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:18:56.362Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:18:56.362Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:18:56.363Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.363Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.363Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.363Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.364Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.364Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.365Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.365Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.365Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.430Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.431Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.431Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.432Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.432Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.433Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.433Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.433Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.434Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.495Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.496Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.496Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.497Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.497Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.498Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.498Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.498Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.500Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.501Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.502Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.502Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.503Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:26.504Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:26.505Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:26.506Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:53.325Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:19:56.504Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.504Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.504Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.505Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.505Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.505Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.506Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.506Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.566Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.568Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.568Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.568Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.569Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.569Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.570Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.570Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.570Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.632Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.632Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.632Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.633Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.633Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.633Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.634Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.634Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.636Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.637Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.637Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.638Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.638Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:19:56.639Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:19:56.639Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:19:56.640Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.638Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.638Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.638Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.639Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.639Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.639Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.640Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.640Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.711Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.713Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.713Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.713Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.714Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.714Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.715Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.715Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.715Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.784Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.785Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.785Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.785Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.786Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.786Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.786Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.787Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.788Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.788Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.788Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.789Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.790Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:26.790Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:26.790Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:26.790Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:28.005Z | debug | Executing cron for workflow {"scopes":["cron"],"workflowId":"TP_RFBFPlmwik3ug0txZJ","nodeId":"b70b8012-3104-479f-a6a1-0de467f7e603","cron":"28*/10 ** **","instanceRole":"leader","file":"scheduled-task-manager.js"}
2026-02-15T20:20:28.006Z | debug | Polling trigger initiated for workflow "workflow_producao_v6_timeout" {"workflowName":"workflow_producao_v6_timeout","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"active-workflows.js","function":"executeTrigger"}
2026-02-15T20:20:53.321Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:20:56.788Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.789Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.789Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.789Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.790Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.790Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.790Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.791Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.872Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.874Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.875Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.875Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.876Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.876Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.877Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.877Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.877Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.947Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.948Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.948Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.949Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.950Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.950Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.950Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.951Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.952Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.952Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.953Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.953Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.953Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:20:56.954Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:20:56.954Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:20:56.955Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:26.952Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:26.953Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:26.953Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:26.954Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:26.954Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:26.955Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:26.955Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:26.955Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.023Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.024Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.025Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.025Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.026Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.026Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.027Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.027Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.027Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.088Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.088Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.089Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.089Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.090Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.090Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.090Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.090Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.092Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.092Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.092Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.093Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.094Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:27.094Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:27.094Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:27.095Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:53.317Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:21:57.094Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.095Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.095Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.095Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.096Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.096Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.096Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.096Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.165Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.166Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.167Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.167Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.168Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.168Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.168Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.169Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.169Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.238Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.238Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.238Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.239Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.239Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.240Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.240Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.240Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.242Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.243Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.243Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.243Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.244Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:21:57.244Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:21:57.245Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:21:57.245Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.245Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.245Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.245Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.246Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.246Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.247Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.247Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.247Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.314Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.315Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.316Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.317Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.317Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.318Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.318Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.318Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.319Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.379Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.379Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.379Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.380Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.381Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.381Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.381Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.382Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.383Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.383Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.384Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.384Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.385Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:27.385Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:27.385Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:27.386Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:53.312Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:22:57.384Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.384Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.385Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.385Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.385Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.386Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.386Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.386Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.453Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.454Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.455Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.455Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.455Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.456Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.456Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.456Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.457Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.528Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.528Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.528Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.529Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.529Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.530Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.530Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.530Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.532Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.532Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.532Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.533Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.533Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:22:57.534Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:22:57.534Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:22:57.537Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.535Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.535Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.536Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.536Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.537Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.537Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.537Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.537Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.601Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.602Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.602Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.603Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.603Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.604Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.604Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.604Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.604Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.659Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.659Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.660Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.660Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.660Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.661Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.661Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.661Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.662Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.662Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.662Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.663Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.663Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:27.663Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:27.664Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:27.664Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:53.307Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:23:57.662Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.662Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.663Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.663Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.664Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.664Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.664Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.664Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.742Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.744Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.745Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.745Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.745Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.746Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.747Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.747Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.747Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.818Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.818Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.818Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.819Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.819Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.820Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.820Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.820Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.821Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.822Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.822Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.822Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.823Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:23:57.823Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:23:57.823Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:23:57.824Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.822Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.823Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.823Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.823Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.824Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.824Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.824Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.825Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.889Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.891Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.892Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.892Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.892Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.893Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.893Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.893Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.894Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.951Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.951Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.951Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.952Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.952Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.953Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.953Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.953Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.954Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.955Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.955Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.956Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.956Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:27.957Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:27.957Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:27.957Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:53.303Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:24:57.956Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:57.957Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:57.957Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:57.957Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:57.958Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:57.958Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:57.958Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:57.959Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.022Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.023Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.024Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.024Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.025Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.025Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.025Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.026Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.026Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.087Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.087Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.087Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.088Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.088Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.089Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.089Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.089Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.091Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.091Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.091Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.092Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.092Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:24:58.093Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:24:58.093Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:24:58.093Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.091Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.091Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.091Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.092Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.092Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.092Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.093Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.093Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.154Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.156Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.156Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.156Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.157Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.157Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.158Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.158Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.158Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.213Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.214Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.214Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.214Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.215Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.215Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.215Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.216Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.217Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.217Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.217Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.217Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.218Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:28.218Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:28.218Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:28.219Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:53.294Z | info  | [license SDK] attempting license renewal {"scopes":["license"],"file":"LicenseManager.js","function":"log"}
2026-02-15T20:25:53.298Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:25:58.218Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.218Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.218Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.218Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.219Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.219Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.219Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.220Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.290Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.292Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.292Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.293Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.293Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.294Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.294Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.294Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.294Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.402Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.403Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.403Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.403Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.404Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.404Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.405Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.405Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.414Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.418Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.418Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.419Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.420Z | debug | Start executing node "Is Timeout?" {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.421Z | debug | Executing hook on node "Is Timeout?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.421Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.422Z | debug | Running node "Is Timeout?" started {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.430Z | debug | Running node "Is Timeout?" finished successfully {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.431Z | debug | Executing hook on node "Is Timeout?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.431Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.433Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.434Z | debug | Start executing node "Job Succeeded?" {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.434Z | debug | Executing hook on node "Job Succeeded?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.434Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.436Z | debug | Running node "Job Succeeded?" started {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.438Z | debug | Running node "Job Succeeded?" finished successfully {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.439Z | debug | Executing hook on node "Job Succeeded?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.439Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.439Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.441Z | debug | Start executing node "Mark Job Failed" {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.442Z | debug | Executing hook on node "Mark Job Failed" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.442Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.443Z | debug | Running node "Mark Job Failed" started {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.564Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.567Z | debug | Running node "Mark Job Failed" finished successfully {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.568Z | debug | Executing hook on node "Mark Job Failed" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.568Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.568Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.569Z | debug | Start executing node "Pixabay API" {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:58.569Z | debug | Executing hook on node "Pixabay API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:58.569Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:58.570Z | debug | Running node "Pixabay API" started {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.126Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.129Z | debug | Running node "Pixabay API" finished successfully {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.129Z | debug | Executing hook on node "Pixabay API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:59.130Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.130Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.131Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.131Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:59.131Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.132Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.132Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.132Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:59.133Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.134Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.135Z | debug | Start executing node "Serper.dev (Images)" {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:25:59.135Z | debug | Executing hook on node "Serper.dev (Images)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:25:59.135Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:25:59.136Z | debug | Running node "Serper.dev (Images)" started {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.147Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.150Z | debug | Running node "Serper.dev (Images)" finished successfully {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.151Z | debug | Executing hook on node "Serper.dev (Images)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:00.151Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.152Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.152Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.153Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:00.153Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.153Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.155Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.155Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:00.155Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.156Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.156Z | debug | Start executing node "SearXNG" {"node":"SearXNG","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:00.157Z | debug | Executing hook on node "SearXNG" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:00.157Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:00.157Z | debug | Running node "SearXNG" started {"node":"SearXNG","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.341Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.346Z | debug | Running node "SearXNG" finished successfully {"node":"SearXNG","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.347Z | debug | Executing hook on node "SearXNG" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:04.347Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.348Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.353Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.355Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:04.355Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.356Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.357Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.358Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:04.358Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.359Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.359Z | debug | Start executing node "Gaveta VIP (Embeds)" {"node":"Gaveta VIP (Embeds)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:04.359Z | debug | Executing hook on node "Gaveta VIP (Embeds)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:04.360Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:04.360Z | debug | Running node "Gaveta VIP (Embeds)" started {"node":"Gaveta VIP (Embeds)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:05.984Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:05.991Z | debug | Running node "Gaveta VIP (Embeds)" finished successfully {"node":"Gaveta VIP (Embeds)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:05.993Z | debug | Executing hook on node "Gaveta VIP (Embeds)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:05.995Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:05.996Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.000Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.000Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.000Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.001Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.001Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.002Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.002Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.002Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.003Z | debug | Start executing node "Próximos Jogos (Free)" {"node":"Próximos Jogos (Free)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.003Z | debug | Executing hook on node "Próximos Jogos (Free)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.003Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.004Z | debug | Running node "Próximos Jogos (Free)" started {"node":"Próximos Jogos (Free)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.028Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.032Z | debug | Running node "Próximos Jogos (Free)" finished successfully {"node":"Próximos Jogos (Free)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.032Z | debug | Executing hook on node "Próximos Jogos (Free)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.033Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.033Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.034Z | debug | Start executing node "Odds (Python)" {"node":"Odds (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.037Z | debug | Executing hook on node "Odds (Python)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.037Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.038Z | debug | Running node "Odds (Python)" started {"node":"Odds (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.068Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.070Z | debug | Running node "Odds (Python)" finished successfully {"node":"Odds (Python)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.070Z | debug | Executing hook on node "Odds (Python)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.070Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.071Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.071Z | debug | Start executing node "Agente de Apostas Pro" {"node":"Agente de Apostas Pro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:06.072Z | debug | Executing hook on node "Agente de Apostas Pro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:06.072Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:06.072Z | debug | Running node "Agente de Apostas Pro" started {"node":"Agente de Apostas Pro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:12.172Z | debug | Found no executions to hard-delete {"scopes":["pruning"],"file":"executions-pruning.service.js","function":"hardDelete"}
2026-02-15T20:26:12.172Z | debug | Hard-deletion in next 15 minutes {"scopes":["pruning"],"file":"executions-pruning.service.js","function":"scheduleNextHardDeletion"}
2026-02-15T20:26:38.977Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.978Z | debug | Running node "Agente de Apostas Pro" finished successfully {"node":"Agente de Apostas Pro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:38.980Z | debug | Executing hook on node "Agente de Apostas Pro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:38.980Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.981Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.982Z | debug | Start executing node "Envio Telegram Apostas" {"node":"Envio Telegram Apostas","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:38.982Z | debug | Executing hook on node "Envio Telegram Apostas" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:38.982Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.983Z | debug | Running node "Envio Telegram Apostas" started {"node":"Envio Telegram Apostas","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:38.984Z | debug | Running node "Envio Telegram Apostas" finished successfully {"node":"Envio Telegram Apostas","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:38.984Z | debug | Executing hook on node "Envio Telegram Apostas" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:38.984Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.985Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.985Z | debug | Start executing node "IA Roteiro Master" {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:38.986Z | debug | Executing hook on node "IA Roteiro Master" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:38.986Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:38.986Z | debug | Running node "IA Roteiro Master" started {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:53.293Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:26:57.075Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.076Z | debug | Running node "IA Roteiro Master" finished successfully {"node":"IA Roteiro Master","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:57.076Z | debug | Executing hook on node "IA Roteiro Master" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:57.076Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.077Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.077Z | debug | Start executing node "Parse Roteiro" {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:57.078Z | debug | Executing hook on node "Parse Roteiro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:57.078Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.078Z | debug | Running node "Parse Roteiro" started {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:57.124Z | debug | Running node "Parse Roteiro" finished successfully {"node":"Parse Roteiro","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:57.125Z | debug | Executing hook on node "Parse Roteiro" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:57.125Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.126Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.126Z | debug | Start executing node "Brave Images" {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:57.127Z | debug | Executing hook on node "Brave Images" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:57.127Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:57.127Z | debug | Running node "Brave Images" started {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.291Z | debug | Running node "Brave Images" finished successfully {"node":"Brave Images","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.292Z | debug | Executing hook on node "Brave Images" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:58.292Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.292Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.294Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.295Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:58.295Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.295Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.296Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.296Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:58.296Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.297Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.297Z | debug | Start executing node "Serper Videos" {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:58.297Z | debug | Executing hook on node "Serper Videos" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:58.298Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:58.298Z | debug | Running node "Serper Videos" started {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.022Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.024Z | debug | Running node "Serper Videos" finished successfully {"node":"Serper Videos","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.024Z | debug | Executing hook on node "Serper Videos" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:59.024Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.025Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.025Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.026Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:59.026Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.026Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.027Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.027Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:59.027Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.027Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.028Z | debug | Start executing node "Brave Web" {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:26:59.028Z | debug | Executing hook on node "Brave Web" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:26:59.028Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:26:59.029Z | debug | Running node "Brave Web" started {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.263Z | debug | Running node "Brave Web" finished successfully {"node":"Brave Web","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.264Z | debug | Executing hook on node "Brave Web" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:00.264Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.264Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.265Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.265Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:00.265Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.265Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.266Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.267Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:00.267Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.268Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.268Z | debug | Start executing node "Serper News" {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:00.269Z | debug | Executing hook on node "Serper News" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:00.269Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:00.270Z | debug | Running node "Serper News" started {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.204Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.206Z | debug | Running node "Serper News" finished successfully {"node":"Serper News","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.207Z | debug | Executing hook on node "Serper News" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:01.207Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.207Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.208Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.208Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:01.208Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.209Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.209Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.210Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:01.210Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.210Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.210Z | debug | Start executing node "Tavily AI" {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:01.211Z | debug | Executing hook on node "Tavily AI" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:01.211Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:01.211Z | debug | Running node "Tavily AI" started {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.073Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.074Z | debug | Running node "Tavily AI" finished successfully {"node":"Tavily AI","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.075Z | debug | Executing hook on node "Tavily AI" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:04.075Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.075Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.076Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.076Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:04.076Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.076Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.077Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.077Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:04.078Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.078Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.078Z | debug | Start executing node "IA Metadata" {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:04.079Z | debug | Executing hook on node "IA Metadata" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:27:04.079Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:27:04.080Z | debug | Running node "IA Metadata" started {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:27:53.290Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:28:05.945Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.946Z | debug | Running node "IA Metadata" finished successfully {"node":"IA Metadata","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:05.947Z | debug | Executing hook on node "IA Metadata" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:05.948Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.948Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.949Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:05.950Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:05.950Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.950Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:05.951Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:05.951Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:05.952Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.952Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.953Z | debug | Start executing node "Pexels API" {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:05.953Z | debug | Executing hook on node "Pexels API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:05.953Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:05.954Z | debug | Running node "Pexels API" started {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.014Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.020Z | debug | Running node "Pexels API" finished successfully {"node":"Pexels API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.020Z | debug | Executing hook on node "Pexels API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:06.021Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.022Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.024Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.026Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:06.026Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.027Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.028Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.029Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:06.029Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.030Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.030Z | debug | Start executing node "Serper Search" {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:06.031Z | debug | Executing hook on node "Serper Search" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:06.031Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:06.031Z | debug | Running node "Serper Search" started {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.003Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.006Z | debug | Running node "Serper Search" finished successfully {"node":"Serper Search","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.006Z | debug | Executing hook on node "Serper Search" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.007Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.007Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.008Z | debug | Start executing node "Agrupador Master Assets" {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.009Z | debug | Executing hook on node "Agrupador Master Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.009Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.009Z | debug | Running node "Agrupador Master Assets" started {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.186Z | debug | Running node "Agrupador Master Assets" finished successfully {"node":"Agrupador Master Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.187Z | debug | Executing hook on node "Agrupador Master Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.187Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.188Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.188Z | debug | Start executing node "Baixa Capa" {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.189Z | debug | Executing hook on node "Baixa Capa" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.189Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.189Z | debug | Running node "Baixa Capa" started {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.260Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.295Z | debug | Running node "Baixa Capa" finished successfully {"node":"Baixa Capa","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.295Z | debug | Executing hook on node "Baixa Capa" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.296Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.296Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.297Z | debug | Start executing node "Espera Randomica" {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.297Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.297Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.298Z | debug | Running node "Espera Randomica" started {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.299Z | debug | Setting execution status for 780 to "waiting" {"file":"workflow-execute-additional-data.js","function":"setExecutionStatus"}
2026-02-15T20:28:07.299Z | debug | Running node "Espera Randomica" finished successfully {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.300Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.306Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.308Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.309Z | debug | Workflow execution will wait until Sun Feb 15 2026 17:29:41 GMT-0300 (Brasilia Standard Time) {"workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:28:07.310Z | debug | Executing hook (hookFunctionsSave) {"executionId":"780","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.311Z | debug | Save execution data to database for execution ID 780 {"executionId":"780","workflowId":"TP_RFBFPlmwik3ug0txZJ","finished":false,"stoppedAt":"2026-02-15T20:28:07.310Z","file":"shared-hook-functions.js","function":"updateExistingExecution"}
2026-02-15T20:28:07.479Z | debug | Executing hook (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:28:07.479Z | debug | Pushed to frontend: executionWaiting {"dataType":"executionWaiting","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:28:07.480Z | debug | Execution finalized {"executionId":"780","file":"active-executions.js","function":"finalizeExecution"}
2026-02-15T20:28:53.285Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:28:53.288Z | debug | Found 1 executions. Setting timer for IDs: 780 {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:29:41.295Z | debug | Resuming execution 780 {"scopes":["waiting-executions"],"executionId":"780","file":"wait-tracker.js","function":"startExecution"}
2026-02-15T20:29:41.526Z | debug | Execution added {"executionId":"780","file":"active-executions.js","function":"add"}
2026-02-15T20:29:41.543Z | debug | Execution for workflow workflow_producao_v6_timeout was assigned id 780 {"executionId":"780","file":"workflow-runner.js","function":"runMainProcess"}
2026-02-15T20:29:41.550Z | debug | Execution ID 780 had Execution data. Running with payload. {"executionId":"780","file":"workflow-runner.js","function":"runMainProcess"}
2026-02-15T20:29:41.551Z | debug | Workflow execution started {"workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.555Z | debug | Start executing node "Espera Randomica" {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.556Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:29:41.556Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.557Z | debug | Running node "Espera Randomica" started {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.557Z | debug | Running node "Espera Randomica" finished successfully {"node":"Espera Randomica","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.559Z | debug | Executing hook on node "Espera Randomica" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:29:41.559Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.560Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.561Z | debug | Start executing node "Gera Vídeo Híbrido" {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.562Z | debug | Executing hook on node "Gera Vídeo Híbrido" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:29:41.562Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.562Z | debug | Running node "Gera Vídeo Híbrido" started {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.634Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.636Z | debug | Running node "Gera Vídeo Híbrido" finished successfully {"node":"Gera Vídeo Híbrido","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.637Z | debug | Executing hook on node "Gera Vídeo Híbrido" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:29:41.637Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.637Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.638Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:41.639Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:29:41.639Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:29:41.640Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:29:53.280Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:30:11.639Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.640Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.640Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.640Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.640Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.641Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.641Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.641Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.710Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.711Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.711Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.712Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.712Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.712Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.712Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.713Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.713Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.813Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.813Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.813Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.813Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.814Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.814Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.814Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.815Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.815Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.816Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.816Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.816Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.817Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:11.817Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:11.818Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:11.818Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:28.006Z | debug | Executing cron for workflow {"scopes":["cron"],"workflowId":"TP_RFBFPlmwik3ug0txZJ","nodeId":"b70b8012-3104-479f-a6a1-0de467f7e603","cron":"28 */10* ** *","instanceRole":"leader","file":"scheduled-task-manager.js"}
2026-02-15T20:30:28.006Z | debug | Polling trigger initiated for workflow "workflow_producao_v6_timeout" {"workflowName":"workflow_producao_v6_timeout","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"active-workflows.js","function":"executeTrigger"}
2026-02-15T20:30:41.818Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.818Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.818Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.819Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.819Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.820Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.820Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.820Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.883Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.884Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.885Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.885Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.885Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.886Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.886Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.886Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.887Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.977Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.977Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.977Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.978Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.978Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.978Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.978Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.979Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.980Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.980Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.980Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.980Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.981Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:41.981Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:30:41.981Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:30:41.982Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:30:53.275Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:31:11.979Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:11.980Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:11.980Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:11.980Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:11.981Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:11.981Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:11.981Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:11.981Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.047Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.049Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.049Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.050Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.050Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.051Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.051Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.051Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.052Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.169Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.169Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.170Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.170Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.171Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.171Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.171Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.172Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.173Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.173Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.174Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.174Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.175Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:12.175Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:12.175Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:12.176Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:13.122Z | debug | Received message from editor-UI {"pushRef":"gskldamqp0","msg":{"type":"workflowOpened","workflowId":"TP_RFBFPlmwik3ug0txZJ"},"file":"abstract.push.js","function":"onMessageReceived"}
2026-02-15T20:31:13.189Z | debug | Pushed to frontend: collaboratorsChanged {"dataType":"collaboratorsChanged","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.175Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.175Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.176Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.176Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.177Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.177Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.177Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.177Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.241Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.243Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.243Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.243Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.244Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.244Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.245Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.245Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.246Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.344Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.344Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.344Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.345Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.345Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.346Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.346Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.346Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.347Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.347Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.348Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.348Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.349Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:42.349Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:31:42.349Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:31:42.349Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:31:53.270Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:32:12.348Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.349Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.349Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.350Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.351Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.351Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.351Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.352Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.416Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.417Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.418Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.418Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.418Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.419Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.419Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.419Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.420Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.521Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.522Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.522Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.522Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.523Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.523Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.524Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.524Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.525Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.526Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.526Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.526Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.527Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:12.527Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:12.527Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:12.528Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.527Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.528Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.529Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.529Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.530Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.530Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.530Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.531Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.601Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.602Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.603Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.603Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.603Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.604Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.604Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.604Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.605Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.712Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.713Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.713Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.713Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.713Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.714Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.714Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.714Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.715Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.716Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.716Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.717Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.717Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:42.717Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:32:42.718Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:32:42.718Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:32:53.266Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:33:12.717Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.717Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.718Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.718Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.718Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.719Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.719Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.719Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.788Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.789Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.790Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.790Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.790Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.791Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.792Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.792Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.793Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.905Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.905Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.906Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.906Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.907Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.908Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.908Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.908Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.910Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.910Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.910Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.911Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.911Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:12.912Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:12.912Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:12.912Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.910Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.910Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:42.911Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.911Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.911Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.912Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:42.912Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.912Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.977Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.978Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.979Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:42.979Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.979Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.980Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:42.980Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:42.980Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:42.981Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.082Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.083Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:43.083Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.083Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.084Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.084Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:43.085Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.085Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.086Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.087Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:43.087Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.087Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.088Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:43.088Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:33:43.088Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:33:43.088Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:33:53.261Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:34:13.086Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.087Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.087Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.088Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.088Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.088Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.089Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.089Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.154Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.155Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.156Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.156Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.156Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.157Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.157Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.157Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.158Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.256Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.257Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.257Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.257Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.258Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.258Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.258Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.259Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.260Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.260Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.261Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.261Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.261Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:13.262Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:13.262Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:13.262Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.261Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.262Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.262Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.262Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.263Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.263Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.263Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.264Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.327Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.328Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.329Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.329Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.329Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.330Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.330Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.330Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.331Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.425Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.426Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.426Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.427Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.427Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.428Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.428Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.428Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.429Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.430Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.430Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.430Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.431Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:43.431Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:34:43.432Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:34:43.432Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:34:53.256Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:35:13.430Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.431Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.431Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.431Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.432Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.432Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.432Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.433Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.493Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.494Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.495Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.495Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.495Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.496Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.496Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.496Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.496Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.592Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.592Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.592Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.593Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.593Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.594Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.594Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.594Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.596Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.596Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.596Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.597Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.597Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:13.597Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:13.598Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:13.598Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.600Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.600Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.601Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.601Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.601Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.602Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.602Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.602Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.665Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.667Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.667Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.667Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.668Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.668Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.669Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.669Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.669Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.779Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.779Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.780Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.780Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.780Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.781Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.781Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.781Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.782Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.783Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.783Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.784Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.785Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:43.785Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:35:43.785Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:35:43.786Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:35:53.253Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:36:13.785Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.785Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.785Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.786Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.786Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.787Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.787Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.788Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.851Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.852Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.853Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.853Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.853Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.854Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.854Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.854Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.854Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.964Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.964Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.964Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.965Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.965Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.965Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.966Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.966Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.967Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.967Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.967Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.968Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.968Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:13.969Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:13.969Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:13.969Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:43.968Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:43.968Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:43.968Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:43.969Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:43.969Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:43.970Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:43.970Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:43.970Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.032Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.033Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.033Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.033Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.034Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.034Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.035Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.035Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.035Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.130Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.130Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.131Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.131Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.132Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.132Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.132Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.133Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.134Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.134Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.134Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.135Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.135Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:44.136Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:36:44.136Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:36:44.136Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:36:53.248Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:37:14.135Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.135Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.136Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.136Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.136Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.137Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.137Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.137Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.199Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.200Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.201Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.201Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.201Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.202Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.202Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.202Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.203Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.301Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.302Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.302Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.302Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.303Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.303Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.303Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.304Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.305Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.305Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.308Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.309Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.310Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:14.310Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:14.311Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:14.311Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.309Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.310Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.310Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.311Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.311Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.311Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.311Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.312Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.369Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.370Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.371Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.371Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.371Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.372Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.372Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.373Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.373Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.468Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.469Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.469Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.470Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.470Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.471Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.471Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.472Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.473Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.473Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.474Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.474Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.475Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:44.475Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:37:44.475Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:37:44.476Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:37:53.244Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:38:14.474Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.474Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.474Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.475Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.475Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.476Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.476Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.476Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.536Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.538Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.538Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.538Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.539Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.539Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.540Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.540Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.540Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.641Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.641Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.641Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.642Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.643Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.643Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.643Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.644Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.645Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.645Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.646Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.646Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.647Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:14.647Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:14.648Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:14.648Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.647Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.648Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.648Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.648Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.649Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.649Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.649Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.650Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.713Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.714Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.715Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.715Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.716Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.716Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.717Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.717Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.718Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.817Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.817Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.818Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.818Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.818Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.819Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.819Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.819Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.820Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.821Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.821Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.821Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.822Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:44.822Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:38:44.822Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:38:44.823Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:38:53.239Z | debug | Querying database for waiting executions {"scopes":["waiting-executions"],"file":"wait-tracker.js","function":"getWaitingExecutions"}
2026-02-15T20:39:14.821Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.821Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.821Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.822Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.822Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.823Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.823Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.823Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.880Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.881Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.881Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.881Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.881Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.882Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.882Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.882Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.883Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.977Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.977Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.978Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.978Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.978Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.979Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.979Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.979Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.980Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.981Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.981Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.981Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.982Z | debug | Start executing node "Wait for Job" {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:14.982Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:14.982Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:14.986Z | debug | Running node "Wait for Job" started {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:44.985Z | debug | Running node "Wait for Job" finished successfully {"node":"Wait for Job","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:44.986Z | debug | Executing hook on node "Wait for Job" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:44.986Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:44.986Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:44.987Z | debug | Start executing node "Check Job Status" {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:44.987Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:44.987Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:44.988Z | debug | Running node "Check Job Status" started {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.044Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.045Z | debug | Running node "Check Job Status" finished successfully {"node":"Check Job Status","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.045Z | debug | Executing hook on node "Check Job Status" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.046Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.046Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.046Z | debug | Start executing node "Increment Attempts" {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.047Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.047Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.047Z | debug | Running node "Increment Attempts" started {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.139Z | debug | Running node "Increment Attempts" finished successfully {"node":"Increment Attempts","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.140Z | debug | Executing hook on node "Increment Attempts" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.140Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.140Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.141Z | debug | Start executing node "Job Finished?" {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.141Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.141Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.141Z | debug | Running node "Job Finished?" started {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.143Z | debug | Running node "Job Finished?" finished successfully {"node":"Job Finished?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.143Z | debug | Executing hook on node "Job Finished?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.143Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.144Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.144Z | debug | Start executing node "Is Timeout?" {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.145Z | debug | Executing hook on node "Is Timeout?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.145Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.145Z | debug | Running node "Is Timeout?" started {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.146Z | debug | Running node "Is Timeout?" finished successfully {"node":"Is Timeout?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.146Z | debug | Executing hook on node "Is Timeout?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.147Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.147Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.148Z | debug | Start executing node "Job Succeeded?" {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.149Z | debug | Executing hook on node "Job Succeeded?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.149Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.150Z | debug | Running node "Job Succeeded?" started {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.151Z | debug | Running node "Job Succeeded?" finished successfully {"node":"Job Succeeded?","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.152Z | debug | Executing hook on node "Job Succeeded?" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.152Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.152Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.153Z | debug | Start executing node "Mark Job Failed" {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.153Z | debug | Executing hook on node "Mark Job Failed" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.153Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.153Z | debug | Running node "Mark Job Failed" started {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.214Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.216Z | debug | Running node "Mark Job Failed" finished successfully {"node":"Mark Job Failed","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.216Z | debug | Executing hook on node "Mark Job Failed" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.216Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.217Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.217Z | debug | Start executing node "Pixabay API" {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.217Z | debug | Executing hook on node "Pixabay API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.218Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.218Z | debug | Running node "Pixabay API" started {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.616Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.619Z | debug | Running node "Pixabay API" finished successfully {"node":"Pixabay API","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.620Z | debug | Executing hook on node "Pixabay API" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.620Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.620Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.621Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.621Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.621Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.622Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.622Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.623Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.623Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.623Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.624Z | debug | Start executing node "Serper.dev (Images)" {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:45.625Z | debug | Executing hook on node "Serper.dev (Images)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:45.626Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:45.626Z | debug | Running node "Serper.dev (Images)" started {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.623Z | debug | Pushed to frontend: sendConsoleMessage {"dataType":"sendConsoleMessage","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.625Z | debug | Running node "Serper.dev (Images)" finished successfully {"node":"Serper.dev (Images)","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.626Z | debug | Executing hook on node "Serper.dev (Images)" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:46.626Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.626Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.628Z | debug | Start executing node "Merge Assets" {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.628Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:46.628Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.629Z | debug | Running node "Merge Assets" started {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.629Z | debug | Running node "Merge Assets" finished successfully {"node":"Merge Assets","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.630Z | debug | Executing hook on node "Merge Assets" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:46.631Z | debug | Pushed to frontend: nodeExecuteAfter {"dataType":"nodeExecuteAfter","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.631Z | debug | Pushed to frontend: nodeExecuteAfterData {"dataType":"nodeExecuteAfterData","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.631Z | debug | Start executing node "SearXNG" {"node":"SearXNG","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
2026-02-15T20:39:46.632Z | debug | Executing hook on node "SearXNG" (hookFunctionsPush) {"executionId":"780","pushRef":"gskldamqp0","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"execution-lifecycle-hooks.js"}
2026-02-15T20:39:46.632Z | debug | Pushed to frontend: nodeExecuteBefore {"dataType":"nodeExecuteBefore","pushRefs":"gskldamqp0","file":"abstract.push.js","function":"sendTo"}
2026-02-15T20:39:46.633Z | debug | Running node "SearXNG" started {"node":"SearXNG","workflowId":"TP_RFBFPlmwik3ug0txZJ","file":"logger-proxy.js","function":"exports.debug"}
