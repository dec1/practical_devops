### Keycloak

- #### Realm
    A realm in Keycloak is a high-level concept that defines a space where users, applications, and roles exist and are managed. Each realm is isolated from others, meaning users and configurations in one realm are invisible and inaccessible to others. This isolation allows multiple organizations or applications to be managed within the same Keycloak instance without interference.

    #####
    - **Use Case**: A company might have separate realms for different business units or environments (e.g., development, staging, production).

- #### Users

- #### Role
    A role in Keycloak represents a set of permissions or a position within an organization. Roles can be assigned to users, and users can have multiple roles. There are two types of roles:

    ### 
    - **Realm Roles**: These are roles that are available throughout the entire realm and can be assigned to any user or client in the realm.
    - **Client Roles**: These are roles specific to a particular client (application) within the realm and can only be assigned to users who have access to that client.
    
    ####
    - **Use Case**: A user in the realm might have a role like `admin` that gives them administrative privileges across the entire realm or a client-specific role like `editor` for a particular application.

- #### Applications (Clients)
    In the context of Keycloak, an application is referred to as a client. A client in Keycloak represents an application or a service that requires authentication and authorization. Clients can be web applications, mobile applications, or any service that interacts with Keycloak for user authentication.

    - **Example**: If you have a web application called `myapp` and a mobile application called `mobileapp`, both would be registered as clients in Keycloak.

    ####
    - Resource access is primarily used in ABAC but can be part of RBAC when client-specific roles are involved.

- #### Claims
    In the context of Keycloak and JWT tokens, **claims** are pieces of information asserted about a user. These claims can include user attributes, roles, and permissions, and they are embedded within the token issued by Keycloak. Claims provide the necessary information for access control decisions within an application.

    ####
    - **Users**: Claims may include user-specific information such as the username or email, and (for ABAC) the resources they have access to.

    - **Roles**: Claims often include the roles assigned to the user, both realm roles and client-specific roles.

    - **Resource Access**: A type of claim that specifies the roles a user has for specific clients (applications) within the realm. This details what the user is allowed to do within those clients. `resource_access` claims are an extension of roles and do not contradict them but rather specify client-specific permissions.

    #####
    - **Use Case**: An application can check the `resource_access` part of the token to determine what the user is allowed to do within the application. For instance, if the user has an `editor` role for the `myapp` client, the application can grant access to editing features.

        - ##### Handling Conflicting Claims
            In cases where a user has conflicting claims, such as a broad `admin` role and restrictive `resource_access` claims, the application must decide how to interpret these claims. Generally, the application should follow a principle of least privilege, where the more restrictive claim takes precedence to ensure security. Alternatively, the application can implement custom logic to resolve these conflicts based on the specific requirements of the system.

            #####
            - **Example**: If a user has an `admin` realm role but restrictive `resource_access` for a specific client, the application might choose to enforce the more restrictive `resource_access` permissions within that client while allowing broader permissions elsewhere.


---

An example 

- #### Realm 
    - my_company

- #### Users
    - Alice
    - Bob

- #### Roles:

    - **Realm Roles**: 
        - **admin**, **user** (available globally within the realm).
    - **Client Roles**: 
        - myapp:  
            - **editor**
            - **viewer**
        - mobileapp: 
            - **mobile-user**.




- #### Clients (Applications):

    - **myapp**: - A web application.
    - **mobileapp**: A mobile application.


- #### Claims:

    - **Alice** has:
        - admin realm role.
        - editor client role for myapp.
        - mobile-user client role for mobileapp.
        - **Token**
            ```yaml
            {
                "resource_access": {
                    "myapp": {
                        "roles": ["editor"]
                    },
                    "mobileapp": {
                        "roles": ["mobile-user"]
                    }
                },
                "realm_access": {
                    "roles": ["admin"]
                }
            }
            ```

    - **Bob** has:
        - user realm role.
        - viewer client role for myapp.
        - **Token**
            ```yaml
            {
                "resource_access": {
                    "myapp": {
                        "roles": ["viewer"]
                    }
                },
                "realm_access": {
                    "roles": ["user"]
                }
            }
            ```