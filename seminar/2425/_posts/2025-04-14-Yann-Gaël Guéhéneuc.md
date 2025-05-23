---
layout : null
title : "GLASS, a Framework for Refactorings using FCA"
speaker : "Yann-Gaël Guéhéneuc"
start : "1330"
end : "1400"
---
Yann-Gaël Guéhéneuc is a visiting researcher from Concordia University.

_Collaborators_: Luca Scistri, Imen Benzarti, Petko Valtchev, Yann-Gaël Guéhéneuc, Ghizlane El Boussaidi, Hafedh Mili

[Slides](seminar/2425/material/yann-gael-GLASS-2025.pdf)

_Summary_: Many works have studied the design of object-oriented programs and quality practices. They have reported a conflict between the desired design and practices and the capabilities of programming languages. Indeed, many programming languages only offer single inheritance, while many designs naturally require multiple inheritance. Also, many programming languages mix reusing and typing, making it difficult to avoid code duplication in class hierarchies.
Without aspect-oriented techniques to develop and compose features, developers resort to object-oriented design and programming idioms to separate features as well as possible. Given a legacy OO system, discovering existing functional features helps understand the design of the system and extract these features to ease their maintenance and reuse. We want to discover candidate functional features in OO systems. We first define functional features and then discuss the footprints that such features are likely to leave in an OO system. We identify three such footprints: (1) multiple inheritance, (2) delegation, and (3) ad-hoc. We develop and implement a set of algorithms for identifying such footprints in Java.
Once having discovered these features, we want to refactor some ad hoc features to minimise code duplication by redesigning the class hierarchies. In this work in progress, we propose to redesign class hierarchies by pulling up methods, replacing inheritance with delegation, and introducing a systematic and consistent type hierarchy (i.e., interposing interfaces between client code and the class hierarchies). We first illustrate our intuition using various real-world examples and then propose an approach that selects certain ad hoc features, which should be refactored according to some criteria, and then suggests refactoring opportunities to transform these ad hoc features into deliberate features. This approach thus reduces code duplication while maintaining the type hierarchy.
We apply our approach to several case studies to illustrate its benefits, but also limitations. Real-world examples include JavaWebMail, JHotDraw, and PADL.