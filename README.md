# NaoMod -- Nantes Software Modeling Group 
## Dynamic Models for Continuous Software Construction


The main goal of the NaoMod team is to provide techniques and tools to leverage dynamic models for continuous software construction. 
We envision software development, integration, validation, deployment, and management as a continuous process, where models are  first-class artifacts.


## Team members

- Gerson Sunyé (Head). Associate Professor HDR, University of Nantes.
- Hugo Brunelière. Research Engineer, IMT Atlantique.
- Jean-Marie Mottu. Associate Professor, University of Nantes.
- Jean-Claude Royer. Professor, IMT Atlantique.
- Dalila Tamzalit. Associate Professor, University of Nantes.
- Massimo Tisi. Associate Professor, IMT Atlantique.


## Scientific Context

Gartner, Inc. forecasts that [8.4 billion connected things will be in use worldwide in 2017](http://www.gartner.com/newsroom/id/3598917), up 31 percent from 2016, and will reach 20.4 billion by 2020. 
This forecast agrees with previous CISCO's predictions that in 2020, there will be more than 50 billions of connected devices exchanging more than 1 zettabyte/year of data [evans:2011].

This growth emphasizes the need for interoperable software integrating companies, Cyber-Physical Systems (CPS), Internet of Things (IoT) devices, and humans,
with real-time capabilities for collecting and analyzing data at runtime. 
Along with this growth, new application domains arise. This is the case for instance of the Industry 4.0 which integrates the Industrial Internet of Things, Cyber-Physical Systems and Cloud Computing.
In this application domain, data obtained during the operation of complex systems can be used to improve the original software (and so the whole system), emphasizing the need for a bigger integration between software development and operation.
Moreover, the Industry 4.0 also introduces the notion of _digital twin_: a software model continuously updated with the data obtained from a physical entity (devices, robots, worker, etc.).

The advent of new connected devices, such as sensors, actuators, engines, machines, and components, which produce large amounts of data, raises a new  software engineering challenge: how to gather and analyze data created at runtime to continuously improve the design of modular, reusable, scalable, and interoperable software?

We believe that there is no silver bullet [Brooks:1987]: there will be no complete revolution in the way practitioners develop software, mostly because they usually like to rely on existing, well-oiled, reliable development tools.
Thus, existing software development techniques, tools, and methods must be adapted and improved (when necessary) to meet new and future requirements.
We also strongly believe that model-based engineering [Schmidt:2006] (MDE) is a well-suited approach to support the needed improvements.

Related model-based techniques and tools must evolve to support continuous design along with continuous quality assurance. 
Software operational data should be collected and analyzed at runtime, 
and used to improve software design in a continuous integration delivery pipeline [Loukides:2012]. 
Software quality must be verified continuously as well and during operation, similarly to the Netflix's Simian Army [Tseitlin:2013].
Indeed, reproducing real-world conditions for large-scale software deployed on millions of nodes, such as Microsoft's Skype, is unrealizable. 

## Application Context

The growth of interconnected devices relies mostly on three families of devices: cyber-physical systems, smartphones and IoT sensors and actuators. While until now these families are considered as different platforms, there are important unification efforts and we believe that development tools and techniques for these platforms will converge in the next years.

These new families of devices and their intrinsic interconnection capabilities allow new application contexts, such as smart factories and smart health.
In the following sections, we present two application contexts to which our research can be applied.

### Cyber-Physical Systems

The current revolution of the manufacturing industry is driven by the recent research in Cyber-Physical System, defined as 

> "a set of heterogeneous physical units (e.g., sensors, control modules) communicating via heterogeneous networks (using networking equipment) and potentially interacting with applications deployed on Cloud infrastructures and/or humans to achieve a common goal."

To be used in the manufacturing industry, a CPS need to be able to face unexpected changes in the environment (e.g., increases in temperature), in the system state (e.g., component failures), and in objectives (e.g., demand for faster response). 
Moreover, since CPS data are now communicated to help computation, they need to be modeled with data structures, typed, delimited, and finally interpretable.
Software Engineering should help manage _scientific computations_ (based on physical or mechanical formulas, business processes for instance) processing data produced by multiple heterogeneous devices. 


### Internet of Things

The Internet of Things (IoT) is redefining the way Internet extends its coverage of the cyber world by including physical world and its objects.
It has applications and implications on a wide range of domains such as industrial processes, homes, cities, wearables, medical devices, etc.
In order to reach large deployment scale and unlock its full potential, software engineering of IoT should consider how to exchange data and orders considering heterogeneous devices (both on material architecture and on software environments) in _large open system network_.
That raises issues and challenges such as _continuously changing networks_, _interactions between unknown participants_, _time-delayed communication_, _management of many heterogeneous devices and their software_.

## Scientific Challenges
The use of models has increase with Model-Driven Engineering, they are no more only descriptive (such as originally with UML for instance), they are first class assets, manipulated, transformed, interpreted to create softwares.
Nevertheless, their are still too much prescriptive and even using reverse engineering, the model is still not used plainly to help software development at any step.
Considering the introduced scientific context, it is necessary to MDE and its model into an agile process.
Therefore, we should consider several major challenges to enforce the place of the models in the software development considering both the development and the V&V:

- How to update and exploit models during Continuous Software Construction?
- How to use the data streams from CPS/IoT devices to update the models?
- How to increase to control dynamically the models are accurate?

We decline these challenges in several parts of the NaoMod project.

### Continuous Software Construction

Complex systems, and more particularly CPS, are becoming more and more software intensive.
This calls for existing software engineering practices to target new advances in applicability, productivity and quality.
MDE and related modeling techniques have already proved to bring significant gains in various contexts [Whittle2014].
However, they still need to be further developed and enhanced in order to scale up for large and complex industrial projects.
Indeed, one of the major challenges in the model-based engineering of such critical (software) systems is the better integration between the design and runtime aspects [derler2012modeling].
The actual system behavior at runtime has to be frequently matched with its current design in order to fully understand critical situations, as well as eventual failures in design or related deviations from requirements.
Many methods and tools exist for tracing the execution and performing measurements of system runtime properties.
Nevertheless, these solutions do not currently allow the integration with system models - the most suitable level for system engineers to perform their analysis and make decisions.
Thus, achieving a continuous engineering cycle and feedback loop between design and runtime (models) would allow improving the quality of the running system as a whole. 

The NaoMod team advocates for the use of modeling principles and techniques in order to realize such a continuous engineering process.
This will require the definition of relevant model-based architecture(s) as well as the corresponding chaining of various kinds of models and operations on/between them.
Thus, improvements in the state-of-the-art will have to be made related to model management, model federation, interoperability and/or traceability (notably via model view techniques [bruneliere2015emf,bruneliere2017survey]), runtime modeling or model verification and validation for instance.   

### Holistic Models

On the pure software side, Model-Driven Engineering has fostered in the last decade the uniform treatment of all software engineering artifacts as models and has proven to greatly help the understanding, development, and maintenance of complex systems. 
Due to the direct interaction with the "physical world", software development for CPS often requires considering aspects such as physical (e.g., electrical) properties and the geometry/movement of components, which is typically not a concern in the engineering of pure software systems. 

We plan to build a _holistic model of the software execution_, that would integrate execution traces considering the software (e.g., program state, execution environment, network use, data access) and the physical (e.g., energy consumption, electrical measures for sensors and actuators, geometry of the scene) parts of the system; to apply model-based techniques (e.g., model transformation, model query, structural pattern detection, graph analysis) for the monitoring and optimization of CPS systems. 

Such approach would enable cross-domain analysis correlating the software and physical parts of execution traces. For instance it would be possible to detect the program substructures associated with high power consumption in the physical world, identify possible alternatives and abstract them into domain-specific energy consumption anti-patterns. Model transformation may be then used to remove these anti-patterns. 

Moreover, specialization of CPS/IoT requires to discover and optimize constraints on the data to adapt to specific usage scenarios (e.g. localisation data and associated moves should be differently considered on a sport field or inside a factory). 
We need to verify properties such a time synchronization between live data streams from multiple devices. Due to uncertainty in the environment, measurements from devices are suffering for data quality issues, such as completeness, timeliness and correctness. Therefore, design space exploration of constraints, to ensure well-formedness of live data streams is of paramount importance. Those constraints complete the model of the data in a _holistic model of the software data_.
It would help reduce risk of error due to processing data of low quality outside the perceived operational limits of CPS/IoT.


### Dynamic Software Validation and Verification

Users of MDE tools assume that V&V results on the model will also apply to the generated code. For instance when a test passes on the model, the user expects that test to pass on the generated code too. However, the Industry 4.0 domain raises particularly critical concerns on possible threats to information privacy and interoperability. While such properties can be verified on software models, we need a more systematic approach to give high-confidence that they will be also exhibited by the generated code. The NaoMod team created and maintains a model transformation language, ATL, dedicated to the analysis and processing of models. Several V&V techniques have been recently developed to certify the correctness of ATL transformations [Cheng:2017,Mottu:2015]. We will conceive and develop V&V techniques for model transformations to produce certified components that will monitor at runtime that the behavior of the system respects the properties verified on the model. Examples of such properties are access control on sensitive data, security of communication protocols, data synchronization, correct interoperability and scalability. 

CPSs need to maintain at runtime an up-to-date model of the cyber and physical parts. To guarantee that the updates of this model are always correctly performed, we propose a novel formal verification approach. In practice, the user encodes the possible updates as streaming model transformations, i.e. declarative update rules responding to a stream of incoming events. These streaming transformations are translated into a formal verification framework, together with contracts on the dynamic behavior (e.g. guaranteeing to avoid buffer overflows or frame skipping). We will investigate the automatic verification of such contracts on Satisfiability-Modulo Theory (SMT) and their interactive verification by the theorem prover Coq. The research will build on top of recent results in the model-driven engineering community on a co-inductive representation of models for model-transformation verification. We will investigate how to encode the stream of complex events as an infinite typed graph. The contract language will be extended to support stream-specific constraints. In both interactive and automatic cases, extensions of the existing verification tool VeriATL will be produced. 

In contract-based MDE, deductive verification at each model update may help the system developer in early bug detection. However, because of the execution performance of current verification systems, re-verifying from scratch after a change has been made would introduce impractical delays. We will address this problem by proposing an incremental verification approach for MDE. Our approach is based on decomposing each contract into sub-goals, and caching the sub-goal verification results. We already successfully applied this idea to the verification of model transformations. We exploit the relational semantics to determine whether a cached verification result may be impacted by a change. Consequently, less postconditions/sub-goals need to be re-verified. When a change forces the re-verification of a postcondition, we use the cached verification results of sub-goals to construct a simplified version of the postcondition to verify. We plan to extend this idea to the verification of several modeling languages in MDE.

To enable the transition to Industry 4.0, we must ensure users of software solutions that we offer them a quality, which needs as much reliable development methods as verification by testing. 
A bug in the software chain leads to significant turnover losses, site blocking risk, or purchase reports to the competition. [Upgrade bugs are a large part of the problems(http://www.usinenouvelle.com/article/stallergenes-paralyse-par-un-probleme-informatique-en-france.N367862) with medical consequence and a loss of 60M€ in 2016 for Stallergenes).
Software is constantly changing, either during design (Agile, DevOps) or throughout the lifecycle [mirzaaghaei:2012], by successive improvements (new features, non-functional optimizations) or changes in the ecosystem [Mens: 2008] (when dependencies or deployment environment evolve). Performing this modernization is a continuous work for development and support teams. 
Besides the impact of continuous modernization on software, we must also consider continuously its effect on software validation [Zeller:2015].

### Model Management Infrastructure


Continuous software construction requires two kinds of models: development and operational models. While the first ones are typically small, created by humans to prescribe how software must be executed, the second ones are large, automatically created at runtime and describe the behavior of a system during execution.

However, current MDE tools are not fully adapted for both kinds of models.
Indeed, most tools are stand alone, non-concurrent and tailored for small-scale models. For instance, the Eclipse Modeling Framework, which is the _de facto_ standard framework for creating modeling tools, is unadapted for large models and does not support concurrent access [Benelallam:2014]. 

Thus, there is a need for new modeling infrastructures that fully support both, development and operational models.
In the one side, there is a need for distributed and scalable modeling tools that are able to manage models that are continuously updated from different sources.
In the other side, there is a need for distributed, versioned and persistent modeling tools, that allow users to analyze large models and to create development collaboratively.

