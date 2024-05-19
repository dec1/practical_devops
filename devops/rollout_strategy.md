- **Rolling**:
    Gradually replaces instances (or small batches thereof) of the old version with the new one, **individually**, ensuring continuous availability. Each instance is taken out of service, updated, and then reintroduced into the infrastructure. The process repeats until all instances are updated.
    #####

- **Canary**:
    A small **subset of users or servers** (the "canaries") initially receives the new version. If it performs well without issues, the rollout extends to a larger audience, eventually encompassing the entire user base or infrastructure.
    #####

- **Blue-Green**:
    2 environments (Blue and Green) are maintained, with only **one active**ly serving production traffic at any time.
    The inactive one undergoes updates, testing, and preparation for the next release. Once ready, the traffic is switched to the updated environment.
    #####

- **Shadow** :
    New version of the application is deployed alongside the existing version. Real production traffic is **duplicated** as **input** to the new version without affecting user experience (who only receive responses from existing version). This allows for monitoring and testing in a real-world scenario without user impact.
    #####

- **A/B (Split)** Testing:
    Testing **multiple** versions of an application each to a different group of users to **compare** their performance and user satisfaction.
    #####

- **Feature Flags** (Toggles):
    Deploying new features with the ability to **toggle** them at **runtime** _without_ redeploying the application.

