
    @Rule(Fact(query_topic='definition_of_a_mixture'))
    def rule_definition_of_a_mixture(self):
        """A mixture is a form of matter that contains two or more different substances (elements or compounds) that are physically combined but not chemically bonded, meaning each substance retains its individual chemical properties."""
        self.response = {
            'concept': 'Definition of a Mixture',
            'explanation': """A mixture is a form of matter that contains two or more different substances (elements or compounds) that are physically combined but not chemically bonded, meaning each substance retains its individual chemical properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures, Classification of Matter',
            'examples': ["If some matter contains two or more substances, such matter is referred to as mixtures.", "Mixtures are formed by physically combining two or more pure substances.", "Air, soil, and sea water are examples of mixtures."]
        }
        self.halt()

    @Rule(Fact(query_topic='air_composition_as_a_mixture'))
    def rule_air_composition_as_a_mixture(self):
        """The air around us is a prime example of a mixture, specifically a mixture of several gases like nitrogen, oxygen, argon, carbon dioxide, and water vapor, along with varying amounts of small solid particles such as dust."""
        self.response = {
            'concept': 'Air Composition as a Mixture',
            'explanation': """The air around us is a prime example of a mixture, specifically a mixture of several gases like nitrogen, oxygen, argon, carbon dioxide, and water vapor, along with varying amounts of small solid particles such as dust.""",
            'topic': 'Chemistry',
            'subtopic': 'Atmospheric Chemistry, Mixtures',
            'examples': ["Air is composed of gases like nitrogen, oxygen, argon, carbon dioxide, water vapour, and very small particles such as dust.", "You may understand that air is a mixture of several substances.", "Nitrogen and oxygen are major components of the air mixture."]
        }
        self.halt()

    @Rule(Fact(query_topic='distinction_between_mixtures_and_pure_substances'))
    def rule_distinction_between_mixtures_and_pure_substances(self):
        """Elements and compounds are classified as pure substances, meaning they have a fixed chemical composition. In contrast, mixtures are not pure substances because their composition can vary, and their components retain their individual properties."""
        self.response = {
            'concept': 'Distinction between Mixtures and Pure Substances',
            'explanation': """Elements and compounds are classified as pure substances, meaning they have a fixed chemical composition. In contrast, mixtures are not pure substances because their composition can vary, and their components retain their individual properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Matter, Mixtures',
            'examples': ["Elements and compounds are pure substances.", "Mixtures are not pure substances.", "Pure substances have a definite composition, unlike mixtures."]
        }
        self.halt()

    @Rule(Fact(query_topic='prevalence_of_mixtures_in_nature_and_everyday_life'))
    def rule_prevalence_of_mixtures_in_nature_and_everyday_life(self):
        """Mixtures are highly prevalent in both the natural environment and in many manufactured or consumed items in daily life, indicating that pure substances are less common in their isolated form in nature."""
        self.response = {
            'concept': 'Prevalence of Mixtures in Nature and Everyday Life',
            'explanation': """Mixtures are highly prevalent in both the natural environment and in many manufactured or consumed items in daily life, indicating that pure substances are less common in their isolated form in nature.""",
            'topic': 'Chemistry',
            'subtopic': 'Everyday Chemistry, Mixtures',
            'examples': ["Natural environment mostly contains mixtures, not pure substances.", "Air, soil, sea water, river water and rocks around us are examples.", "Cool drinks, fruit drinks, tea, coffee, ice cream, yoghurt and fruit salad are also mixtures."]
        }
        self.halt()

    @Rule(Fact(query_topic='mixture'))
    def rule_mixture(self):
        """A blend of two or more pure substances that are not chemically combined, forming matter whose components can be separated by physical methods."""
        self.response = {
            'concept': 'Mixture',
            'explanation': """A blend of two or more pure substances that are not chemically combined, forming matter whose components can be separated by physical methods.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["A mixture of copper sulphate and naphthalene", "Air (a mixture of gases)", "Saltwater"]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_a_mixture'))
    def rule_components_of_a_mixture(self):
        """The individual pure substances that come together to form a mixture."""
        self.response = {
            'concept': 'Components of a Mixture',
            'explanation': """The individual pure substances that come together to form a mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["Copper sulphate in a copper sulphate-naphthalene mixture", "Naphthalene in a copper sulphate-naphthalene mixture", "Oxygen and nitrogen in air"]
        }
        self.halt()

    @Rule(Fact(query_topic='chemical_nature_of_components_in_a_mixture'))
    def rule_chemical_nature_of_components_in_a_mixture(self):
        """Even when substances are mixed to form a mixture, their individual chemical nature and identity remain unchanged within the mixture."""
        self.response = {
            'concept': 'Chemical Nature of Components in a Mixture',
            'explanation': """Even when substances are mixed to form a mixture, their individual chemical nature and identity remain unchanged within the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Mixtures',
            'examples': ["Copper sulphate remains a blue, water-soluble substance in its mixture with naphthalene", "Naphthalene remains a white, water-insoluble substance in its mixture with copper sulphate", "Salt retains its taste and solubility when mixed with water"]
        }
        self.halt()

    @Rule(Fact(query_topic='separation_of_mixture_components'))
    def rule_separation_of_mixture_components(self):
        """The individual components of a mixture can be separated from each other using various physical methods."""
        self.response = {
            'concept': 'Separation of Mixture Components',
            'explanation': """The individual components of a mixture can be separated from each other using various physical methods.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Mixtures',
            'examples': ["Filtering naphthalene powder from a copper sulphate solution", "Evaporation to separate salt from saltwater", "Using a magnet to separate iron filings from sand"]
        }
        self.halt()

    @Rule(Fact(query_topic='importance_of_thorough_mixing_for_uniformity_in_mixtures'))
    def rule_importance_of_thorough_mixing_for_uniformity_in_mixtures(self):
        """For a mixture to exhibit consistent properties throughout, its components must be mixed thoroughly. Inadequate mixing leads to non-uniform distribution of components, resulting in varying properties in different parts of the mixture, affecting taste, color, or other functional attributes."""
        self.response = {
            'concept': 'Importance of Thorough Mixing for Uniformity in Mixtures',
            'explanation': """For a mixture to exhibit consistent properties throughout, its components must be mixed thoroughly. Inadequate mixing leads to non-uniform distribution of components, resulting in varying properties in different parts of the mixture, affecting taste, color, or other functional attributes.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Mixtures',
            'examples': ["When making colors by mixing paints, application will not give a uniform color unless they are mixed well.", "If the components used to make cake are not mixed well, different parts of the cake taste differently, and rising will be inconsistent.", "The medicinal property of tablets, capsules, or liquid mixtures will not be even if the components are not mixed well during production."]
        }
        self.halt()

    @Rule(Fact(query_topic='investigating_component_distribution_in_mixtures'))
    def rule_investigating_component_distribution_in_mixtures(self):
        """The distribution of components in a mixture can be studied experimentally to determine its uniformity. This involves observing visual characteristics like color and clearness, and comparing residual matter obtained from different parts of the mixture after vaporization."""
        self.response = {
            'concept': 'Investigating Component Distribution in Mixtures',
            'explanation': """The distribution of components in a mixture can be studied experimentally to determine its uniformity. This involves observing visual characteristics like color and clearness, and comparing residual matter obtained from different parts of the mixture after vaporization.""",
            'topic': 'Chemistry',
            'subtopic': 'Experimental Study of Mixtures',
            'examples': ["In a water-clay mixture, observe if the muddy color is uniformly distributed throughout the solution and if the clearness is similar from top to bottom after standing.", "Take identical drops from two different places (A and B) of a solution, vaporize them on a metal plate, and check which sample contains more residual matter to assess distribution uniformity."]
        }
        self.halt()

    @Rule(Fact(query_topic='non_uniform_mixture_characteristics'))
    def rule_non_uniform_mixture_characteristics(self):
        """In a mixture where components are not uniformly distributed, properties such as color and transparency can vary from one part of the mixture to another. The concentration of particles of one component can also differ in different unit volumes within the mixture."""
        self.response = {
            'concept': 'Non-uniform Mixture Characteristics',
            'explanation': """In a mixture where components are not uniformly distributed, properties such as color and transparency can vary from one part of the mixture to another. The concentration of particles of one component can also differ in different unit volumes within the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["The color/transparency varies from place to place in a clay-water mixture.", "The amount of clay particles per unit volume differs from place to place.", "Residual matter (like clay) settles unevenly in water."]
        }
        self.halt()

    @Rule(Fact(query_topic='uniform_mixture_characteristics'))
    def rule_uniform_mixture_characteristics(self):
        """In a mixture where components are uniformly distributed, properties such as transparency are consistent throughout the solution. The concentration of particles of a dissolved component in a unit volume is equal throughout the mixture."""
        self.response = {
            'concept': 'Uniform Mixture Characteristics',
            'explanation': """In a mixture where components are uniformly distributed, properties such as transparency are consistent throughout the solution. The concentration of particles of a dissolved component in a unit volume is equal throughout the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["The transparency is equal throughout a salt-water solution.", "The amount of salt particles in a unit volume is equal throughout a salt-water solution.", "Properties like clearness are uniform from top to bottom in a salt solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='mixture_classification_by_component_distribution'))
    def rule_mixture_classification_by_component_distribution(self):
        """Mixtures can be categorized into two main types based on how their components are distributed: those where the composition is uniform throughout, and those where the composition is not uniform throughout."""
        self.response = {
            'concept': 'Mixture Classification by Component Distribution',
            'explanation': """Mixtures can be categorized into two main types based on how their components are distributed: those where the composition is uniform throughout, and those where the composition is not uniform throughout.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Mixtures with uniform component composition (e.g., salt in water).", "Mixtures with non-uniform component composition (e.g., clay in water).", "Dividing mixtures based on how evenly substances are spread."]
        }
        self.halt()

    @Rule(Fact(query_topic='heterogeneous_mixture'))
    def rule_heterogeneous_mixture(self):
        """A heterogeneous mixture is one in which the components are visibly separated from one another, and their composition is not uniformly distributed throughout the mixture."""
        self.response = {
            'concept': 'Heterogeneous Mixture',
            'explanation': """A heterogeneous mixture is one in which the components are visibly separated from one another, and their composition is not uniformly distributed throughout the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Mixture prepared by dissolving clay in water.", "Components are separated from one another in a heterogeneous mixture.", "Composition is not uniform throughout the mixture."]
        }
        self.halt()

    @Rule(Fact(query_topic='homogeneous_mixture'))
    def rule_homogeneous_mixture(self):
        """A homogeneous mixture is one in which the components cannot be observed separately from one another. The properties and composition, such as color and transparency, are uniform and similar throughout the entire mixture."""
        self.response = {
            'concept': 'Homogeneous Mixture',
            'explanation': """A homogeneous mixture is one in which the components cannot be observed separately from one another. The properties and composition, such as color and transparency, are uniform and similar throughout the entire mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Mixture prepared by dissolving common salt in water.", "Components cannot be observed separately from one another in a homogeneous mixture.", "Physical properties like color and transparency are similar throughout a homogeneous mixture."]
        }
        self.halt()

    @Rule(Fact(query_topic='homogeneous_mixtures__solutions_'))
    def rule_homogeneous_mixtures__solutions_(self):
        """Mixtures in which physical properties such as colour, transparency, and density are identical everywhere. They are also known as solutions."""
        self.response = {
            'concept': 'Homogeneous mixtures (Solutions)',
            'explanation': """Mixtures in which physical properties such as colour, transparency, and density are identical everywhere. They are also known as solutions.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["salt solution", "sugar solution"]
        }
        self.halt()

    @Rule(Fact(query_topic='heterogeneous_mixtures'))
    def rule_heterogeneous_mixtures(self):
        """Mixtures in which the components can be distinguished from one another. The physical properties of the mixture such as colour, transparency and density are different from place to place."""
        self.response = {
            'concept': 'Heterogeneous mixtures',
            'explanation': """Mixtures in which the components can be distinguished from one another. The physical properties of the mixture such as colour, transparency and density are different from place to place.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Water in which clay is dissolved", "cement mortar", "fruit salad"]
        }
        self.halt()

    @Rule(Fact(query_topic='solid_liquid_heterogeneous_mixture'))
    def rule_solid_liquid_heterogeneous_mixture(self):
        """A mixture composed of a solid and a liquid that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place."""
        self.response = {
            'concept': 'Solid-liquid heterogeneous mixture',
            'explanation': """A mixture composed of a solid and a liquid that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Wheat flour in water", "Clay in water", "Washing powder in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='solid_liquid_homogeneous_mixture'))
    def rule_solid_liquid_homogeneous_mixture(self):
        """A mixture composed of a solid and a liquid that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere."""
        self.response = {
            'concept': 'Solid-liquid homogeneous mixture',
            'explanation': """A mixture composed of a solid and a liquid that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Salt in water", "Copper sulphate in water", "Potassium permanganate in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='liquid_liquid_heterogeneous_mixture'))
    def rule_liquid_liquid_heterogeneous_mixture(self):
        """A mixture composed of two liquids that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place."""
        self.response = {
            'concept': 'Liquid-liquid heterogeneous mixture',
            'explanation': """A mixture composed of two liquids that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Coconut oil in water", "Sherbet drinks"]
        }
        self.halt()

    @Rule(Fact(query_topic='liquid_liquid_homogeneous_mixture'))
    def rule_liquid_liquid_homogeneous_mixture(self):
        """A mixture composed of two liquids that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere."""
        self.response = {
            'concept': 'Liquid-liquid homogeneous mixture',
            'explanation': """A mixture composed of two liquids that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Ethyl alcohol in water", "Water mixed with ethyl alcohol"]
        }
        self.halt()

    @Rule(Fact(query_topic='solid_solid_heterogeneous_mixture'))
    def rule_solid_solid_heterogeneous_mixture(self):
        """A mixture composed of two solids that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place."""
        self.response = {
            'concept': 'Solid-solid heterogeneous mixture',
            'explanation': """A mixture composed of two solids that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Sugar and Salt mixture", "Fruit salad"]
        }
        self.halt()

    @Rule(Fact(query_topic='solid_solid_homogeneous_mixture'))
    def rule_solid_solid_homogeneous_mixture(self):
        """A mixture composed of two solids that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere."""
        self.response = {
            'concept': 'Solid-solid homogeneous mixture',
            'explanation': """A mixture composed of two solids that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Copper and Zinc alloy", "Brass (alloy of copper and zinc)"]
        }
        self.halt()

    @Rule(Fact(query_topic='gas_liquid_heterogeneous_mixture'))
    def rule_gas_liquid_heterogeneous_mixture(self):
        """A mixture composed of a gas and a liquid that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place."""
        self.response = {
            'concept': 'Gas-liquid heterogeneous mixture',
            'explanation': """A mixture composed of a gas and a liquid that is heterogeneous, meaning its components can be distinguished and its physical properties vary from place to place.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Carbon dioxide in hot water", "Bubbling CO2 through hot water"]
        }
        self.halt()

    @Rule(Fact(query_topic='gas_liquid_homogeneous_mixture'))
    def rule_gas_liquid_homogeneous_mixture(self):
        """A mixture composed of a gas and a liquid that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere."""
        self.response = {
            'concept': 'Gas-liquid homogeneous mixture',
            'explanation': """A mixture composed of a gas and a liquid that is homogeneous, meaning its components cannot be distinguished and its physical properties are uniform everywhere.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Mixtures by Physical State',
            'examples': ["Carbon dioxide in cold water", "CO2 dissolved in cold water"]
        }
        self.halt()

    @Rule(Fact(query_topic='alloy__brass_example_'))
    def rule_alloy__brass_example_(self):
        """Brass is a specific example of an alloy, which is a solid-solid homogeneous mixture composed of 65% of copper and 35% of zinc."""
        self.response = {
            'concept': 'Alloy (Brass example)',
            'explanation': """Brass is a specific example of an alloy, which is a solid-solid homogeneous mixture composed of 65% of copper and 35% of zinc.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Brass (composed of 65% copper and 35% zinc)", "An alloy of copper and zinc"]
        }
        self.halt()

    @Rule(Fact(query_topic='solution'))
    def rule_solution(self):
        """A homogeneous mixture is also called a solution. A solution is composed of a solvent and one or more solutes, where the components are uniformly distributed."""
        self.response = {
            'concept': 'Solution',
            'explanation': """A homogeneous mixture is also called a solution. A solution is composed of a solvent and one or more solutes, where the components are uniformly distributed.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures and Solutions',
            'examples': ["Salt solution", "Copper sulphate solution", "Sugar solution"]
        }
        self.halt()

    @Rule(Fact(query_topic='solute'))
    def rule_solute(self):
        """In a solution, solutes are the components that are present in a lesser amount (not in excess) compared to the solvent, and are dissolved by the solvent."""
        self.response = {
            'concept': 'Solute',
            'explanation': """In a solution, solutes are the components that are present in a lesser amount (not in excess) compared to the solvent, and are dissolved by the solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Salt (in salt solution)", "Copper sulphate (in copper sulphate solution)", "Sugar (in sugar solution)"]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent'))
    def rule_solvent(self):
        """In a solution, the solvent is the component present in excess, which dissolves the other components (solutes) to form the solution."""
        self.response = {
            'concept': 'Solvent',
            'explanation': """In a solution, the solvent is the component present in excess, which dissolves the other components (solutes) to form the solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Water (in salt solution)", "Water (in copper sulphate solution)", "Water (in sugar solution)"]
        }
        self.halt()

    @Rule(Fact(query_topic='solution_composition'))
    def rule_solution_composition(self):
        """The formation of a solution can be represented by the equation: Solute + Solvent = Solution. This formula indicates how the constituent parts combine to form the final mixture."""
        self.response = {
            'concept': 'Solution Composition',
            'explanation': """The formation of a solution can be represented by the equation: Solute + Solvent = Solution. This formula indicates how the constituent parts combine to form the final mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Salt + Water = Salt solution", "Copper sulphate + Water = Copper sulphate solution", "Sugar + Water = Sugar solution"]
        }
        self.halt()

    @Rule(Fact(query_topic='solubility_of_a_solute'))
    def rule_solubility_of_a_solute(self):
        """Solubility refers to the maximum quantity or amount of a solute that can completely dissolve in a given volume or amount of a solvent under specific conditions, without forming a precipitate."""
        self.response = {
            'concept': 'Solubility of a Solute',
            'explanation': """Solubility refers to the maximum quantity or amount of a solute that can completely dissolve in a given volume or amount of a solvent under specific conditions, without forming a precipitate.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["The maximum mass of salt that can dissolve in 100 ml of water", "The quantity of calcium hydroxide that can dissolve in 100 ml of water", "The amount of sugar that can dissolve in a specific volume of water"]
        }
        self.halt()

    @Rule(Fact(query_topic='varying_solubility_of_different_substances'))
    def rule_varying_solubility_of_different_substances(self):
        """Different substances dissolve in varying quantities in the same volume of water. Some substances exhibit higher solubility, meaning a larger mass can dissolve, while others have lower solubility, dissolving in smaller quantities under identical conditions."""
        self.response = {
            'concept': 'Varying Solubility of Different Substances',
            'explanation': """Different substances dissolve in varying quantities in the same volume of water. Some substances exhibit higher solubility, meaning a larger mass can dissolve, while others have lower solubility, dissolving in smaller quantities under identical conditions.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility Characteristics',
            'examples': ["The quantity dissolved is more for some substances, while it is less for some other substances in the same volume of water.", "An activity involving calcium hydroxide, common salt, and sugar demonstrates that each will dissolve in different maximum amounts in 100 ml of water."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_temperature_on_solubility'))
    def rule_effect_of_temperature_on_solubility(self):
        """For most solid solutes, an increase in temperature leads to an increase in solubility. A greater amount of solute can typically dissolve in a given volume of solvent at a higher temperature compared to the amount that dissolves in an equal volume of the same solvent at room temperature."""
        self.response = {
            'concept': 'Effect of Temperature on Solubility',
            'explanation': """For most solid solutes, an increase in temperature leads to an increase in solubility. A greater amount of solute can typically dissolve in a given volume of solvent at a higher temperature compared to the amount that dissolves in an equal volume of the same solvent at room temperature.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility',
            'examples': ["Repeating dissolution activities using 100 ml of hot water (approx. 80 °C) instead of room temperature water.", "It would be observed that a greater amount of the solute dissolves at a higher temperature than it does in an equal volume of water at room temperature."]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_solubility'))
    def rule_definition_of_solubility(self):
        """The solubility of a solute at a given temperature is quantitatively defined as the maximum mass of that solute which can dissolve in 100 g of the solvent at that specific temperature. This standardization allows for meaningful comparison of different solutes."""
        self.response = {
            'concept': 'Definition of Solubility',
            'explanation': """The solubility of a solute at a given temperature is quantitatively defined as the maximum mass of that solute which can dissolve in 100 g of the solvent at that specific temperature. This standardization allows for meaningful comparison of different solutes.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility Definition',
            'examples': ["At 25 °C, the solubility of magnesium chloride in water is 53.0 g (meaning 53.0 g of magnesium chloride dissolves in 100 g of water).", "At the same temperature, solubility of potassium sulphate in water is 12.0 g (meaning 12.0 g of potassium sulphate dissolves in 100 g of water)."]
        }
        self.halt()

    @Rule(Fact(query_topic='introduction_to_factors_affecting_solubility'))
    def rule_introduction_to_factors_affecting_solubility(self):
        """The solubility of a solute in a given solvent is influenced by various factors. Temperature has been identified as one key factor, and there are other factors, such as the nature of the solute and solvent, which also play a significant role."""
        self.response = {
            'concept': 'Introduction to Factors Affecting Solubility',
            'explanation': """The solubility of a solute in a given solvent is influenced by various factors. Temperature has been identified as one key factor, and there are other factors, such as the nature of the solute and solvent, which also play a significant role.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility',
            'examples': ["You have already identified temperature as a factor affecting the solubility of a solute in a given solvent.", "Activity 3.1.8, comparing the dissolution of common salt and sugar, is designed to investigate other factors affecting solubility beyond just temperature."]
        }
        self.halt()

    @Rule(Fact(query_topic='nature_of_solute_affects_solubility'))
    def rule_nature_of_solute_affects_solubility(self):
        """At the same temperature, different solutes dissolve in different amounts in equal volumes of the same solvent, which confirms that the inherent nature of the solute affects its solubility."""
        self.response = {
            'concept': 'Nature of Solute Affects Solubility',
            'explanation': """At the same temperature, different solutes dissolve in different amounts in equal volumes of the same solvent, which confirms that the inherent nature of the solute affects its solubility.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility',
            'examples': ["Salt dissolves readily in water, while sand remains undissolved.", "Sugar dissolves well in water, but waxes have very low solubility.", "Copper sulfate dissolves more than calcium carbonate in water under similar conditions."]
        }
        self.halt()

    @Rule(Fact(query_topic='nature_of_solvent_affects_solubility'))
    def rule_nature_of_solvent_affects_solubility(self):
        """The solubility of the same solute is different in equal volumes of different solvents at the same temperature, demonstrating that the nature of the solvent significantly affects solubility."""
        self.response = {
            'concept': 'Nature of Solvent Affects Solubility',
            'explanation': """The solubility of the same solute is different in equal volumes of different solvents at the same temperature, demonstrating that the nature of the solvent significantly affects solubility.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility',
            'examples': ["Sugar completely dissolves in water.", "Sugar added to kerosene remains almost undissolved.", "Oil does not dissolve in water, but readily dissolves in hexane."]
        }
        self.halt()

    @Rule(Fact(query_topic='primary_factors_affecting_solubility'))
    def rule_primary_factors_affecting_solubility(self):
        """According to observations, solubility is affected by three confirmed factors: temperature, the nature of the solute, and the nature of the solvent."""
        self.response = {
            'concept': 'Primary Factors Affecting Solubility',
            'explanation': """According to observations, solubility is affected by three confirmed factors: temperature, the nature of the solute, and the nature of the solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility',
            'examples': ["Increasing temperature often increases the solubility of solid solutes.", "Sugar's ability to dissolve in water is due to the nature of both.", "Oil and water do not mix due to their differing natures."]
        }
        self.halt()

    @Rule(Fact(query_topic='polarity_based_classification_of_chemical_compounds'))
    def rule_polarity_based_classification_of_chemical_compounds(self):
        """Chemical compounds can be classified into two categories, polar and non-polar, based on the polarity of their chemical bonds, which is a characteristic property imparted by their constituent particles."""
        self.response = {
            'concept': 'Polarity-Based Classification of Chemical Compounds',
            'explanation': """Chemical compounds can be classified into two categories, polar and non-polar, based on the polarity of their chemical bonds, which is a characteristic property imparted by their constituent particles.""",
            'topic': 'Chemistry',
            'subtopic': 'Compound Classification',
            'examples': ["Water (H2O) is a polar compound.", "Methane (CH4) is a non-polar compound.", "Ethanol (CH3CH2OH) is a polar compound."]
        }
        self.halt()

    @Rule(Fact(query_topic='organic_and_inorganic_classification_of_chemical_compounds'))
    def rule_organic_and_inorganic_classification_of_chemical_compounds(self):
        """Chemical compounds can also be classified as organic or inorganic based on their constituent elements, offering another categorization in addition to polarity."""
        self.response = {
            'concept': 'Organic and Inorganic Classification of Chemical Compounds',
            'explanation': """Chemical compounds can also be classified as organic or inorganic based on their constituent elements, offering another categorization in addition to polarity.""",
            'topic': 'Chemistry',
            'subtopic': 'Compound Classification',
            'examples': ["Sugar is an organic compound.", "Sodium chloride (table salt) is an inorganic compound.", "Methane (natural gas) is an organic compound."]
        }
        self.halt()

    @Rule(Fact(query_topic='four_classes_of_solutes_and_solvents'))
    def rule_four_classes_of_solutes_and_solvents(self):
        """By combining the classifications of polarity (polar/non-polar) and elemental composition (organic/inorganic), solutes and solvents can be categorized into four distinct classes: polar organic, non-polar organic, polar inorganic, and non-polar inorganic."""
        self.response = {
            'concept': 'Four Classes of Solutes and Solvents',
            'explanation': """By combining the classifications of polarity (polar/non-polar) and elemental composition (organic/inorganic), solutes and solvents can be categorized into four distinct classes: polar organic, non-polar organic, polar inorganic, and non-polar inorganic.""",
            'topic': 'Chemistry',
            'subtopic': 'Solute and Solvent Classification',
            'examples': ["Water is a polar inorganic solvent.", "Ethanol is a polar organic solvent.", "Hexane is a non-polar organic solvent."]
        }
        self.halt()

    @Rule(Fact(query_topic='polar_solutes_are_soluble_in_polar_solvents'))
    def rule_polar_solutes_are_soluble_in_polar_solvents(self):
        """Solutes and solvents with similar polarity properties dissolve in each other. Specifically, polar compounds are soluble in polar solvents."""
        self.response = {
            'concept': 'Polar Solutes are Soluble in Polar Solvents',
            'explanation': """Solutes and solvents with similar polarity properties dissolve in each other. Specifically, polar compounds are soluble in polar solvents.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility; Polarity',
            'examples': ["Ethanol is a polar compound and water is a polar compound, therefore ethanol is soluble in water.", "Ammonia is a polar compound and water is a polar compound, therefore ammonia dissolves in water."]
        }
        self.halt()

    @Rule(Fact(query_topic='non_polar_solutes_are_soluble_in_non_polar_solvents'))
    def rule_non_polar_solutes_are_soluble_in_non_polar_solvents(self):
        """Solutes and solvents with similar polarity properties dissolve in each other. Specifically, non-polar compounds are soluble in non-polar solvents."""
        self.response = {
            'concept': 'Non-Polar Solutes are Soluble in Non-Polar Solvents',
            'explanation': """Solutes and solvents with similar polarity properties dissolve in each other. Specifically, non-polar compounds are soluble in non-polar solvents.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility; Polarity',
            'examples': ["Grease is a non-polar solute and kerosene is a non-polar solvent, therefore grease dissolves in kerosene.", "Jak glue (koholle) is a non-polar solute and kerosene is a non-polar solvent, therefore jak glue is soluble in kerosene."]
        }
        self.halt()

    @Rule(Fact(query_topic='like_dissolves_like_principle'))
    def rule_like_dissolves_like_principle(self):
        """Solutes and solvents of similar polarity properties dissolve in each other. This is a general principle governing solubility."""
        self.response = {
            'concept': 'Like Dissolves Like Principle',
            'explanation': """Solutes and solvents of similar polarity properties dissolve in each other. This is a general principle governing solubility.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility; Polarity',
            'examples': ["Polar compounds like water and ethanol mix readily.", "Non-polar substances like oil and benzene are mutually soluble.", "Ionic compounds typically dissolve in polar solvents like water."]
        }
        self.halt()

    @Rule(Fact(query_topic='gases_can_dissolve_in_water'))
    def rule_gases_can_dissolve_in_water(self):
        """Gases can dissolve in water, forming a solution. This dissolved gas can be liberated under certain conditions."""
        self.response = {
            'concept': 'Gases Can Dissolve in Water',
            'explanation': """Gases can dissolve in water, forming a solution. This dissolved gas can be liberated under certain conditions.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility of Gases',
            'examples': ["When a bottle of soda water or a fizzy drink is opened, gas bubbles evolve from the solution.", "When a beaker of water is heated, gas bubbles can be seen on the walls of the beaker.", "Carbon dioxide gas is mixed with water during soda water production."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_pressure_on_gas_solubility_in_water'))
    def rule_effect_of_pressure_on_gas_solubility_in_water(self):
        """The solubility of gases in water increases with higher pressure. More gas dissolves in water under elevated pressure conditions."""
        self.response = {
            'concept': 'Effect of Pressure on Gas Solubility in Water',
            'explanation': """The solubility of gases in water increases with higher pressure. More gas dissolves in water under elevated pressure conditions.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility; Solubility of Gases',
            'examples': ["During the production of soda water, carbon dioxide gas is mixed with water under high pressure, causing more gas to dissolve.", "Atmospheric gases like carbon dioxide and oxygen dissolve only in small quantities in natural water due to lower atmospheric pressure compared to industrial processes."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_temperature_on_gas_solubility_in_water'))
    def rule_effect_of_temperature_on_gas_solubility_in_water(self):
        """The solubility of gases in water decreases as the temperature of the water increases. Heating water causes dissolved gases to evolve."""
        self.response = {
            'concept': 'Effect of Temperature on Gas Solubility in Water',
            'explanation': """The solubility of gases in water decreases as the temperature of the water increases. Heating water causes dissolved gases to evolve.""",
            'topic': 'Chemistry',
            'subtopic': 'Factors Affecting Solubility; Solubility of Gases',
            'examples': ["When water is heated, the dissolved gases are evolved.", "The amount of gases remaining dissolved in hot water is very small.", "Gas bubbles seen on the walls of a heated beaker of water are dissolved gases being liberated."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_temperature_on_solubility__gases_vs__solids_'))
    def rule_effect_of_temperature_on_solubility__gases_vs__solids_(self):
        """The solubility of a solid substance in a solvent generally increases with rising temperature. In contrast, the solubility of a gas in a given solvent decreases as the temperature increases."""
        self.response = {
            'concept': 'Effect of Temperature on Solubility (Gases vs. Solids)',
            'explanation': """The solubility of a solid substance in a solvent generally increases with rising temperature. In contrast, the solubility of a gas in a given solvent decreases as the temperature increases.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["Sugar (a solid) dissolves faster and more completely in hot water than in cold water.", "Carbon dioxide gas escapes more rapidly from a warm bottle of soda water than from a cold one.", "Fish are often stressed in warm water because less oxygen gas is dissolved compared to cold water."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_pressure_on_gas_solubility'))
    def rule_effect_of_pressure_on_gas_solubility(self):
        """The solubility of a gas in a liquid increases when the pressure of that gas in contact with the liquid is increased. Conversely, reducing the pressure of a gas above a liquid will decrease its solubility."""
        self.response = {
            'concept': 'Effect of Pressure on Gas Solubility',
            'explanation': """The solubility of a gas in a liquid increases when the pressure of that gas in contact with the liquid is increased. Conversely, reducing the pressure of a gas above a liquid will decrease its solubility.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["An unopened bottle of soda water feels hard because carbon dioxide gas is dissolved under high pressure.", "When the cap of a soda bottle is opened, the pressure decreases, causing dissolved carbon dioxide to escape as bubbles.", "Deep-sea divers experience increased nitrogen solubility in their blood due to high pressure; rapid ascent can cause 'the bends' as nitrogen bubbles out."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_gas_solubility'))
    def rule_factors_affecting_gas_solubility(self):
        """The solubility of a gas in a liquid is primarily influenced by two main factors: temperature and pressure. Higher temperature generally decreases gas solubility, while higher pressure generally increases it."""
        self.response = {
            'concept': 'Factors Affecting Gas Solubility',
            'explanation': """The solubility of a gas in a liquid is primarily influenced by two main factors: temperature and pressure. Higher temperature generally decreases gas solubility, while higher pressure generally increases it.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["A warm, opened soda bottle quickly loses its fizziness because both high temperature and low pressure reduce CO2 solubility.", "A cold, unopened soda bottle maintains its fizz because low temperature and high pressure keep CO2 dissolved.", "Oxygen levels in lakes are higher in colder months, demonstrating the temperature effect on gas solubility crucial for aquatic life."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_of_a_mixture__concentration_'))
    def rule_composition_of_a_mixture__concentration_(self):
        """The composition of a mixture, particularly a solution, refers to the relative amounts of its constituent components. A higher amount of solute in a fixed amount of solvent results in a more concentrated mixture, leading to a more intense manifestation of its properties (e.g., color, taste)."""
        self.response = {
            'concept': 'Composition of a Mixture (Concentration)',
            'explanation': """The composition of a mixture, particularly a solution, refers to the relative amounts of its constituent components. A higher amount of solute in a fixed amount of solvent results in a more concentrated mixture, leading to a more intense manifestation of its properties (e.g., color, taste).""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures and Solutions',
            'examples': ["A solution made with 0.4 g of potassium permanganate in 50 ml of water will be a more intense purple color than one made with 0.2 g in the same volume of water.", "Adding more sugar to a glass of tea increases its sweetness and makes the tea more concentrated with respect to sugar.", "Diluting a concentrated juice with water reduces its concentration and makes its color lighter and taste less intense."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_of_a_mixture'))
    def rule_composition_of_a_mixture(self):
        """The composition of a mixture refers to the relative amounts of its components. Different compositions lead to different properties, such as color intensity in solutions. Understanding and controlling the composition is crucial for various applications, including preparing pharmaceuticals, agricultural chemicals, and laboratory solutions."""
        self.response = {
            'concept': 'Composition of a Mixture',
            'explanation': """The composition of a mixture refers to the relative amounts of its components. Different compositions lead to different properties, such as color intensity in solutions. Understanding and controlling the composition is crucial for various applications, including preparing pharmaceuticals, agricultural chemicals, and laboratory solutions.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["Potassium permanganate solutions with varying purple color intensities due to different amounts of solute.", "Preparing mixtures of weedicides and insecticides in correct proportions for effectiveness.", "Laboratory solutions that require a fixed composition for experimental accuracy."]
        }
        self.halt()

    @Rule(Fact(query_topic='mass_fraction__m_m_'))
    def rule_mass_fraction__m_m_(self):
        """Mass fraction expresses the composition of a mixture as the ratio of the mass of a specific component to the total mass of the mixture. For a component A in a mixture with components A and B, the mass fraction of A is calculated as (Mass of A) / (Mass of A + Mass of B)."""
        self.response = {
            'concept': 'Mass Fraction (m/m)',
            'explanation': """Mass fraction expresses the composition of a mixture as the ratio of the mass of a specific component to the total mass of the mixture. For a component A in a mixture with components A and B, the mass fraction of A is calculated as (Mass of A) / (Mass of A + Mass of B).""",
            'topic': 'Chemistry',
            'subtopic': 'Expressing Composition of Mixtures',
            'examples': ["If 100 g of a solution contains 5 g of solute, the mass fraction of the solute is 5 g / 100 g = 0.05.", "If 250 g of a salt solution yields 10 g of salt upon evaporation, the mass fraction of salt is 10 g / 250 g = 0.04."]
        }
        self.halt()

    @Rule(Fact(query_topic='volume_fraction__v_v_'))
    def rule_volume_fraction__v_v_(self):
        """Volume fraction is a method used to indicate the composition of a mixture, specifically when both of its components exist in either the liquid state or the gaseous state. The volume fraction of a component A in a mixture of A and B is given as (Volume of A) / (Volume of A + Volume of B)."""
        self.response = {
            'concept': 'Volume Fraction (V/V)',
            'explanation': """Volume fraction is a method used to indicate the composition of a mixture, specifically when both of its components exist in either the liquid state or the gaseous state. The volume fraction of a component A in a mixture of A and B is given as (Volume of A) / (Volume of A + Volume of B).""",
            'topic': 'Chemistry',
            'subtopic': 'Expressing Composition of Mixtures',
            'examples': ["A mixture of alcohol and water (both liquids).", "A mixture of oxygen and nitrogen gases (like air).", "A mixture of two miscible liquid components used in a chemical reaction."]
        }
        self.halt()

    @Rule(Fact(query_topic='volume_fraction'))
    def rule_volume_fraction(self):
        """The volume fraction of a given component of a mixture is the ratio of the volume of that component to the total volume of the mixture. It is calculated as the Volume of the component divided by the Total volume of the mixture."""
        self.response = {
            'concept': 'Volume Fraction',
            'explanation': """The volume fraction of a given component of a mixture is the ratio of the volume of that component to the total volume of the mixture. It is calculated as the Volume of the component divided by the Total volume of the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Composition of Mixtures',
            'examples': ["A solution of final volume 250 cm³ was made by adding distilled water to 25 cm³ of ethyl alcohol. The volume fraction of ethyl alcohol is 25 cm³ / 250 cm³ = 0.1.", "To prepare 500 cm³ of an aqueous solution of acetic acid with a volume fraction of 1/25, the required volume of acetic acid is (1/25) x 500 cm³ = 20 cm³."]
        }
        self.halt()

    @Rule(Fact(query_topic='mole_fraction'))
    def rule_mole_fraction(self):
        """The mole fraction of a component of a mixture is the ratio of the amount of moles of that component to the total amount of moles of all the components in the mixture. For a mixture of components A and B, the mole fraction of A is (Amount of moles of A) / (Amount of moles of A + Amount of moles of B)."""
        self.response = {
            'concept': 'Mole Fraction',
            'explanation': """The mole fraction of a component of a mixture is the ratio of the amount of moles of that component to the total amount of moles of all the components in the mixture. For a mixture of components A and B, the mole fraction of A is (Amount of moles of A) / (Amount of moles of A + Amount of moles of B).""",
            'topic': 'Chemistry',
            'subtopic': 'Composition of Mixtures',
            'examples': ["To find the mole fraction of sodium hydroxide (NaOH) in a solution made by dissolving 40 g of NaOH in 180 g of water, first calculate the moles: moles of water = 180 g / 18 g mol⁻¹ = 10 mol, and moles of NaOH = 40 g / 40 g mol⁻¹ = 1 mol."]
        }
        self.halt()

    @Rule(Fact(query_topic='mole_fraction'))
    def rule_mole_fraction(self):
        """The mole fraction of a component in a mixture is defined as the ratio of the amount of moles of that specific component to the total amount of moles of all components present in the mixture. It is a unitless quantity."""
        self.response = {
            'concept': 'Mole Fraction',
            'explanation': """The mole fraction of a component in a mixture is defined as the ratio of the amount of moles of that specific component to the total amount of moles of all components present in the mixture. It is a unitless quantity.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Mole fraction of sodium hydroxide = (Amount of moles of sodium hydroxide) / (Amount of moles of water + Amount of moles of sodium hydroxide)", "Given 1 mole of sodium hydroxide and 10 moles of water, the mole fraction of sodium hydroxide is 1 / (10 + 1) = 1/11.", "Given 1 mole of sodium hydroxide and 10 moles of water, the mole fraction of water is 10 / (10 + 1) = 10/11."]
        }
        self.halt()

    @Rule(Fact(query_topic='sum_of_fractions__mole__mass__volume_'))
    def rule_sum_of_fractions__mole__mass__volume_(self):
        """The sum of mole fractions, mass fractions, or volume fractions of all the individual components within a given mixture is always equal to one. These fractional quantities are dimensionless."""
        self.response = {
            'concept': 'Sum of Fractions (Mole, Mass, Volume)',
            'explanation': """The sum of mole fractions, mass fractions, or volume fractions of all the individual components within a given mixture is always equal to one. These fractional quantities are dimensionless.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Sum of mole fractions = Mole fraction of water + Mole fraction of sodium hydroxide = 10/11 + 1/11 = 1.", "The sum of mole fractions of all the components in a mixture is one.", "The sum of mass fractions or volume fractions of all the components in a mixture is equal to one."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_as_a_percentage'))
    def rule_composition_as_a_percentage(self):
        """The composition of a mixture, initially expressed as a fraction (e.g., mass fraction, mole fraction), can be converted and expressed as a percentage by multiplying the fraction by 100."""
        self.response = {
            'concept': 'Composition as a Percentage',
            'explanation': """The composition of a mixture, initially expressed as a fraction (e.g., mass fraction, mole fraction), can be converted and expressed as a percentage by multiplying the fraction by 100.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Composition as a percentage = Fraction x 100", "If the mass fraction of magnesium carbonate is 0.6, its composition as a mass percentage is 0.6 x 100 = 60%.", "A mole fraction of 0.35 can be expressed as 35%."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_as_parts_per_million__ppm_'))
    def rule_composition_as_parts_per_million__ppm_(self):
        """The composition of a mixture, when expressed as a fraction, can be converted to parts per million (ppm) by multiplying the fraction by 1,000,000."""
        self.response = {
            'concept': 'Composition as Parts Per Million (ppm)',
            'explanation': """The composition of a mixture, when expressed as a fraction, can be converted to parts per million (ppm) by multiplying the fraction by 1,000,000.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Composition as parts per million (ppm) = Fraction x 1,000,000", "If the mass fraction of a trace contaminant is 0.000005, its concentration in ppm is 5 ppm.", "A volume fraction of 0.0002 for a gas component is equivalent to 200 ppm."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_in_terms_of_mass_volume__m_v_'))
    def rule_composition_in_terms_of_mass_volume__m_v_(self):
        """This method expresses the composition of a mixture by stating the mass of solute contained in a unit volume of the mixture. It is a measure of concentration."""
        self.response = {
            'concept': 'Composition in terms of Mass/Volume (m/v)',
            'explanation': """This method expresses the composition of a mixture by stating the mass of solute contained in a unit volume of the mixture. It is a measure of concentration.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Composition of solute (m/v) = Mass of sodium chloride / Volume of solution", "If 1 dm³ of Jeewani solution contains 5 g of sodium chloride, the composition is 5 g / 1 dm³ = 5 g dm⁻³.", "A solution containing 25 g of a substance in 500 cm³ (0.5 dm³) would have an m/v composition of 50 g dm⁻³."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_in_terms_of_amount_of_moles_volume__n_v_'))
    def rule_composition_in_terms_of_amount_of_moles_volume__n_v_(self):
        """This method is used to express the composition of a homogeneous mixture (solution) in terms of the amount of moles of solute contained in a unit volume of the solution. The 'mole' is the international unit for the amount of matter, and this measure is commonly known as Molarity."""
        self.response = {
            'concept': 'Composition in terms of Amount of Moles/Volume (n/v)',
            'explanation': """This method is used to express the composition of a homogeneous mixture (solution) in terms of the amount of moles of solute contained in a unit volume of the solution. The 'mole' is the international unit for the amount of matter, and this measure is commonly known as Molarity.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures Composition',
            'examples': ["Composition (n/v) = Amount of moles of solute / Volume of solution", "If a solution contains 0.2 moles of solute in 1 dm³ of solution, its n/v composition is 0.2 mol dm⁻³.", "Expressing composition as moles per litre (mol L⁻¹) or moles per cubic decimeter (mol dm⁻³) is an example of n/v composition."]
        }
        self.halt()

    @Rule(Fact(query_topic='concentration__c_'))
    def rule_concentration__c_(self):
        """Concentration is the amount of solute contained in a unit volume of a solution. In chemistry, it is often expressed as the amount of moles of solute contained in a cubic decimetre (mol dm⁻³) of the solution."""
        self.response = {
            'concept': 'Concentration (C)',
            'explanation': """Concentration is the amount of solute contained in a unit volume of a solution. In chemistry, it is often expressed as the amount of moles of solute contained in a cubic decimetre (mol dm⁻³) of the solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Chemistry',
            'examples': ["If 2 dm³ of a solution contains 4 moles of sodium hydroxide, its concentration is 2 mol dm⁻³.", "A solution with 2 moles of solute in 1 dm³ has a concentration of 2 mol dm⁻³."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculating_mass_of_solute_for_solution_preparation'))
    def rule_calculating_mass_of_solute_for_solution_preparation(self):
        """To prepare a solution of a specific concentration and volume, the required mass of solute is calculated using its molar mass and the desired number of moles. This often involves converting between volume units."""
        self.response = {
            'concept': 'Calculating Mass of Solute for Solution Preparation',
            'explanation': """To prepare a solution of a specific concentration and volume, the required mass of solute is calculated using its molar mass and the desired number of moles. This often involves converting between volume units.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation',
            'examples': ["To prepare 1 dm³ of a 1 mol dm⁻³ glucose solution, 180 g of glucose (Molar mass = 180 g mol⁻¹) is required.", "To prepare 500 cm³ of a 1 mol dm⁻³ glucose solution, 90 g of glucose is required."]
        }
        self.halt()

    @Rule(Fact(query_topic='standard_solution'))
    def rule_standard_solution(self):
        """A standard solution is a solution in which the concentration is very accurately known. These solutions are essential for various chemical experiments."""
        self.response = {
            'concept': 'Standard Solution',
            'explanation': """A standard solution is a solution in which the concentration is very accurately known. These solutions are essential for various chemical experiments.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation',
            'examples': ["Standard solutions are required to be prepared for chemical experiments.", "A solution with its concentration precisely determined is considered a standard solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='volume_unit_relationships'))
    def rule_volume_unit_relationships(self):
        """Key relationships between common volume units are crucial for accurate solution preparation and calculations in chemistry."""
        self.response = {
            'concept': 'Volume Unit Relationships',
            'explanation': """Key relationships between common volume units are crucial for accurate solution preparation and calculations in chemistry.""",
            'topic': 'Chemistry',
            'subtopic': 'Units and Conversions',
            'examples': ["1 dm³ = 1 l (Litre)", "1 dm³ = 1000 cm³", "1 cm³ = 1 ml"]
        }
        self.halt()

    @Rule(Fact(query_topic='laboratory_equipment_for_solution_preparation'))
    def rule_laboratory_equipment_for_solution_preparation(self):
        """Specific laboratory equipment is necessary to accurately prepare a solution of a specified concentration, ensuring precision in measurements."""
        self.response = {
            'concept': 'Laboratory Equipment for Solution Preparation',
            'explanation': """Specific laboratory equipment is necessary to accurately prepare a solution of a specified concentration, ensuring precision in measurements.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Techniques',
            'examples': ["Volumetric flasks are used for precise volume measurements.", "A funnel assists in transferring solids or liquids into volumetric flasks.", "A wash bottle is used for rinsing glassware."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculation_of_solute_mass_for_solution_preparation'))
    def rule_calculation_of_solute_mass_for_solution_preparation(self):
        """Before preparing a solution of a specific concentration, the required mass of the solute must be calculated using its molar mass, the desired concentration, and the final volume."""
        self.response = {
            'concept': 'Calculation of Solute Mass for Solution Preparation',
            'explanation': """Before preparing a solution of a specific concentration, the required mass of the solute must be calculated using its molar mass, the desired concentration, and the final volume.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation Stoichiometry',
            'examples': ["Molar mass of sodium chloride = (23.0 + 35.5) g mol-1 = 58.5 g mol-1", "Mass of sodium chloride in 1000 cm3 of a 1 mol dm-3 solution = 58.5 g", "Mass of sodium chloride in 500 cm3 of a 1 mol dm-3 solution = 29.25 g"]
        }
        self.halt()

    @Rule(Fact(query_topic='accurate_weighing_of_solid_solute'))
    def rule_accurate_weighing_of_solid_solute(self):
        """The calculated mass of the solid solute must be weighed very accurately onto a watch glass using a precision balance, such as a four beam balance or chemical balance."""
        self.response = {
            'concept': 'Accurate Weighing of Solid Solute',
            'explanation': """The calculated mass of the solid solute must be weighed very accurately onto a watch glass using a precision balance, such as a four beam balance or chemical balance.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Techniques',
            'examples': ["Weigh 29.25 g of sodium chloride very accurately.", "Use a four beam balance/chemical balance.", "Weigh solute onto a watch glass."]
        }
        self.halt()

    @Rule(Fact(query_topic='preparation_and_use_of_a_volumetric_flask'))
    def rule_preparation_and_use_of_a_volumetric_flask(self):
        """A clean volumetric flask of the correct volume should be selected. Its stopper must be removed, and a clean funnel placed in its neck to aid in transferring the solute."""
        self.response = {
            'concept': 'Preparation and Use of a Volumetric Flask',
            'explanation': """A clean volumetric flask of the correct volume should be selected. Its stopper must be removed, and a clean funnel placed in its neck to aid in transferring the solute.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Equipment and Procedures',
            'examples': ["Select a clean 500 cm3 volumetric flask.", "Remove its stopper.", "Place a clean funnel in the flask opening."]
        }
        self.halt()

    @Rule(Fact(query_topic='complete_transfer_of_solute_and_washings'))
    def rule_complete_transfer_of_solute_and_washings(self):
        """Ensure the weighed solute is completely transferred from the watch glass into the volumetric flask via the funnel. Rinse the watch glass and the inner surface of the funnel with a wash bottle, transferring all washings into the flask to avoid solute loss."""
        self.response = {
            'concept': 'Complete Transfer of Solute and Washings',
            'explanation': """Ensure the weighed solute is completely transferred from the watch glass into the volumetric flask via the funnel. Rinse the watch glass and the inner surface of the funnel with a wash bottle, transferring all washings into the flask to avoid solute loss.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation Technique',
            'examples': ["Transfer the weighed sodium chloride completely through the funnel.", "Wash the surface of the watch glass and inner surface of the funnel.", "Transfer the washings into the flask."]
        }
        self.halt()

    @Rule(Fact(query_topic='initial_dissolution_of_solute'))
    def rule_initial_dissolution_of_solute(self):
        """Add approximately two-thirds of the total required water volume to the flask, stopper it, and shake thoroughly until all the solute is completely dissolved."""
        self.response = {
            'concept': 'Initial Dissolution of Solute',
            'explanation': """Add approximately two-thirds of the total required water volume to the flask, stopper it, and shake thoroughly until all the solute is completely dissolved.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation Technique',
            'examples': ["Add about 2/3 of the required volume of water.", "Stopper the volumetric flask.", "Shake the flask so that all of the sodium chloride dissolves well."]
        }
        self.halt()

    @Rule(Fact(query_topic='adjusting_final_volume_to_the_mark'))
    def rule_adjusting_final_volume_to_the_mark(self):
        """Carefully add water to the volumetric flask until the bottom of the meniscus aligns precisely with the volume mark, ensuring your eye is at the level of the mark to prevent parallax error."""
        self.response = {
            'concept': 'Adjusting Final Volume to the Mark',
            'explanation': """Carefully add water to the volumetric flask until the bottom of the meniscus aligns precisely with the volume mark, ensuring your eye is at the level of the mark to prevent parallax error.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation Technique',
            'examples': ["Add water carefully, keeping the eye at the level of the volume mark.", "Stop adding water when the meniscus is at the position of the mark.", "Refer to Figure 3.2.3 for correct meniscus positioning."]
        }
        self.halt()

    @Rule(Fact(query_topic='final_mixing_for_solution_homogeneity'))
    def rule_final_mixing_for_solution_homogeneity(self):
        """After adjusting the solution's volume to the mark, stopper the flask and mix it again to ensure the solution is homogeneous and of uniform concentration."""
        self.response = {
            'concept': 'Final Mixing for Solution Homogeneity',
            'explanation': """After adjusting the solution's volume to the mark, stopper the flask and mix it again to ensure the solution is homogeneous and of uniform concentration.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation Technique',
            'examples': ["Stopper the flask and mix again.", "Ensure all salt is dissolved well.", "Consult teacher for proper mixing instructions."]
        }
        self.halt()

    @Rule(Fact(query_topic='critical_factors_for_accurate_standard_solution_preparation'))
    def rule_critical_factors_for_accurate_standard_solution_preparation(self):
        """When preparing a solution of a specific concentration, several critical factors must be considered to ensure accuracy and reliability."""
        self.response = {
            'concept': 'Critical Factors for Accurate Standard Solution Preparation',
            'explanation': """When preparing a solution of a specific concentration, several critical factors must be considered to ensure accuracy and reliability.""",
            'topic': 'Chemistry',
            'subtopic': 'Best Practices in Solution Preparation',
            'examples': ["Cleanliness of all the equipment used.", "Weighing the solute accurately.", "Adjusting the final volume carefully."]
        }
        self.halt()

    @Rule(Fact(query_topic='general_method_for_preparing_solutions'))
    def rule_general_method_for_preparing_solutions(self):
        """This activity outlines the practical steps for preparing various solutions by accurately measuring the solute, dissolving it, and diluting to a specific final volume. It also emphasizes the importance of labeling solutions with the solute name, concentration, and date of preparation, and identifying the solute and solvent."""
        self.response = {
            'concept': 'General Method for Preparing Solutions',
            'explanation': """This activity outlines the practical steps for preparing various solutions by accurately measuring the solute, dissolving it, and diluting to a specific final volume. It also emphasizes the importance of labeling solutions with the solute name, concentration, and date of preparation, and identifying the solute and solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions and Concentrations / Practical Chemistry',
            'examples': ["Preparing 250 cm3 of 1 mol dm-3 sodium chloride (NaCl) solution.", "Preparing 100 cm3 of 1 mol dm-3 glucose (C6H12O6) solution.", "Preparing 500 cm3 of 1 mol dm-3 urea (CO(NH2)2) solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='importance_of_accurate_solution_composition'))
    def rule_importance_of_accurate_solution_composition(self):
        """Certain applications and processes require solutions to have a very precise and accurate composition to ensure desired outcomes or safety. This necessitates careful measurement and preparation techniques."""
        self.response = {
            'concept': 'Importance of Accurate Solution Composition',
            'explanation': """Certain applications and processes require solutions to have a very precise and accurate composition to ensure desired outcomes or safety. This necessitates careful measurement and preparation techniques.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions and Concentrations / Practical Chemistry',
            'examples': ["Preparation of saline solutions for medical purposes.", "Solutions used in analytical chemistry for titrations.", "Pharmaceutical preparations where dosage depends on exact concentration."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculating_concentration_of_a_solution__from_mass_and_volume_'))
    def rule_calculating_concentration_of_a_solution__from_mass_and_volume_(self):
        """To determine the molar concentration (mol dm-3) of a solution, first calculate the amount of moles of the solute from its mass and molar mass, then divide by the total volume of the solution, ensuring the volume is expressed in dm3."""
        self.response = {
            'concept': 'Calculating Concentration of a Solution (from Mass and Volume)',
            'explanation': """To determine the molar concentration (mol dm-3) of a solution, first calculate the amount of moles of the solute from its mass and molar mass, then divide by the total volume of the solution, ensuring the volume is expressed in dm3.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions and Concentrations / Stoichiometry Calculations',
            'examples': ["A solution prepared by dissolving 17 g of sodium nitrate (NaNO3) in water to a final volume of 200 cm3 has a concentration of 1 mol dm-3.", "Molar mass of NaNO3 = 85 g mol-1.", "Concentration = (Moles of Solute) / (Volume of Solution in dm3)."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculating_mass_of_solute_for_desired_concentration_and_volume'))
    def rule_calculating_mass_of_solute_for_desired_concentration_and_volume(self):
        """To prepare a solution of a specific concentration and volume, calculate the required moles of solute by multiplying the desired concentration by the volume in dm3, then convert this amount in moles to mass using the solute's molar mass."""
        self.response = {
            'concept': 'Calculating Mass of Solute for Desired Concentration and Volume',
            'explanation': """To prepare a solution of a specific concentration and volume, calculate the required moles of solute by multiplying the desired concentration by the volume in dm3, then convert this amount in moles to mass using the solute's molar mass.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions and Concentrations / Stoichiometry Calculations',
            'examples': ["To prepare 500 cm3 of a 1 mol dm-3 potassium carbonate (K2CO3) solution, 69 g of K2CO3 is required.", "Molar mass of K2CO3 = 138 g mol-1.", "Mass required = (Concentration × Volume in dm3) × Molar Mass."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculating_solution_concentration__step_by_step_method_'))
    def rule_calculating_solution_concentration__step_by_step_method_(self):
        """To find the concentration of a solution, first calculate the molar mass of the solute. Then, determine the amount of moles of the solute present in the given mass. Finally, divide the amount of moles by the volume of the solution (usually in dm³) to obtain the concentration in mol dm⁻³."""
        self.response = {
            'concept': 'Calculating Solution Concentration (Step-by-Step Method)',
            'explanation': """To find the concentration of a solution, first calculate the molar mass of the solute. Then, determine the amount of moles of the solute present in the given mass. Finally, divide the amount of moles by the volume of the solution (usually in dm³) to obtain the concentration in mol dm⁻³.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Concentration',
            'examples': ["For 12 g of urea (CO(NH2)2) in 1 dm³: Molar mass = 60 g mol⁻¹, Moles = 12g / 60g mol⁻¹ = 0.2 mol, Concentration = 0.2 mol / 1 dm³ = 0.2 mol dm⁻³.", "For 18 g of glucose (C6H12O6) in 250 cm³: Molar mass = 180 g mol⁻¹, Moles = 18g / 180g mol⁻¹ = 0.1 mol, Volume = 0.25 dm³, Concentration = 0.1 mol / 0.25 dm³ = 0.4 mol dm⁻³."]
        }
        self.halt()

    @Rule(Fact(query_topic='dilution_of_solutions'))
    def rule_dilution_of_solutions(self):
        """Dilution is the process of decreasing the concentration of a solution by adding more solvent to it. This technique is commonly used to prepare less concentrated solutions from stock concentrated solutions for laboratory experiments."""
        self.response = {
            'concept': 'Dilution of Solutions',
            'explanation': """Dilution is the process of decreasing the concentration of a solution by adding more solvent to it. This technique is commonly used to prepare less concentrated solutions from stock concentrated solutions for laboratory experiments.""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Preparation',
            'examples': ["Adding distilled water to a concentrated acid to prepare a safer, less concentrated acid solution for an experiment.", "Preparing a 0.1 M sodium hydroxide solution from a 1.0 M stock solution by adding a specific volume of water."]
        }
        self.halt()

    @Rule(Fact(query_topic='safety_measure_for_diluting_concentrated_acids'))
    def rule_safety_measure_for_diluting_concentrated_acids(self):
        """When diluting concentrated acids, it is crucial to always add the acid slowly to water, rather than adding water to acid. This is because the dilution of concentrated acids is a highly exothermic process, and adding water directly to concentrated acid can cause rapid boiling and dangerous splashing."""
        self.response = {
            'concept': 'Safety Measure for Diluting Concentrated Acids',
            'explanation': """When diluting concentrated acids, it is crucial to always add the acid slowly to water, rather than adding water to acid. This is because the dilution of concentrated acids is a highly exothermic process, and adding water directly to concentrated acid can cause rapid boiling and dangerous splashing.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Safety',
            'examples': ["Pouring concentrated sulfuric acid carefully into a beaker of water while stirring.", "Never adding water directly into a flask containing concentrated hydrochloric acid.", "A lab rule stating 'Always add acid to water'."]
        }
        self.halt()

    @Rule(Fact(query_topic='concentration_formula__c___n_v_'))
    def rule_concentration_formula__c___n_v_(self):
        """The concentration (C) of a solution can be calculated using the formula C = n/V, where 'n' represents the amount of solute in moles (mol) and 'V' represents the total volume of the solution in cubic decimetres (dm⁻³). The resulting concentration 'C' is expressed in moles per cubic decimetre (mol dm⁻³)."""
        self.response = {
            'concept': 'Concentration Formula (C = n/V)',
            'explanation': """The concentration (C) of a solution can be calculated using the formula C = n/V, where 'n' represents the amount of solute in moles (mol) and 'V' represents the total volume of the solution in cubic decimetres (dm⁻³). The resulting concentration 'C' is expressed in moles per cubic decimetre (mol dm⁻³).""",
            'topic': 'Chemistry',
            'subtopic': 'Solution Concentration',
            'examples': ["If 0.2 moles of urea are dissolved in 1 dm³ of solution, the concentration C = 0.2 mol / 1 dm³ = 0.2 mol dm⁻³.", "For 0.4 moles of glucose in 1 dm³ (equivalent volume) of solution, the concentration C = 0.4 mol / 1 dm³ = 0.4 mol dm⁻³.", "A solution containing 0.5 mol of salt in 2 dm³ of water has a concentration C = 0.5 mol / 2 dm³ = 0.25 mol dm⁻³."]
        }
        self.halt()

    @Rule(Fact(query_topic='separation_of_compounds_in_mixtures'))
    def rule_separation_of_compounds_in_mixtures(self):
        """Many essential substances available in the Earth's crust rarely exist in pure form and are naturally mixed with other substances. Therefore, the essential components must be separated from these mixtures."""
        self.response = {
            'concept': 'Separation of compounds in mixtures',
            'explanation': """Many essential substances available in the Earth's crust rarely exist in pure form and are naturally mixed with other substances. Therefore, the essential components must be separated from these mixtures.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["Removal of stones and sand from rice", "Separation of salt from sea water", "Separation of gases such as oxygen, nitrogen and argon from atmospheric air"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_separation'))
    def rule_mechanical_separation(self):
        """The separation of components in a mixture using the difference of their physical properties such as density, particle size, particle shape, magnetic properties and electric properties."""
        self.response = {
            'concept': 'Mechanical separation',
            'explanation': """The separation of components in a mixture using the difference of their physical properties such as density, particle size, particle shape, magnetic properties and electric properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Methods of separation',
            'examples': ["Sifting rice to remove sand (based on difference in densities)", "Winnowing to remove chaff from rice (based on difference in densities)", "Sieving to remove gravel from sand (based on difference in particle size)"]
        }
        self.halt()

    @Rule(Fact(query_topic='density_separation__using_a_water_stream_'))
    def rule_density_separation__using_a_water_stream_(self):
        """A method of separating components of a mixture based on differences in their densities. When directed into a stream of water, components with different densities will separate, with heavier ones settling and lighter ones being carried away."""
        self.response = {
            'concept': 'Density Separation (using a water stream)',
            'explanation': """A method of separating components of a mixture based on differences in their densities. When directed into a stream of water, components with different densities will separate, with heavier ones settling and lighter ones being carried away.""",
            'topic': 'Chemistry',
            'subtopic': 'Mechanical Methods of Separation',
            'examples': ["Separating gold from ores", "Separating seed paddy components based on density differences using water"]
        }
        self.halt()

    @Rule(Fact(query_topic='magnetic_separation'))
    def rule_magnetic_separation(self):
        """A separation method that utilizes the magnetic properties of components in a mixture. Magnetic components are attracted by a magnet, allowing them to be separated from non-magnetic components."""
        self.response = {
            'concept': 'Magnetic Separation',
            'explanation': """A separation method that utilizes the magnetic properties of components in a mixture. Magnetic components are attracted by a magnet, allowing them to be separated from non-magnetic components.""",
            'topic': 'Chemistry',
            'subtopic': 'Mechanical Methods of Separation',
            'examples': ["Separating certain minerals from mineral sands", "Separating iron filings from a mixture"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_methods_of_separation'))
    def rule_mechanical_methods_of_separation(self):
        """A category of physical methods used to separate components of a mixture. These methods include winnowing, sieving, sifting, floating, and subjecting to magnetism, and are frequently used in daily life."""
        self.response = {
            'concept': 'Mechanical Methods of Separation',
            'explanation': """A category of physical methods used to separate components of a mixture. These methods include winnowing, sieving, sifting, floating, and subjecting to magnetism, and are frequently used in daily life.""",
            'topic': 'Chemistry',
            'subtopic': 'Methods of Separation',
            'examples': ["Winnowing", "Sieving", "Magnetic separation"]
        }
        self.halt()

    @Rule(Fact(query_topic='vapourisation_evaporation'))
    def rule_vapourisation_evaporation(self):
        """A separation method where heat is supplied to a mixture, causing unnecessary components to vaporize and leave behind the essential component. This process exploits differences in boiling points or volatility."""
        self.response = {
            'concept': 'Vapourisation/Evaporation',
            'explanation': """A separation method where heat is supplied to a mixture, causing unnecessary components to vaporize and leave behind the essential component. This process exploits differences in boiling points or volatility.""",
            'topic': 'Chemistry',
            'subtopic': 'Methods of Separation',
            'examples': ["Extraction of salt from sea water through solar heat", "Separating pure gold from gold amalgam by heating to evaporate mercury"]
        }
        self.halt()

    @Rule(Fact(query_topic='amalgam'))
    def rule_amalgam(self):
        """A special type of solution formed when metals are dissolved in mercury."""
        self.response = {
            'concept': 'Amalgam',
            'explanation': """A special type of solution formed when metals are dissolved in mercury.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Gold amalgam (a solution of impure or pure gold dissolved in mercury)", "Any metal dissolved in mercury"]
        }
        self.halt()

    @Rule(Fact(query_topic='filtration'))
    def rule_filtration(self):
        """A separation method used to separate components that remain suspended in a liquid without dissolving. It requires a filter to retain the solid particles while allowing the liquid to pass through."""
        self.response = {
            'concept': 'Filtration',
            'explanation': """A separation method used to separate components that remain suspended in a liquid without dissolving. It requires a filter to retain the solid particles while allowing the liquid to pass through.""",
            'topic': 'Chemistry',
            'subtopic': 'Methods of Separation',
            'examples': ["Making coconut milk by straining solids from the liquid", "Using a milk-strainer to separate solids from liquid", "Using filter paper in laboratory settings"]
        }
        self.halt()

    @Rule(Fact(query_topic='filter_mechanism'))
    def rule_filter_mechanism(self):
        """A filter is a device with small holes. Particles that are smaller than these holes can pass through, while particles that are larger than the holes cannot pass through them."""
        self.response = {
            'concept': 'Filter Mechanism',
            'explanation': """A filter is a device with small holes. Particles that are smaller than these holes can pass through, while particles that are larger than the holes cannot pass through them.""",
            'topic': 'Chemistry',
            'subtopic': 'Filtration',
            'examples': ["Sand filters used in water purifying plants", "Filter papers used in laboratories"]
        }
        self.halt()

    @Rule(Fact(query_topic='filtration'))
    def rule_filtration(self):
        """Filtration is a separation technique based on the concept that particles smaller than a filter's holes can pass through, while larger particles are retained, thereby separating them from a mixture."""
        self.response = {
            'concept': 'Filtration',
            'explanation': """Filtration is a separation technique based on the concept that particles smaller than a filter's holes can pass through, while larger particles are retained, thereby separating them from a mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating large clay particles from a mixture of water, salt, and soil", "Using sand filters to purify water"]
        }
        self.halt()

    @Rule(Fact(query_topic='residue'))
    def rule_residue(self):
        """In the process of filtration, the substance that is left behind on the filter because its particles are too large to pass through the filter's holes is called the residue."""
        self.response = {
            'concept': 'Residue',
            'explanation': """In the process of filtration, the substance that is left behind on the filter because its particles are too large to pass through the filter's holes is called the residue.""",
            'topic': 'Chemistry',
            'subtopic': 'Filtration Terminology',
            'examples': ["Large clay particles from soil held back by the filter paper", "The dry soil remaining on the filter paper after filtration"]
        }
        self.halt()

    @Rule(Fact(query_topic='filtrate'))
    def rule_filtrate(self):
        """In the process of filtration, the solution or substance composed of particles small enough to pass through the filter's holes is known as the filtrate."""
        self.response = {
            'concept': 'Filtrate',
            'explanation': """In the process of filtration, the solution or substance composed of particles small enough to pass through the filter's holes is known as the filtrate.""",
            'topic': 'Chemistry',
            'subtopic': 'Filtration Terminology',
            'examples': ["The water and salt solution that passes through the filter paper", "The liquid collected in the flask after filtration of a soil, salt, and water mixture"]
        }
        self.halt()

    @Rule(Fact(query_topic='saturated_solution'))
    def rule_saturated_solution(self):
        """A saturated solution is a homogeneous mixture where, at a specific temperature, the maximum possible concentration of a solute is dissolved in the solvent, meaning no more of that substance can dissolve."""
        self.response = {
            'concept': 'Saturated Solution',
            'explanation': """A saturated solution is a homogeneous mixture where, at a specific temperature, the maximum possible concentration of a solute is dissolved in the solvent, meaning no more of that substance can dissolve.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["A sugar solution where no more sugar can dissolve at a given temperature", "A solution where the concentration of a substance has reached its upper limit for a specific temperature"]
        }
        self.halt()

    @Rule(Fact(query_topic='crystallisation'))
    def rule_crystallisation(self):
        """Crystallisation is a method for separating solid substances from a solution by increasing the concentration of the solute, typically through vaporization of the solvent from a saturated solution, which causes the solute to separate out and form crystals."""
        self.response = {
            'concept': 'Crystallisation',
            'explanation': """Crystallisation is a method for separating solid substances from a solution by increasing the concentration of the solute, typically through vaporization of the solvent from a saturated solution, which causes the solute to separate out and form crystals.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Manufacturing of sugar", "Separating a solute by vaporizing its saturated solution to form crystals"]
        }
        self.halt()

    @Rule(Fact(query_topic='crystallization'))
    def rule_crystallization(self):
        """A separation technique where a dissolved substance separates out from a solution as solid crystals. This process is typically achieved by increasing the concentration of the solution, often through methods like vaporization, which causes the solute to exceed its solubility limit and form crystals."""
        self.response = {
            'concept': 'Crystallization',
            'explanation': """A separation technique where a dissolved substance separates out from a solution as solid crystals. This process is typically achieved by increasing the concentration of the solution, often through methods like vaporization, which causes the solute to exceed its solubility limit and form crystals.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Production of sugar from sugarcane juice, where concentration is increased by vaporization.", "Production of salt from sea water in salterns, where various salts crystallize.", "Obtaining salt by the vaporization or evaporation of a concentrated salt solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='recrystallization'))
    def rule_recrystallization(self):
        """A purification method used to separate pure substances from solid, crystalline substances containing impurities. The process involves dissolving the impure solid in a hot solvent until saturated, filtering the hot solution to remove insoluble impurities, and then cooling the filtrate to obtain pure crystals. It exploits differences in solubility at various temperatures."""
        self.response = {
            'concept': 'Recrystallization',
            'explanation': """A purification method used to separate pure substances from solid, crystalline substances containing impurities. The process involves dissolving the impure solid in a hot solvent until saturated, filtering the hot solution to remove insoluble impurities, and then cooling the filtrate to obtain pure crystals. It exploits differences in solubility at various temperatures.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques / Purification',
            'examples': ["Purifying common salt available in the market by dissolving in hot water, filtering, and cooling.", "Obtaining high quality crystals without impurities from a less pure solid.", "Separating a desired pure solid from other soluble components that remain in solution upon cooling."]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent_extraction__principle_'))
    def rule_solvent_extraction__principle_(self):
        """A separation technique based on the principle that the nature of both the solute and solvent significantly affect solubility. Some solutes exhibit high solubility in one particular solvent while dissolving in very small quantities in another, allowing for selective separation based on this differential solubility."""
        self.response = {
            'concept': 'Solvent Extraction (Principle)',
            'explanation': """A separation technique based on the principle that the nature of both the solute and solvent significantly affect solubility. Some solutes exhibit high solubility in one particular solvent while dissolving in very small quantities in another, allowing for selective separation based on this differential solubility.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating a solute that is highly soluble in an organic solvent but minimally soluble in water.", "Extracting a specific compound from a mixture by dissolving it preferentially in a chosen solvent.", "Utilizing the differing affinities of a substance for various solvents to isolate it."]
        }
        self.halt()

    @Rule(Fact(query_topic='solubility_differences'))
    def rule_solubility_differences(self):
        """The amount of a substance that dissolves can vary greatly depending on the solvent used. Some substances are highly soluble in one solvent but only sparingly soluble in another."""
        self.response = {
            'concept': 'Solubility Differences',
            'explanation': """The amount of a substance that dissolves can vary greatly depending on the solvent used. Some substances are highly soluble in one solvent but only sparingly soluble in another.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["Solid iodine dissolves very little in water, forming a light-coloured solution.", "A larger amount of iodine dissolves in carbon tetrachloride.", "A larger amount of iodine dissolves in cyclohexane."]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent_extraction'))
    def rule_solvent_extraction(self):
        """Solvent extraction is a separation method where a substance is drawn from a solvent in which it is less soluble into another immiscible solvent in which it is more soluble, through direct contact between the two solvents."""
        self.response = {
            'concept': 'Solvent Extraction',
            'explanation': """Solvent extraction is a separation method where a substance is drawn from a solvent in which it is less soluble into another immiscible solvent in which it is more soluble, through direct contact between the two solvents.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Extracting iodine from an aqueous solution into carbon tetrachloride.", "A small volume of carbon tetrachloride can extract iodine from a large volume of aqueous solution.", "Iodine can be recovered by separating the solvent layers and evaporating the carbon tetrachloride."]
        }
        self.halt()

    @Rule(Fact(query_topic='applications_of_solvent_extraction'))
    def rule_applications_of_solvent_extraction(self):
        """Solvent extraction is useful for concentrating substances present in trace amounts, particularly in fields like medicine and pharmaceuticals."""
        self.response = {
            'concept': 'Applications of Solvent Extraction',
            'explanation': """Solvent extraction is useful for concentrating substances present in trace amounts, particularly in fields like medicine and pharmaceuticals.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Separation Techniques',
            'examples': ["Producing medicinal extracts from plants containing trace amounts of components.", "Preparing medicinal solutions of higher concentration using solvents like ethanol.", "Used in the production of medicinal potions."]
        }
        self.halt()

    @Rule(Fact(query_topic='distillation'))
    def rule_distillation(self):
        """Distillation is a separation technique that involves heating a solution or mixture to boil its components into a vapor, and then condensing that vapor back into a liquid to separate them."""
        self.response = {
            'concept': 'Distillation',
            'explanation': """Distillation is a separation technique that involves heating a solution or mixture to boil its components into a vapor, and then condensing that vapor back into a liquid to separate them.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating components by boiling a solution.", "Separating components by boiling a mixture.", "Condensing the vapour after boiling to obtain separated components."]
        }
        self.halt()

    @Rule(Fact(query_topic='liebig_condenser'))
    def rule_liebig_condenser(self):
        """A Liebig condenser is a laboratory apparatus used during distillation to cool and condense the hot vapor produced. It facilitates condensation by circulating cold water around a central tube through which the vapor passes."""
        self.response = {
            'concept': 'Liebig Condenser',
            'explanation': """A Liebig condenser is a laboratory apparatus used during distillation to cool and condense the hot vapor produced. It facilitates condensation by circulating cold water around a central tube through which the vapor passes.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Apparatus',
            'examples': ["Cooling the distillate or vapor that evolves when a mixture is heated.", "Circulating cold water around the vapor path.", "Designed with an inlet and outlet for water circulation."]
        }
        self.halt()

    @Rule(Fact(query_topic='liebig_condenser'))
    def rule_liebig_condenser(self):
        """An apparatus used in the laboratory, particularly in distillation setups, to cool and condense vapor back into liquid. It typically features an outer jacket through which cooling water flows (water in, water out) to facilitate the condensation of vapor passing through its inner tube."""
        self.response = {
            'concept': 'Liebig condenser',
            'explanation': """An apparatus used in the laboratory, particularly in distillation setups, to cool and condense vapor back into liquid. It typically features an outer jacket through which cooling water flows (water in, water out) to facilitate the condensation of vapor passing through its inner tube.""",
            'topic': 'Chemistry',
            'subtopic': 'Distillation Equipment',
            'examples': ["Collecting a sample of distilled water.", "Used as part of a simple distillation apparatus.", "Investigating the construction of an improvised version for laboratory use."]
        }
        self.halt()

    @Rule(Fact(query_topic='simple_distillation'))
    def rule_simple_distillation(self):
        """A separation technique employed for mixtures containing a volatile component and other non-volatile components. During this process, only the volatile components are vaporized and subsequently condensed, while the non-volatile components remain in the original solution. It does not require special control of conditions and can utilize simple equipment like a Liebig condenser."""
        self.response = {
            'concept': 'Simple distillation',
            'explanation': """A separation technique employed for mixtures containing a volatile component and other non-volatile components. During this process, only the volatile components are vaporized and subsequently condensed, while the non-volatile components remain in the original solution. It does not require special control of conditions and can utilize simple equipment like a Liebig condenser.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating water from dissolved salts and gases in well water.", "Obtaining potable water from sea water in some countries.", "Separating a single volatile liquid from a dissolved solid."]
        }
        self.halt()

    @Rule(Fact(query_topic='fractional_distillation'))
    def rule_fractional_distillation(self):
        """A more advanced separation technique required when a solution or mixture contains multiple volatile components. Unlike simple distillation, it cannot be performed with basic simple distillation apparatus and necessitates controlled conditions to effectively separate the various volatile constituents."""
        self.response = {
            'concept': 'Fractional distillation',
            'explanation': """A more advanced separation technique required when a solution or mixture contains multiple volatile components. Unlike simple distillation, it cannot be performed with basic simple distillation apparatus and necessitates controlled conditions to effectively separate the various volatile constituents.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating a mixture that contains several volatile components.", "Used when simple distillation is insufficient for mixtures with multiple volatile liquids.", "Requires specific controlled conditions for effective separation."]
        }
        self.halt()

    @Rule(Fact(query_topic='fractional_distillation_principle'))
    def rule_fractional_distillation_principle(self):
        """Fractional distillation is a separation technique used for mixtures of two or more liquids that have a considerable difference in their boiling points, which implies considerably different volatilities. The vapor formed above such a mixture will contain a higher percentage of the more volatile component (lower boiling point) and a lower percentage of the less volatile component."""
        self.response = {
            'concept': 'Fractional Distillation Principle',
            'explanation': """Fractional distillation is a separation technique used for mixtures of two or more liquids that have a considerable difference in their boiling points, which implies considerably different volatilities. The vapor formed above such a mixture will contain a higher percentage of the more volatile component (lower boiling point) and a lower percentage of the less volatile component.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating two liquids with boiling points of 50 °C and 100 °C.", "A mixture where the vapor is richer in component B (BP 40 °C) than component A (BP 80 °C).", "The necessity for a significant difference in boiling points for effective separation by this method."]
        }
        self.halt()

    @Rule(Fact(query_topic='fractional_distillation_process'))
    def rule_fractional_distillation_process(self):
        """When a mixture of liquids with different boiling points is heated, it begins to boil at a temperature slightly above the boiling point of the most volatile component. The vapor produced is richer in this more volatile component. By collecting and condensing this vapor at a temperature closer to its boiling point, that component can be isolated. As the more volatile component is removed from the mixture, the boiling temperature of the remaining liquid increases, allowing for the sequential separation of other components at different temperatures."""
        self.response = {
            'concept': 'Fractional Distillation Process',
            'explanation': """When a mixture of liquids with different boiling points is heated, it begins to boil at a temperature slightly above the boiling point of the most volatile component. The vapor produced is richer in this more volatile component. By collecting and condensing this vapor at a temperature closer to its boiling point, that component can be isolated. As the more volatile component is removed from the mixture, the boiling temperature of the remaining liquid increases, allowing for the sequential separation of other components at different temperatures.""",
            'topic': 'Chemistry',
            'subtopic': 'Distillation Process',
            'examples': ["A mixture of component A (BP 80 °C) and component B (BP 40 °C) beginning to boil slightly above 40 °C.", "Collecting and condensing vapor at a temperature near 40 °C to obtain a liquid rich in component B.", "The boiling temperature of the mixture increasing as more of component B is removed."]
        }
        self.halt()

    @Rule(Fact(query_topic='industrial_fractional_distillation__crude_oil_refining_'))
    def rule_industrial_fractional_distillation__crude_oil_refining_(self):
        """Fractional distillation is applied industrially to refine crude oil, which is a complex mixture of many hydrocarbon components. A fractionating tower is used to control cooling conditions, with temperature carefully regulated at different levels. Components with lower boiling points rise to and are withdrawn from the upper levels, while components with higher boiling points condense at lower levels or are deposited at the bottom of the tower."""
        self.response = {
            'concept': 'Industrial Fractional Distillation (Crude Oil Refining)',
            'explanation': """Fractional distillation is applied industrially to refine crude oil, which is a complex mixture of many hydrocarbon components. A fractionating tower is used to control cooling conditions, with temperature carefully regulated at different levels. Components with lower boiling points rise to and are withdrawn from the upper levels, while components with higher boiling points condense at lower levels or are deposited at the bottom of the tower.""",
            'topic': 'Chemistry',
            'subtopic': 'Industrial Applications of Distillation',
            'examples': ["Refining crude oil using a fractionating tower to separate its constituent hydrocarbons.", "Components like petroleum gases (lower boiling point) being collected from the upper parts of the tower.", "Bitumen (high boiling point) being deposited at the bottom of the fractionating tower."]
        }
        self.halt()

    @Rule(Fact(query_topic='products_of_crude_oil_fractional_distillation'))
    def rule_products_of_crude_oil_fractional_distillation(self):
        """Fractional distillation of crude oil yields various hydrocarbon fractions, each characterized by a specific boiling point range and common applications. These products are separated at different levels within a fractionating tower based on their volatility and boiling points."""
        self.response = {
            'concept': 'Products of Crude Oil Fractional Distillation',
            'explanation': """Fractional distillation of crude oil yields various hydrocarbon fractions, each characterized by a specific boiling point range and common applications. These products are separated at different levels within a fractionating tower based on their volatility and boiling points.""",
            'topic': 'Chemistry',
            'subtopic': 'Petroleum Products',
            'examples': ["Petroleum gases (refinery gases) with a boiling point around 25 °C, used in gas cylinders.", "Gasoline (petrol) with a boiling point range of 40-75 °C, used as fuel.", "Kerosene with a boiling point range of 150-240 °C, used as jet fuels."]
        }
        self.halt()

    @Rule(Fact(query_topic='petroleum_fractions_and_uses'))
    def rule_petroleum_fractions_and_uses(self):
        """Various fractions obtained from crude oil, likely through a fractionating tower, have distinct boiling points and specific applications in industries such as lubrication, fuel, and construction."""
        self.response = {
            'concept': 'Petroleum Fractions and Uses',
            'explanation': """Various fractions obtained from crude oil, likely through a fractionating tower, have distinct boiling points and specific applications in industries such as lubrication, fuel, and construction.""",
            'topic': 'Chemistry',
            'subtopic': 'Fractional Distillation Products',
            'examples': ["Lubricants (boiling point - 300 °C range)", "Inca oil (fuels for ships, boiling point - 250 °C)", "Bitumen (asphalt) for surfacing roads"]
        }
        self.halt()

    @Rule(Fact(query_topic='fractional_distillation_of_air'))
    def rule_fractional_distillation_of_air(self):
        """Fractional distillation is employed to separate the components of atmospheric air. Air is first pressurized and cooled to approximately -200 °C to liquify it. This liquid mixture is then distilled, allowing components to vaporize at their respective boiling points."""
        self.response = {
            'concept': 'Fractional Distillation of Air',
            'explanation': """Fractional distillation is employed to separate the components of atmospheric air. Air is first pressurized and cooled to approximately -200 °C to liquify it. This liquid mixture is then distilled, allowing components to vaporize at their respective boiling points.""",
            'topic': 'Chemistry',
            'subtopic': 'Fractional Distillation Applications',
            'examples': ["Nitrogen boils off at -196 °C", "Oxygen boils at -183 °C", "Carbon dioxide boils at -78.5 °C"]
        }
        self.halt()

    @Rule(Fact(query_topic='volatile_plant_component_extraction_challenges'))
    def rule_volatile_plant_component_extraction_challenges(self):
        """Certain volatile components found in plants, such as essential oils, are difficult to extract by directly increasing temperature to their boiling points due to the risk of decomposition or conversion into other compounds at high temperatures."""
        self.response = {
            'concept': 'Volatile Plant Component Extraction Challenges',
            'explanation': """Certain volatile components found in plants, such as essential oils, are difficult to extract by directly increasing temperature to their boiling points due to the risk of decomposition or conversion into other compounds at high temperatures.""",
            'topic': 'Chemistry',
            'subtopic': 'Steam Distillation Rationale',
            'examples': ["Cinnamon", "Clove", "Nutmeg"]
        }
        self.halt()

    @Rule(Fact(query_topic='boiling_point_characteristics_of_water_mixtures'))
    def rule_boiling_point_characteristics_of_water_mixtures(self):
        """The boiling point of a mixture containing water depends on the solubility of the other compound. Water-soluble compounds mixed with water result in a mixture boiling above water's boiling point. Conversely, compounds immiscible with water, when mixed with water, form a mixture whose boiling point drops below water's boiling point."""
        self.response = {
            'concept': 'Boiling Point Characteristics of Water Mixtures',
            'explanation': """The boiling point of a mixture containing water depends on the solubility of the other compound. Water-soluble compounds mixed with water result in a mixture boiling above water's boiling point. Conversely, compounds immiscible with water, when mixed with water, form a mixture whose boiling point drops below water's boiling point.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Mixtures',
            'examples': ["Water soluble compounds mixed with water (boiling point > water's BP)", "Essential oils (immiscible) mixed with water (boiling point < water's BP)"]
        }
        self.halt()

    @Rule(Fact(query_topic='steam_distillation_process_for_essential_oils'))
    def rule_steam_distillation_process_for_essential_oils(self):
        """In steam distillation, heat is supplied to a mixture of water and essential oils (which are typically immiscible with water and have boiling points greater than water) by steam. This causes both water and the essential oil to vaporize together as a mixture of vapors at a temperature below the boiling point of water (100 °C). Upon cooling, the distillate separates into two distinct liquid layers."""
        self.response = {
            'concept': 'Steam Distillation Process for Essential Oils',
            'explanation': """In steam distillation, heat is supplied to a mixture of water and essential oils (which are typically immiscible with water and have boiling points greater than water) by steam. This causes both water and the essential oil to vaporize together as a mixture of vapors at a temperature below the boiling point of water (100 °C). Upon cooling, the distillate separates into two distinct liquid layers.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Steam heating cinnamon leaves with water", "Liberation of water and essential oil as a vapor mixture below 100 °C", "Separation of the cooled distillate into two layers"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_essential_oils'))
    def rule_uses_of_essential_oils(self):
        """Essential oils are versatile substances with numerous applications across various industries. They are primarily utilized as flavors and condiments in food products, as key ingredients in the production of perfumes, incorporated into personal care items such as toothpaste, and also employed in the manufacturing of pharmaceuticals."""
        self.response = {
            'concept': 'Uses of Essential Oils',
            'explanation': """Essential oils are versatile substances with numerous applications across various industries. They are primarily utilized as flavors and condiments in food products, as key ingredients in the production of perfumes, incorporated into personal care items such as toothpaste, and also employed in the manufacturing of pharmaceuticals.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Substances',
            'examples': ["Used as flavours and condiments in food", "Used to produce perfumes", "Used as ingredients in toothpaste"]
        }
        self.halt()

    @Rule(Fact(query_topic='chromatography'))
    def rule_chromatography(self):
        """Chromatography is a powerful analytical technique used to separate and identify the individual components present within a mixture. It can be applied to both solid and liquid mixtures, particularly those containing non-volatile components. This broad category encompasses many different types of chromatographic methods."""
        self.response = {
            'concept': 'Chromatography',
            'explanation': """Chromatography is a powerful analytical technique used to separate and identify the individual components present within a mixture. It can be applied to both solid and liquid mixtures, particularly those containing non-volatile components. This broad category encompasses many different types of chromatographic methods.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating pigments in a dye", "Identifying components in a plant extract", "Analyzing different substances in a liquid sample"]
        }
        self.halt()

    @Rule(Fact(query_topic='paper_chromatography'))
    def rule_paper_chromatography(self):
        """Paper chromatography is a specific type of chromatography where the separation process is conducted using a strip of paper, typically made of cellulose, as the stationary phase."""
        self.response = {
            'concept': 'Paper Chromatography',
            'explanation': """Paper chromatography is a specific type of chromatography where the separation process is conducted using a strip of paper, typically made of cellulose, as the stationary phase.""",
            'topic': 'Chemistry',
            'subtopic': 'Chromatography',
            'examples': ["Separating different colors in ink", "Analyzing amino acids in a solution using filter paper", "Separating plant dyes extracted from leaves"]
        }
        self.halt()

    @Rule(Fact(query_topic='stationary_phase__chromatography_'))
    def rule_stationary_phase__chromatography_(self):
        """In chromatography, the stationary phase refers to the immobile medium through which the mixture's components travel. Its physical and chemical properties are crucial as it interacts differently with the components of the mixture, influencing their movement and separation."""
        self.response = {
            'concept': 'Stationary Phase (Chromatography)',
            'explanation': """In chromatography, the stationary phase refers to the immobile medium through which the mixture's components travel. Its physical and chemical properties are crucial as it interacts differently with the components of the mixture, influencing their movement and separation.""",
            'topic': 'Chemistry',
            'subtopic': 'Chromatography',
            'examples': ["A strip of filter paper in paper chromatography", "Silica gel in thin-layer chromatography", "A packed column in gas chromatography"]
        }
        self.halt()

    @Rule(Fact(query_topic='mobile_phase__chromatography_'))
    def rule_mobile_phase__chromatography_(self):
        """The mobile phase in chromatography is the solvent or liquid that flows through the stationary phase, carrying the components of the mixture with it. Components dissolve in this phase and are transported at varying speeds based on their interactions with both the mobile and stationary phases."""
        self.response = {
            'concept': 'Mobile Phase (Chromatography)',
            'explanation': """The mobile phase in chromatography is the solvent or liquid that flows through the stationary phase, carrying the components of the mixture with it. Components dissolve in this phase and are transported at varying speeds based on their interactions with both the mobile and stationary phases.""",
            'topic': 'Chemistry',
            'subtopic': 'Chromatography',
            'examples': ["Water soaked into filter paper", "Acetone used to dissolve and carry components", "Ethyl alcohol flowing through a separation medium"]
        }
        self.halt()

    @Rule(Fact(query_topic='principle_of_separation_in_chromatography'))
    def rule_principle_of_separation_in_chromatography(self):
        """The separation of components in chromatography is achieved due to differences in their rates of upward movement. This movement depends on the varying strengths of attraction or affinity each component has for the stationary phase. Components strongly attracted to the stationary phase move slower, while those less attracted move faster, leading to their effective separation."""
        self.response = {
            'concept': 'Principle of Separation in Chromatography',
            'explanation': """The separation of components in chromatography is achieved due to differences in their rates of upward movement. This movement depends on the varying strengths of attraction or affinity each component has for the stationary phase. Components strongly attracted to the stationary phase move slower, while those less attracted move faster, leading to their effective separation.""",
            'topic': 'Chemistry',
            'subtopic': 'Chromatography',
            'examples': ["A component strongly binding to the paper moves slowly", "A component less attracted to the paper moves faster", "Different speeds of movement leading to distinct bands of separated substances"]
        }
        self.halt()

    @Rule(Fact(query_topic='paper_chromatography'))
    def rule_paper_chromatography(self):
        """A chromatographic technique used to separate and identify several components when they are mixed together. This method involves a stationary phase (e.g., a paper strip) and a mobile phase (a solvent) which moves through the stationary phase, carrying the mixture's components at different rates, leading to their separation based on their affinities."""
        self.response = {
            'concept': 'Paper Chromatography',
            'explanation': """A chromatographic technique used to separate and identify several components when they are mixed together. This method involves a stationary phase (e.g., a paper strip) and a mobile phase (a solvent) which moves through the stationary phase, carrying the mixture's components at different rates, leading to their separation based on their affinities.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating the components in a chlorophyll mixture.", "Finding whether poisonous chemicals are mixed with water.", "Checking whether harmful substances are associated with food items."]
        }
        self.halt()

    @Rule(Fact(query_topic='chlorophyll_mixture_separation_by_paper_chromatography_procedure'))
    def rule_chlorophyll_mixture_separation_by_paper_chromatography_procedure(self):
        """A specific experimental procedure for separating the various colored components within a chlorophyll mixture using paper chromatography. The method involves crushing spinach leaves to extract chlorophyll, applying this extract as a spot on a chromatography paper strip, and then suspending the strip in a sealed boiling tube containing a solvent (e.g., acetone, kerosene, or petrol). As the solvent ascends the paper, it separates the chlorophyll's different components, which become visible as distinct colored bands."""
        self.response = {
            'concept': 'Chlorophyll Mixture Separation by Paper Chromatography Procedure',
            'explanation': """A specific experimental procedure for separating the various colored components within a chlorophyll mixture using paper chromatography. The method involves crushing spinach leaves to extract chlorophyll, applying this extract as a spot on a chromatography paper strip, and then suspending the strip in a sealed boiling tube containing a solvent (e.g., acetone, kerosene, or petrol). As the solvent ascends the paper, it separates the chlorophyll's different components, which become visible as distinct colored bands.""",
            'topic': 'Chemistry',
            'subtopic': 'Chromatography Applications',
            'examples': ["Crushing spinach leaves thoroughly using a mortar and pestle to prepare chlorophyll extract.", "Placing drops of chlorophyll extract onto a chromatography paper strip using a capillary tube.", "Suspending the paper strip in solvents like acetone, kerosene, or petrol in a boiling tube to allow separation."]
        }
        self.halt()

    @Rule(Fact(query_topic='extraction_of_salt_from_sea_water_in_salterns'))
    def rule_extraction_of_salt_from_sea_water_in_salterns(self):
        """In Sri Lanka, salt is produced by collecting sea water in salt pans within salterns and concentrating it through evaporation. This process uses evaporation and crystallization techniques to cause salt to crystallize out."""
        self.response = {
            'concept': 'Extraction of Salt from Sea Water in Salterns',
            'explanation': """In Sri Lanka, salt is produced by collecting sea water in salt pans within salterns and concentrating it through evaporation. This process uses evaporation and crystallization techniques to cause salt to crystallize out.""",
            'topic': 'Chemistry',
            'subtopic': 'Separating Techniques / Industrial Processes',
            'examples': ["Evaporation of sea water in salterns", "Crystallization of salt from concentrated brine", "Production of edible salt from ocean water"]
        }
        self.halt()

    @Rule(Fact(query_topic='geographical_and_environmental_factors_for_saltern_location'))
    def rule_geographical_and_environmental_factors_for_saltern_location(self):
        """When establishing a saltern, several geographical and environmental factors must be considered: a flat land close to a coastal area for easy sea water access, clayey soil to minimize water percolation, a dry and hot climate with bright sunlight and consistent wind throughout the year, and an area with minimal rainfall."""
        self.response = {
            'concept': 'Geographical and Environmental Factors for Saltern Location',
            'explanation': """When establishing a saltern, several geographical and environmental factors must be considered: a flat land close to a coastal area for easy sea water access, clayey soil to minimize water percolation, a dry and hot climate with bright sunlight and consistent wind throughout the year, and an area with minimal rainfall.""",
            'topic': 'Chemistry',
            'subtopic': 'Industrial Site Selection / Saltern Design',
            'examples': ["Flat land near a coastal area", "Presence of clayey soil", "Dry and hot climate with sunlight and wind"]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_tanks_in_a_saltern_structure'))
    def rule_types_of_tanks_in_a_saltern_structure(self):
        """The structure of a saltern typically comprises three main types of tanks, each designed for specific stages of the salt production process: large, shallow tanks; medium tanks; and small tanks."""
        self.response = {
            'concept': 'Types of Tanks in a Saltern Structure',
            'explanation': """The structure of a saltern typically comprises three main types of tanks, each designed for specific stages of the salt production process: large, shallow tanks; medium tanks; and small tanks.""",
            'topic': 'Chemistry',
            'subtopic': 'Saltern Structure / Industrial Equipment',
            'examples': ["Large, shallow tanks for initial evaporation", "Medium tanks for intermediate concentration", "Small tanks for final salt crystallization"]
        }
        self.halt()

    @Rule(Fact(query_topic='saltern_production_step_1__initial_evaporation_and_calcium_carbonate_precipitation'))
    def rule_saltern_production_step_1__initial_evaporation_and_calcium_carbonate_precipitation(self):
        """In the first step, sea water is either flooded or pumped into large, shallow tanks and allowed to evaporate by sunlight. When the concentration of the sea water reaches twice its initial level, calcium carbonate (CaCO3) begins to crystallize and precipitate at the bottom of the tank."""
        self.response = {
            'concept': 'Saltern Production Step 1: Initial Evaporation and Calcium Carbonate Precipitation',
            'explanation': """In the first step, sea water is either flooded or pumped into large, shallow tanks and allowed to evaporate by sunlight. When the concentration of the sea water reaches twice its initial level, calcium carbonate (CaCO3) begins to crystallize and precipitate at the bottom of the tank.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Production Process',
            'examples': ["Sea water entering large, shallow tanks", "Evaporation to double the initial concentration", "Precipitation of calcium carbonate (CaCO3)"]
        }
        self.halt()

    @Rule(Fact(query_topic='saltern_production_step_2__further_evaporation_and_calcium_sulphate_crystallization'))
    def rule_saltern_production_step_2__further_evaporation_and_calcium_sulphate_crystallization(self):
        """Following Step 1, the water is transferred into medium-sized tanks where further evaporation occurs. When the water concentration becomes approximately four times the initial sea water concentration, calcium sulphate (CaSO4) crystallizes and settles at the bottom of these tanks."""
        self.response = {
            'concept': 'Saltern Production Step 2: Further Evaporation and Calcium Sulphate Crystallization',
            'explanation': """Following Step 1, the water is transferred into medium-sized tanks where further evaporation occurs. When the water concentration becomes approximately four times the initial sea water concentration, calcium sulphate (CaSO4) crystallizes and settles at the bottom of these tanks.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Production Process',
            'examples': ["Transferring water to medium tanks", "Evaporation to quadruple the initial concentration", "Crystallization of calcium sulphate (CaSO4)"]
        }
        self.halt()

    @Rule(Fact(query_topic='saltern_production_step_3__final_evaporation_and_sodium_chloride_crystallization'))
    def rule_saltern_production_step_3__final_evaporation_and_sodium_chloride_crystallization(self):
        """After the precipitation of calcium sulphate, the remaining solution flows from the medium tanks into the smaller tanks. Here, water is evaporated even further until the concentration reaches nearly ten times the initial sea water concentration, at which point salt (NaCl) crystallizes and precipitates."""
        self.response = {
            'concept': 'Saltern Production Step 3: Final Evaporation and Sodium Chloride Crystallization',
            'explanation': """After the precipitation of calcium sulphate, the remaining solution flows from the medium tanks into the smaller tanks. Here, water is evaporated even further until the concentration reaches nearly ten times the initial sea water concentration, at which point salt (NaCl) crystallizes and precipitates.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Production Process',
            'examples': ["Solution flowing into smaller tanks", "Evaporation to ten times the initial concentration", "Crystallization of sodium chloride (NaCl)"]
        }
        self.halt()

    @Rule(Fact(query_topic='impurities_in_salt'))
    def rule_impurities_in_salt(self):
        """Even before the complete precipitation of sodium chloride, magnesium chloride (MgCl2) and magnesium sulphate (MgSO4) begin to precipitate. These compounds give a bitter taste to salt and make it hygroscopic and deliquescent when exposed to the atmosphere."""
        self.response = {
            'concept': 'Impurities in Salt',
            'explanation': """Even before the complete precipitation of sodium chloride, magnesium chloride (MgCl2) and magnesium sulphate (MgSO4) begin to precipitate. These compounds give a bitter taste to salt and make it hygroscopic and deliquescent when exposed to the atmosphere.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Production',
            'examples': ["Magnesium chloride (MgCl2)", "Magnesium sulphate (MgSO4)"]
        }
        self.halt()

    @Rule(Fact(query_topic='mother_liquor__bittern_'))
    def rule_mother_liquor__bittern_(self):
        """The solution left after the precipitation of salt, specifically sodium chloride and other impurities like magnesium chloride and sulphate, is known as mother liquor or bittern."""
        self.response = {
            'concept': 'Mother Liquor (Bittern)',
            'explanation': """The solution left after the precipitation of salt, specifically sodium chloride and other impurities like magnesium chloride and sulphate, is known as mother liquor or bittern.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Production',
            'examples': ["Solution remaining after salt precipitation", "Bittern"]
        }
        self.halt()

    @Rule(Fact(query_topic='purification_of_stored_salt'))
    def rule_purification_of_stored_salt(self):
        """Pure sodium chloride is not hygroscopic, but the presence of magnesium chloride and magnesium sulphate makes it bitter, hygroscopic, and deliquescent. Over a period of about six months of storage, these magnesium compounds absorb atmospheric moisture, dissolve, and are mostly removed, leaving the salt as a solid."""
        self.response = {
            'concept': 'Purification of Stored Salt',
            'explanation': """Pure sodium chloride is not hygroscopic, but the presence of magnesium chloride and magnesium sulphate makes it bitter, hygroscopic, and deliquescent. Over a period of about six months of storage, these magnesium compounds absorb atmospheric moisture, dissolve, and are mostly removed, leaving the salt as a solid.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Purification',
            'examples': ["Storing salt for six months", "Magnesium chloride absorbing moisture", "Magnesium sulphate going into solution"]
        }
        self.halt()

    @Rule(Fact(query_topic='essential_oils'))
    def rule_essential_oils(self):
        """Volatile compounds obtained from plant materials that are responsible for the characteristic aroma of some plants. These are extracted using techniques such as steam distillation and solvent extraction."""
        self.response = {
            'concept': 'Essential Oils',
            'explanation': """Volatile compounds obtained from plant materials that are responsible for the characteristic aroma of some plants. These are extracted using techniques such as steam distillation and solvent extraction.""",
            'topic': 'Chemistry',
            'subtopic': 'Natural Products',
            'examples': ["Cinnamon leaf oil", "Citronella oil", "Eucalyptus oil"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_essential_oils'))
    def rule_uses_of_essential_oils(self):
        """Essential oils serve various purposes, including promoting food flavor and scent, and possessing medicinal properties. They are frequently used in medicinal ointments, toothpaste, and perfumes for soap."""
        self.response = {
            'concept': 'Uses of Essential Oils',
            'explanation': """Essential oils serve various purposes, including promoting food flavor and scent, and possessing medicinal properties. They are frequently used in medicinal ointments, toothpaste, and perfumes for soap.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Natural Products',
            'examples': ["Promote food flavour (e.g., pepper oil)", "Used in medicinal ointments (e.g., cinnamon leaf oil)", "Perfumes added to soap (e.g., cardamom oil)"]
        }
        self.halt()

    @Rule(Fact(query_topic='plant_sources_of_essential_oils'))
    def rule_plant_sources_of_essential_oils(self):
        """Essential oils are formed in and extracted from various parts of plants, depending on the specific plant species."""
        self.response = {
            'concept': 'Plant Sources of Essential Oils',
            'explanation': """Essential oils are formed in and extracted from various parts of plants, depending on the specific plant species.""",
            'topic': 'Chemistry',
            'subtopic': 'Sources of Natural Products',
            'examples': ["Roots (e.g., Vetiveria)", "Bark (e.g., Cinnamon)", "Leaves (e.g., Citronella)"]
        }
        self.halt()

    @Rule(Fact(query_topic='steam_distillation'))
    def rule_steam_distillation(self):
        """A method used to extract essential oils from plant parts. Steam, generated from a steam bath, is passed through the plant material. The essential oils, being mixed with water vapor, vaporize at a temperature below 100 °C. This mixture of vapors is then condensed, yielding immiscible essential oil and water, which can be obtained separately."""
        self.response = {
            'concept': 'Steam Distillation',
            'explanation': """A method used to extract essential oils from plant parts. Steam, generated from a steam bath, is passed through the plant material. The essential oils, being mixed with water vapor, vaporize at a temperature below 100 °C. This mixture of vapors is then condensed, yielding immiscible essential oil and water, which can be obtained separately.""",
            'topic': 'Chemistry',
            'subtopic': 'Essential Oil Extraction',
            'examples': ["Obtaining oil from cinnamon leaves by passing steam through them.", "Separating essential oils from lavender flowers.", "Distilling rose petals to obtain rose oil."]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent_extraction__essential_oils_'))
    def rule_solvent_extraction__essential_oils_(self):
        """A method for extracting essential oils using organic solvents such as ether, chloroform, or toluene. When plant parts are shaken with the solvent, the essential oil dissolves in it. The essential oil is then separated by letting the solvent vaporize."""
        self.response = {
            'concept': 'Solvent Extraction (Essential Oils)',
            'explanation': """A method for extracting essential oils using organic solvents such as ether, chloroform, or toluene. When plant parts are shaken with the solvent, the essential oil dissolves in it. The essential oil is then separated by letting the solvent vaporize.""",
            'topic': 'Chemistry',
            'subtopic': 'Essential Oil Extraction',
            'examples': ["Using ether to dissolve essential oils from flower petals.", "Shaking plant parts with chloroform to extract essential oils.", "Separating essential oil from a toluene solution by evaporation."]
        }
        self.halt()

    @Rule(Fact(query_topic='compression__volatile_oil_extraction_'))
    def rule_compression__volatile_oil_extraction_(self):
        """A method where volatile oils in some plant parts can be obtained by compressing them under a suitable pressure."""
        self.response = {
            'concept': 'Compression (Volatile Oil Extraction)',
            'explanation': """A method where volatile oils in some plant parts can be obtained by compressing them under a suitable pressure.""",
            'topic': 'Chemistry',
            'subtopic': 'Essential Oil Extraction',
            'examples': ["Extracting citrus oils from fruit peels by pressing.", "Obtaining oil from seeds by applying mechanical pressure."]
        }
        self.halt()

    @Rule(Fact(query_topic='matter_classification'))
    def rule_matter_classification(self):
        """Matter can be divided into two main parts: pure substances and mixtures. In the natural environment, pure substances are very rare, while mixtures are more abundant."""
        self.response = {
            'concept': 'Matter Classification',
            'explanation': """Matter can be divided into two main parts: pure substances and mixtures. In the natural environment, pure substances are very rare, while mixtures are more abundant.""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Concepts',
            'examples': ["Water (H2O) as a pure substance.", "Air as a mixture of gases.", "Saltwater as a mixture."]
        }
        self.halt()

    @Rule(Fact(query_topic='mixture'))
    def rule_mixture(self):
        """Substances formed by mixing two or more substances without any chemical changes. The physical and chemical properties of the components are retained even in the mixture, and its components can be separated by physical methods."""
        self.response = {
            'concept': 'Mixture',
            'explanation': """Substances formed by mixing two or more substances without any chemical changes. The physical and chemical properties of the components are retained even in the mixture, and its components can be separated by physical methods.""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Concepts',
            'examples': ["Sand and iron filings mixed together.", "Air (a mixture of nitrogen, oxygen, etc.).", "Sugar dissolved in water."]
        }
        self.halt()

    @Rule(Fact(query_topic='homogeneous_mixture__solution_'))
    def rule_homogeneous_mixture__solution_(self):
        """A mixture in which its components are uniformly distributed. It is also referred to as a solution. Characteristics such as concentration, color, density, and transparency of any minute part of a solution are identical."""
        self.response = {
            'concept': 'Homogeneous Mixture (Solution)',
            'explanation': """A mixture in which its components are uniformly distributed. It is also referred to as a solution. Characteristics such as concentration, color, density, and transparency of any minute part of a solution are identical.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Salt dissolved completely in water.", "Air, which is a uniform mixture of gases.", "Sugar water."]
        }
        self.halt()

    @Rule(Fact(query_topic='heterogeneous_mixture'))
    def rule_heterogeneous_mixture(self):
        """A mixture where its components are not uniformly distributed. In heterogeneous mixtures, characteristics such as concentration, color, density, and transparency are different across various parts."""
        self.response = {
            'concept': 'Heterogeneous Mixture',
            'explanation': """A mixture where its components are not uniformly distributed. In heterogeneous mixtures, characteristics such as concentration, color, density, and transparency are different across various parts.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Sand mixed with water.", "Oil and water not mixed.", "A salad with different vegetables."]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent'))
    def rule_solvent(self):
        """In a solution, the component that is present in a greater proportion is called the solvent."""
        self.response = {
            'concept': 'Solvent',
            'explanation': """In a solution, the component that is present in a greater proportion is called the solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Water in a saltwater solution.", "Nitrogen in the air (as the largest component).", "Ethanol in a dilute alcoholic solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='solute_definition'))
    def rule_solute_definition(self):
        """The component within a mixture that is present in a proportionally smaller quantity is defined as the solute."""
        self.response = {
            'concept': 'Solute Definition',
            'explanation': """The component within a mixture that is present in a proportionally smaller quantity is defined as the solute.""",
            'topic': 'Chemistry',
            'subtopic': 'Mixtures',
            'examples': ["Sugar in a cup of tea", "Salt dissolved in water", "Oxygen in the air we breathe (as a component of a gaseous mixture)"]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_dissolving_solubility'))
    def rule_factors_affecting_dissolving_solubility(self):
        """The process by which a solute dissolves in a solvent is dependent on several factors, including temperature, the polar characteristics stemming from the molecular properties of both the solute and solvent, and their respective organic or inorganic nature."""
        self.response = {
            'concept': 'Factors Affecting Dissolving/Solubility',
            'explanation': """The process by which a solute dissolves in a solvent is dependent on several factors, including temperature, the polar characteristics stemming from the molecular properties of both the solute and solvent, and their respective organic or inorganic nature.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["Sugar dissolves more quickly in hot water than cold water", "Oil (nonpolar) does not dissolve in water (polar)", "Ethanol (polar) readily dissolves in water (polar)"]
        }
        self.halt()

    @Rule(Fact(query_topic='gas_solubility_in_water'))
    def rule_gas_solubility_in_water(self):
        """The extent to which a gas can dissolve in water is directly influenced by the pressure of that gas exerted over the water's surface and the temperature of the water."""
        self.response = {
            'concept': 'Gas Solubility in Water',
            'explanation': """The extent to which a gas can dissolve in water is directly influenced by the pressure of that gas exerted over the water's surface and the temperature of the water.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["Carbon dioxide gas is more soluble in soda under higher pressure", "A warm carbonated drink loses its fizziness faster than a cold one", "Less oxygen is dissolved in warmer lake water, affecting aquatic life"]
        }
        self.halt()

    @Rule(Fact(query_topic='notations_for_mixture_composition'))
    def rule_notations_for_mixture_composition(self):
        """Various standardized notations are utilized to quantitatively express the composition of a mixture. These include mass fraction (m/m), volume fraction (V/V), mole fraction, mass-volume ratio (m/V), and mole-volume ratio (n/V)."""
        self.response = {
            'concept': 'Notations for Mixture Composition',
            'explanation': """Various standardized notations are utilized to quantitatively express the composition of a mixture. These include mass fraction (m/m), volume fraction (V/V), mole fraction, mass-volume ratio (m/V), and mole-volume ratio (n/V).""",
            'topic': 'Chemistry',
            'subtopic': 'Mixture Quantification',
            'examples': ["Calculating the mass fraction of salt in a saline solution", "Stating the volume fraction of alcohol in a hand sanitizer", "Determining the mole fraction of nitrogen in atmospheric air"]
        }
        self.halt()

    @Rule(Fact(query_topic='concentration__mole_volume_ratio_'))
    def rule_concentration__mole_volume_ratio_(self):
        """Among the different notations for mixture composition, the mole-volume ratio (n/V) is specifically known as the concentration. Its standard units are mol dm-3 (moles per cubic decimetre)."""
        self.response = {
            'concept': 'Concentration (Mole-Volume Ratio)',
            'explanation': """Among the different notations for mixture composition, the mole-volume ratio (n/V) is specifically known as the concentration. Its standard units are mol dm-3 (moles per cubic decimetre).""",
            'topic': 'Chemistry',
            'subtopic': 'Mixture Quantification',
            'examples': ["A solution described as having a 1 mol dm-3 concentration of sodium chloride", "Preparing a 0.5 mol dm-3 acid solution for an experiment", "Measuring the concentration of a pollutant in water in mol dm-3"]
        }
        self.halt()

    @Rule(Fact(query_topic='preparation_of_solutes'))
    def rule_preparation_of_solutes(self):
        """For numerous applications in daily life and scientific tasks, it is necessary to prepare solutes with a precisely known composition, often requiring the use of various specialized laboratory apparatus."""
        self.response = {
            'concept': 'Preparation of Solutes',
            'explanation': """For numerous applications in daily life and scientific tasks, it is necessary to prepare solutes with a precisely known composition, often requiring the use of various specialized laboratory apparatus.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Techniques',
            'examples': ["Preparing a standard solution for titrimetric analysis", "Diluting a stock solution to a specific working concentration", "Formulating a chemical reagent with a defined molarity"]
        }
        self.halt()

    @Rule(Fact(query_topic='mixture_component_separation'))
    def rule_mixture_component_separation(self):
        """The individual components within mixtures are routinely separated in both everyday life scenarios and industrial processes, employing a diverse array of methodologies."""
        self.response = {
            'concept': 'Mixture Component Separation',
            'explanation': """The individual components within mixtures are routinely separated in both everyday life scenarios and industrial processes, employing a diverse array of methodologies.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating different types of grains after harvest", "Refining crude oil into various petroleum products", "Extracting a desired metal from its ore"]
        }
        self.halt()

    @Rule(Fact(query_topic='separation_by_density_or_size_difference'))
    def rule_separation_by_density_or_size_difference(self):
        """Methods such as sifting, flatting, and winnowing achieve component separation by exploiting differences in their densities. Conversely, sieving and filtration separate components based on disparities in the size of their particles."""
        self.response = {
            'concept': 'Separation by Density or Size Difference',
            'explanation': """Methods such as sifting, flatting, and winnowing achieve component separation by exploiting differences in their densities. Conversely, sieving and filtration separate components based on disparities in the size of their particles.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Winnowing rice to separate the lighter chaff from the heavier grains", "Sieving flour to remove larger clumps or impurities", "Filtering coffee grounds from brewed coffee using a filter paper"]
        }
        self.halt()

    @Rule(Fact(query_topic='separation_by_boiling_point__vaporization_'))
    def rule_separation_by_boiling_point__vaporization_(self):
        """Components within a mixture can be effectively separated through the process of vaporization, which leverages the distinct differences in their individual boiling points."""
        self.response = {
            'concept': 'Separation by Boiling Point (Vaporization)',
            'explanation': """Components within a mixture can be effectively separated through the process of vaporization, which leverages the distinct differences in their individual boiling points.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Distilling water from a salt solution to obtain pure water", "Separating ethanol from water in an alcoholic mixture", "Fractional distillation of crude oil to yield different fuel types"]
        }
        self.halt()

    @Rule(Fact(query_topic='crystallization_and_recrystallization'))
    def rule_crystallization_and_recrystallization(self):
        """Crystallization and recrystallization are processes that involve adjusting the concentration of a solution to surpass its saturated concentration, leading to the formation of solid crystals."""
        self.response = {
            'concept': 'Crystallization and Recrystallization',
            'explanation': """Crystallization and recrystallization are processes that involve adjusting the concentration of a solution to surpass its saturated concentration, leading to the formation of solid crystals.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Growing rock candy crystals from a supersaturated sugar solution", "Purifying an impure solid compound by recrystallizing it from a suitable solvent", "Forming salt crystals by allowing seawater to evaporate"]
        }
        self.halt()

    @Rule(Fact(query_topic='differential_solubility'))
    def rule_differential_solubility(self):
        """Certain substances exhibit a higher degree of solubility in one particular solvent while demonstrating a lower solubility in another solvent."""
        self.response = {
            'concept': 'Differential Solubility',
            'explanation': """Certain substances exhibit a higher degree of solubility in one particular solvent while demonstrating a lower solubility in another solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solubility',
            'examples': ["Iodine dissolves readily in alcohol but sparingly in water", "Grease dissolves well in organic solvents like hexane but not in water", "Table salt dissolves easily in water but is insoluble in oil"]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent_extraction'))
    def rule_solvent_extraction(self):
        """In solvent extraction, a solute that is dissolved in a smaller quantity in one solvent is selectively transferred into a second solvent, provided that the solute is more soluble in the second solvent and the two solvents are immiscible."""
        self.response = {
            'concept': 'Solvent Extraction',
            'explanation': """In solvent extraction, a solute that is dissolved in a smaller quantity in one solvent is selectively transferred into a second solvent, provided that the solute is more soluble in the second solvent and the two solvents are immiscible.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Extracting caffeine from coffee beans using an organic solvent", "Separating an organic product from an aqueous reaction mixture", "Removing iodine from an aqueous solution into a nonpolar solvent like tetrachloromethane"]
        }
        self.halt()

    @Rule(Fact(query_topic='distillation__component_collection_'))
    def rule_distillation__component_collection_(self):
        """During the separation of components by distillation, the mixture is heated. Components that vaporize at their respective boiling points are removed from the main mixture and subsequently collected at a separate location by cooling them back into a liquid state."""
        self.response = {
            'concept': 'Distillation (Component Collection)',
            'explanation': """During the separation of components by distillation, the mixture is heated. Components that vaporize at their respective boiling points are removed from the main mixture and subsequently collected at a separate location by cooling them back into a liquid state.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating water from impurities by boiling and condensing the steam", "Fractional distillation to separate different components of crude oil based on their boiling points", "Obtaining pure ethanol from a fermented mixture by heating and collecting the vapor"]
        }
        self.halt()

    @Rule(Fact(query_topic='distillation_modes'))
    def rule_distillation_modes(self):
        """Distillation, a separation technique, can be divided into distinct modes based on the specific techniques utilized and the inherent properties of the components being separated."""
        self.response = {
            'concept': 'Distillation Modes',
            'explanation': """Distillation, a separation technique, can be divided into distinct modes based on the specific techniques utilized and the inherent properties of the components being separated.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Simple distillation", "Fractional distillation", "Steam distillation"]
        }
        self.halt()

    @Rule(Fact(query_topic='paper_chromatography'))
    def rule_paper_chromatography(self):
        """Paper chromatography is a separation method where a volatile solvent passes through a mixture applied as a drop on special paper. Components are separated from one another due to differences in their speed of travel through the paper, which in turn is caused by varying strengths of attraction of the components to the paper (cellulose)."""
        self.response = {
            'concept': 'Paper Chromatography',
            'explanation': """Paper chromatography is a separation method where a volatile solvent passes through a mixture applied as a drop on special paper. Components are separated from one another due to differences in their speed of travel through the paper, which in turn is caused by varying strengths of attraction of the components to the paper (cellulose).""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating components of an ink mixture", "Separating different dyes", "Analyzing plant pigments"]
        }
        self.halt()

    @Rule(Fact(query_topic='mixtures'))
    def rule_mixtures(self):
        """A substance containing two or more different substances that are physically combined but not chemically bonded, and which retain their individual properties."""
        self.response = {
            'concept': 'Mixtures',
            'explanation': """A substance containing two or more different substances that are physically combined but not chemically bonded, and which retain their individual properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Concepts',
            'examples': ["Mixture of salt water", "Mixture of ethanol and water", "Mixture of copper sulphate and water"]
        }
        self.halt()

    @Rule(Fact(query_topic='homogeneous_mixture'))
    def rule_homogeneous_mixture(self):
        """A mixture in which the composition is uniform throughout, meaning the components are evenly distributed and indistinguishable from one another."""
        self.response = {
            'concept': 'Homogeneous Mixture',
            'explanation': """A mixture in which the composition is uniform throughout, meaning the components are evenly distributed and indistinguishable from one another.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Salt dissolved in water (salt water)", "Ethanol mixed with water", "Acetic acid dissolved in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='heterogeneous_mixture'))
    def rule_heterogeneous_mixture(self):
        """A mixture in which the composition is not uniform throughout, and the components are not evenly distributed and can often be visually distinguished."""
        self.response = {
            'concept': 'Heterogeneous Mixture',
            'explanation': """A mixture in which the composition is not uniform throughout, and the components are not evenly distributed and can often be visually distinguished.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Mixtures',
            'examples': ["Oil and water", "Sand and iron filings", "Suspension of mud in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_a_mixture'))
    def rule_components_of_a_mixture(self):
        """The individual substances or constituents that combine to form a mixture."""
        self.response = {
            'concept': 'Components of a Mixture',
            'explanation': """The individual substances or constituents that combine to form a mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Concepts',
            'examples': ["Salt and water are components of salt water", "Ethanol and water are components of an ethanol-water mixture"]
        }
        self.halt()

    @Rule(Fact(query_topic='solution'))
    def rule_solution(self):
        """A homogeneous mixture consisting of a solute dissolved into a solvent."""
        self.response = {
            'concept': 'Solution',
            'explanation': """A homogeneous mixture consisting of a solute dissolved into a solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["A solution of salt in water", "A solution of acetic acid in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent'))
    def rule_solvent(self):
        """The substance in a solution that dissolves the solute, typically present in a larger quantity."""
        self.response = {
            'concept': 'Solvent',
            'explanation': """The substance in a solution that dissolves the solute, typically present in a larger quantity.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Water as a solvent for salt", "Ethanol as a solvent for iodine"]
        }
        self.halt()

    @Rule(Fact(query_topic='solute'))
    def rule_solute(self):
        """The substance in a solution that is dissolved in the solvent, typically present in a smaller quantity."""
        self.response = {
            'concept': 'Solute',
            'explanation': """The substance in a solution that is dissolved in the solvent, typically present in a smaller quantity.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Salt as the solute in salt water", "Iodine as the solute in organic solvents"]
        }
        self.halt()

    @Rule(Fact(query_topic='solubility'))
    def rule_solubility(self):
        """The property of a solid, liquid, or gaseous chemical substance to dissolve in a solvent to form a homogeneous solution. It quantifies the maximum amount of solute that can dissolve in a given amount of solvent at a specific temperature and pressure."""
        self.response = {
            'concept': 'Solubility',
            'explanation': """The property of a solid, liquid, or gaseous chemical substance to dissolve in a solvent to form a homogeneous solution. It quantifies the maximum amount of solute that can dissolve in a given amount of solvent at a specific temperature and pressure.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Solubility of CaCO3, CaSO4, NaCl, MgCl2 (from Q10)", "Iodine's insolubility in water and solubility in other solvents"]
        }
        self.halt()

    @Rule(Fact(query_topic='organic_solvents'))
    def rule_organic_solvents(self):
        """Solvents that are organic compounds, meaning they are carbon-based and often contain hydrogen atoms."""
        self.response = {
            'concept': 'Organic Solvents',
            'explanation': """Solvents that are organic compounds, meaning they are carbon-based and often contain hydrogen atoms.""",
            'topic': 'Chemistry',
            'subtopic': 'Solvents',
            'examples': ["Ethanol", "Diethyl ether", "Chloroform"]
        }
        self.halt()

    @Rule(Fact(query_topic='inorganic_solvents'))
    def rule_inorganic_solvents(self):
        """Solvents that are inorganic compounds, meaning they are typically not carbon-based."""
        self.response = {
            'concept': 'Inorganic Solvents',
            'explanation': """Solvents that are inorganic compounds, meaning they are typically not carbon-based.""",
            'topic': 'Chemistry',
            'subtopic': 'Solvents',
            'examples': ["Water", "Liquid ammonia", "Hydrochloric acid"]
        }
        self.halt()

    @Rule(Fact(query_topic='crystallization__separation_technique_'))
    def rule_crystallization__separation_technique_(self):
        """A separation and purification technique that involves the formation of solid crystals from a solution, often by cooling a hot saturated solution or by evaporating the solvent. It separates a soluble solid from a liquid."""
        self.response = {
            'concept': 'Crystallization (Separation Technique)',
            'explanation': """A separation and purification technique that involves the formation of solid crystals from a solution, often by cooling a hot saturated solution or by evaporating the solvent. It separates a soluble solid from a liquid.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separation of salt from salt water", "Production of sugar crystals", "Purification of copper sulphate"]
        }
        self.halt()

    @Rule(Fact(query_topic='deliquescence'))
    def rule_deliquescence(self):
        """The property of certain substances to absorb moisture from the atmosphere to such an extent that they dissolve in it and form a solution."""
        self.response = {
            'concept': 'Deliquescence',
            'explanation': """The property of certain substances to absorb moisture from the atmosphere to such an extent that they dissolve in it and form a solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Substances',
            'examples': ["Magnesium chloride (MgCl2) exhibiting deliquescence", "Calcium chloride (CaCl2) absorbing atmospheric water"]
        }
        self.halt()

    @Rule(Fact(query_topic='saturated_solution'))
    def rule_saturated_solution(self):
        """A solution that contains the maximum amount of solute that can be dissolved in a given amount of solvent at a specific temperature and pressure, where no more solute can dissolve."""
        self.response = {
            'concept': 'Saturated Solution',
            'explanation': """A solution that contains the maximum amount of solute that can be dissolved in a given amount of solvent at a specific temperature and pressure, where no more solute can dissolve.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["A salt solution where no more salt will dissolve at that temperature", "A sugar solution with undissolved sugar at the bottom"]
        }
        self.halt()

    @Rule(Fact(query_topic='increasing_solubility_in_saturated_solutions'))
    def rule_increasing_solubility_in_saturated_solutions(self):
        """To dissolve more solute in a saturated solution, one can typically increase the temperature of the solution (for most solids) or add more solvent."""
        self.response = {
            'concept': 'Increasing Solubility in Saturated Solutions',
            'explanation': """To dissolve more solute in a saturated solution, one can typically increase the temperature of the solution (for most solids) or add more solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Solutions',
            'examples': ["Heating a saturated salt solution to dissolve more salt", "Adding more water to a saturated solution to dissolve more solute"]
        }
        self.halt()

    @Rule(Fact(query_topic='solvent_extraction'))
    def rule_solvent_extraction(self):
        """A separation technique used to separate compounds based on their relative solubilities in two different immiscible liquids, usually an aqueous phase and an organic solvent."""
        self.response = {
            'concept': 'Solvent Extraction',
            'explanation': """A separation technique used to separate compounds based on their relative solubilities in two different immiscible liquids, usually an aqueous phase and an organic solvent.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Extracting caffeine from coffee beans using an organic solvent", "Separating organic compounds from an aqueous mixture using diethyl ether"]
        }
        self.halt()

    @Rule(Fact(query_topic='qualities_of_solvents_for_solvent_extraction'))
    def rule_qualities_of_solvents_for_solvent_extraction(self):
        """For effective solvent extraction, the two solvents must be immiscible, and the substance to be extracted must be significantly more soluble in the second solvent than in the existing one. The solvents should also be easily separable."""
        self.response = {
            'concept': 'Qualities of Solvents for Solvent Extraction',
            'explanation': """For effective solvent extraction, the two solvents must be immiscible, and the substance to be extracted must be significantly more soluble in the second solvent than in the existing one. The solvents should also be easily separable.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["The second solvent must not mix with the first solvent", "The solute must preferentially dissolve in the extracting solvent", "The solvents should have different densities for easy separation"]
        }
        self.halt()

    @Rule(Fact(query_topic='distillation__separation_technique_'))
    def rule_distillation__separation_technique_(self):
        """A separation process that purifies a liquid from a non-volatile solid or separates two or more liquids with different boiling points by heating the mixture to form vapor and then condensing the vapor back into liquid."""
        self.response = {
            'concept': 'Distillation (Separation Technique)',
            'explanation': """A separation process that purifies a liquid from a non-volatile solid or separates two or more liquids with different boiling points by heating the mixture to form vapor and then condensing the vapor back into liquid.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating pure water from salt solution", "Separating ethanol from water mixture", "Purifying industrial chemicals"]
        }
        self.halt()

    @Rule(Fact(query_topic='principle_of_distillation'))
    def rule_principle_of_distillation(self):
        """Distillation separates components of a mixture primarily based on the differences in their boiling points, where the component with the lower boiling point vaporizes first."""
        self.response = {
            'concept': 'Principle of Distillation',
            'explanation': """Distillation separates components of a mixture primarily based on the differences in their boiling points, where the component with the lower boiling point vaporizes first.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating liquids with different boiling points, such as ethanol (78°C) and water (100°C)", "Removing non-volatile impurities from a volatile liquid"]
        }
        self.halt()

    @Rule(Fact(query_topic='simple_vs__fractional_distillation'))
    def rule_simple_vs__fractional_distillation(self):
        """Both are distillation methods. Simple distillation is used for separating liquids with widely different boiling points (>25°C difference) or a liquid from a non-volatile solute. Fractional distillation is used for separating liquids with close boiling points, utilizing a fractionating column for increased surface area and repeated vaporization-condensation cycles to achieve better separation."""
        self.response = {
            'concept': 'Simple vs. Fractional Distillation',
            'explanation': """Both are distillation methods. Simple distillation is used for separating liquids with widely different boiling points (>25°C difference) or a liquid from a non-volatile solute. Fractional distillation is used for separating liquids with close boiling points, utilizing a fractionating column for increased surface area and repeated vaporization-condensation cycles to achieve better separation.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Simple distillation to separate salt from water", "Fractional distillation to separate components of crude oil", "Fractional distillation to separate ethanol from water"]
        }
        self.halt()

    @Rule(Fact(query_topic='liebig_condenser_setup_for_distillation'))
    def rule_liebig_condenser_setup_for_distillation(self):
        """In a Liebig condenser, vapor should be inserted from the top to ensure efficient flow downwards and maximum contact with the cooled surface. Cooling water should be inserted from the bottom to fill the condenser jacket completely, allowing for efficient heat exchange through counter-current flow (cold water flows against the descending hot vapor/condensate)."""
        self.response = {
            'concept': 'Liebig Condenser Setup for Distillation',
            'explanation': """In a Liebig condenser, vapor should be inserted from the top to ensure efficient flow downwards and maximum contact with the cooled surface. Cooling water should be inserted from the bottom to fill the condenser jacket completely, allowing for efficient heat exchange through counter-current flow (cold water flows against the descending hot vapor/condensate).""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Techniques',
            'examples': ["Vapor entering at the top ensures gravity aids condensation", "Water entering at the bottom ensures the entire jacket is filled with cold water", "Counter-current flow maximizes cooling efficiency"]
        }
        self.halt()

    @Rule(Fact(query_topic='vapour_distillation__steam_distillation_'))
    def rule_vapour_distillation__steam_distillation_(self):
        """A special type of distillation process used to separate substances that are insoluble in water and have high boiling points, such as essential oils, by passing steam through the material. This allows the compounds to distill at lower temperatures, preventing thermal decomposition."""
        self.response = {
            'concept': 'Vapour Distillation (Steam Distillation)',
            'explanation': """A special type of distillation process used to separate substances that are insoluble in water and have high boiling points, such as essential oils, by passing steam through the material. This allows the compounds to distill at lower temperatures, preventing thermal decomposition.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Extracting essential oils from plant materials like cinnamon bark", "Production of essential oils in Sri Lanka", "Separating volatile organic compounds from plant matter"]
        }
        self.halt()

    @Rule(Fact(query_topic='chromatography_for_separating_colors'))
    def rule_chromatography_for_separating_colors(self):
        """Chromatography, specifically paper or thin-layer chromatography, is a technique used to separate the different colored components of a mixture (like dyes in food) based on their differing affinities for a stationary phase and a mobile phase. Components travel at different speeds, resulting in separation."""
        self.response = {
            'concept': 'Chromatography for Separating Colors',
            'explanation': """Chromatography, specifically paper or thin-layer chromatography, is a technique used to separate the different colored components of a mixture (like dyes in food) based on their differing affinities for a stationary phase and a mobile phase. Components travel at different speeds, resulting in separation.""",
            'topic': 'Chemistry',
            'subtopic': 'Separation Techniques',
            'examples': ["Separating the pigments in a marker pen ink using paper chromatography", "Analyzing the dyes in food products like candies or toffees", "Identifying the components of plant extracts"]
        }
        self.halt()

    @Rule(Fact(query_topic='large_intestine_structure'))
    def rule_large_intestine_structure(self):
        """The large intestine is approximately 1.5 m long, beginning with the caecum and terminating at the anus. The dilated portion is known as the rectum, which opens to the outside via the anus. Materials entering the large intestine contain very small amounts of nutrients, primarily undigested cellulose and water."""
        self.response = {
            'concept': 'Large Intestine Structure',
            'explanation': """The large intestine is approximately 1.5 m long, beginning with the caecum and terminating at the anus. The dilated portion is known as the rectum, which opens to the outside via the anus. Materials entering the large intestine contain very small amounts of nutrients, primarily undigested cellulose and water.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Anatomy',
            'examples': ["The caecum is the initial part of the large intestine.", "The rectum is the dilated final section of the large intestine.", "The anus is the external opening of the large intestine."]
        }
        self.halt()

    @Rule(Fact(query_topic='appendix'))
    def rule_appendix(self):
        """The appendix is a small, blind-ended tubular structure that originates at the end of the caecum. In humans, it is very small and can become infected and swollen."""
        self.response = {
            'concept': 'Appendix',
            'explanation': """The appendix is a small, blind-ended tubular structure that originates at the end of the caecum. In humans, it is very small and can become infected and swollen.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Anatomy',
            'examples': ["The appendix is located near the caecum.", "It is a small, finger-like projection.", "Infection can cause the appendix to become swollen."]
        }
        self.halt()

    @Rule(Fact(query_topic='appendicitis'))
    def rule_appendicitis(self):
        """Appendicitis is a disease characterized by the infection and swelling of the appendix."""
        self.response = {
            'concept': 'Appendicitis',
            'explanation': """Appendicitis is a disease characterized by the infection and swelling of the appendix.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Disorders',
            'examples': ["An infected appendix leads to appendicitis.", "Symptoms of appendicitis often include severe abdominal pain.", "Surgical removal may be necessary for appendicitis."]
        }
        self.halt()

    @Rule(Fact(query_topic='large_intestine_function'))
    def rule_large_intestine_function(self):
        """The primary function of the large intestine is to absorb water from the matter received from the ileum, thereby converting it into a semi-solid state."""
        self.response = {
            'concept': 'Large Intestine Function',
            'explanation': """The primary function of the large intestine is to absorb water from the matter received from the ileum, thereby converting it into a semi-solid state.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Physiology',
            'examples': ["Water absorption is a key role of the large intestine.", "The large intestine helps in compacting waste material.", "Without adequate water absorption, faecal matter would remain liquid."]
        }
        self.halt()

    @Rule(Fact(query_topic='faecal_matter'))
    def rule_faecal_matter(self):
        """Faecal matter is the material that enters the large intestine, composed mainly of undigested food (such as cellulose), microorganisms, epithelial cells, and mucus. It typically has a yellow color due to the presence of bile pigments."""
        self.response = {
            'concept': 'Faecal Matter',
            'explanation': """Faecal matter is the material that enters the large intestine, composed mainly of undigested food (such as cellulose), microorganisms, epithelial cells, and mucus. It typically has a yellow color due to the presence of bile pigments.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System',
            'examples': ["Undigested cellulose is a component of faecal matter.", "Bile pigments contribute to the yellow color of faecal matter.", "Microorganisms are found within faecal matter."]
        }
        self.halt()

    @Rule(Fact(query_topic='defecation'))
    def rule_defecation(self):
        """When the large intestine becomes filled with faecal matter, it is expelled from the rectum through the anus."""
        self.response = {
            'concept': 'Defecation',
            'explanation': """When the large intestine becomes filled with faecal matter, it is expelled from the rectum through the anus.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Physiology',
            'examples': ["The rectum holds faecal matter before defecation.", "The process of passing faecal matter out of the body is defecation.", "The anus is the exit point for faecal matter."]
        }
        self.halt()

    @Rule(Fact(query_topic='vulnerability_of_digestive_system_to_infections'))
    def rule_vulnerability_of_digestive_system_to_infections(self):
        """The digestive tract has a high susceptibility to infections and disorders because materials frequently enter it from the external environment."""
        self.response = {
            'concept': 'Vulnerability of Digestive System to Infections',
            'explanation': """The digestive tract has a high susceptibility to infections and disorders because materials frequently enter it from the external environment.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Disorders',
            'examples': ["Consuming contaminated food can introduce infections to the digestive tract.", "Pathogens can easily enter the digestive system with ingested food.", "Frequent exposure to external substances increases the risk of digestive illnesses."]
        }
        self.halt()

    @Rule(Fact(query_topic='gastritis'))
    def rule_gastritis(self):
        """Gastritis is the inflammation of the inner lining (mucosa) of the stomach, commonly referred to as 'acidity.' Symptoms include acid regurgitation to the mouth, a burning sensation, and stomach pain. In more severe cases, ulcers can form in the stomach and duodenal wall, potentially leading to bleeding."""
        self.response = {
            'concept': 'Gastritis',
            'explanation': """Gastritis is the inflammation of the inner lining (mucosa) of the stomach, commonly referred to as 'acidity.' Symptoms include acid regurgitation to the mouth, a burning sensation, and stomach pain. In more severe cases, ulcers can form in the stomach and duodenal wall, potentially leading to bleeding.""",
            'topic': 'Human body processes',
            'subtopic': 'Digestive System Disorders',
            'examples': ["A burning feeling in the stomach is a symptom of gastritis.", "Severe gastritis can lead to stomach ulcers.", "Gastritis is often colloquially known as 'acidity'."]
        }
        self.halt()

    @Rule(Fact(query_topic='acids__bases_and_salts'))
    def rule_acids__bases_and_salts(self):
        """Acids, bases and salts are used for various activities in our day to day life."""
        self.response = {
            'concept': 'Acids, Bases and Salts',
            'explanation': """Acids, bases and salts are used for various activities in our day to day life.""",
            'topic': 'Chemistry',
            'subtopic': 'General Chemistry',
            'examples': ["Lime juice", "Antacid tablets", "Salt"]
        }
        self.halt()

    @Rule(Fact(query_topic='acids'))
    def rule_acids(self):
        """A classification of substances based on their chemical properties."""
        self.response = {
            'concept': 'Acids',
            'explanation': """A classification of substances based on their chemical properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Bases',
            'examples': ["Lime juice", "Vinegar", "Vitamin C tablets"]
        }
        self.halt()

    @Rule(Fact(query_topic='bases'))
    def rule_bases(self):
        """A classification of substances based on their chemical properties."""
        self.response = {
            'concept': 'Bases',
            'explanation': """A classification of substances based on their chemical properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Bases',
            'examples': ["Antacid tablets", "Milk of magnesia", "Toothpaste"]
        }
        self.halt()

    @Rule(Fact(query_topic='salts'))
    def rule_salts(self):
        """A classification of substances based on their chemical properties."""
        self.response = {
            'concept': 'Salts',
            'explanation': """A classification of substances based on their chemical properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Bases',
            'examples': ["Salt", "Saline solution"]
        }
        self.halt()

    @Rule(Fact(query_topic='acid'))
    def rule_acid(self):
        """A compound that releases hydrogen ions (H+) when dissolved in an aqueous medium."""
        self.response = {
            'concept': 'Acid',
            'explanation': """A compound that releases hydrogen ions (H+) when dissolved in an aqueous medium.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids',
            'examples': ["Hydrochloric acid (HCl)", "Nitric acid (HNO3)", "Sulphuric acid (H2SO4)"]
        }
        self.halt()

    @Rule(Fact(query_topic='strong_acid'))
    def rule_strong_acid(self):
        """Acids that release H+ ions through complete ionisation in an aqueous medium, meaning all acid molecules dissociate into H+ ions and their corresponding negative ions in water."""
        self.response = {
            'concept': 'Strong Acid',
            'explanation': """Acids that release H+ ions through complete ionisation in an aqueous medium, meaning all acid molecules dissociate into H+ ions and their corresponding negative ions in water.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Acids',
            'examples': ["Hydrochloric acid (HCl)", "Sulphuric acid (H2SO4)", "Nitric acid (HNO3)"]
        }
        self.halt()

    @Rule(Fact(query_topic='weak_acid'))
    def rule_weak_acid(self):
        """Acids which release H+ ions in an aqueous medium by incomplete or partial ionisation. In such solutions, only a fraction of the acid molecules dissociate, while the remaining unionised molecules stay intact."""
        self.response = {
            'concept': 'Weak Acid',
            'explanation': """Acids which release H+ ions in an aqueous medium by incomplete or partial ionisation. In such solutions, only a fraction of the acid molecules dissociate, while the remaining unionised molecules stay intact.""",
            'topic': 'Chemistry',
            'subtopic': 'Classification of Acids',
            'examples': ["Acetic acid (CH3COOH)", "Carbonic acid (H2CO3)", "Phosphoric acid (H3PO4)"]
        }
        self.halt()

    @Rule(Fact(query_topic='dilute_acids'))
    def rule_dilute_acids(self):
        """Acids of low concentration are known as dilute acids. Required concentration can be prepared by mixing concentrated acids with water."""
        self.response = {
            'concept': 'Dilute Acids',
            'explanation': """Acids of low concentration are known as dilute acids. Required concentration can be prepared by mixing concentrated acids with water.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Acids',
            'examples': ["Mixing concentrated hydrochloric acid with water to obtain a dilute solution", "Sulfuric acid with a low percentage of H2SO4"]
        }
        self.halt()

    @Rule(Fact(query_topic='corrosive_properties_of_acids'))
    def rule_corrosive_properties_of_acids(self):
        """Concentrated acids are corrosive in nature. When they come into contact with substances like wood, metals, or cloth, they corrode them. If spilled on the skin, they cause severe burns. This property is often indicated by a warning symbol."""
        self.response = {
            'concept': 'Corrosive Properties of Acids',
            'explanation': """Concentrated acids are corrosive in nature. When they come into contact with substances like wood, metals, or cloth, they corrode them. If spilled on the skin, they cause severe burns. This property is often indicated by a warning symbol.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Acids',
            'examples': ["Concentrated acid corroding a wooden surface", "Severe burns on skin caused by acid spillage", "Damage to metals upon contact with concentrated acids"]
        }
        self.halt()

    @Rule(Fact(query_topic='taste_of_acids'))
    def rule_taste_of_acids(self):
        """A common characteristic feature of acids is that they have a sour taste. (Caution: Laboratory acids should never be tasted)."""
        self.response = {
            'concept': 'Taste of Acids',
            'explanation': """A common characteristic feature of acids is that they have a sour taste. (Caution: Laboratory acids should never be tasted).""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Acids',
            'examples': ["The sour taste of lime juice", "The sourness of lemon juice"]
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_dilute_acids_with_metals'))
    def rule_reaction_of_dilute_acids_with_metals(self):
        """Dilute acids react with metals that are above hydrogen in the reactivity series, forming the salt of the metal and releasing hydrogen gas."""
        self.response = {
            'concept': 'Reaction of Dilute Acids with Metals',
            'explanation': """Dilute acids react with metals that are above hydrogen in the reactivity series, forming the salt of the metal and releasing hydrogen gas.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Properties of Acids',
            'examples': ["Mg (s) + 2HCl (aq) → MgCl2 (aq) + H2 (g)", "Reaction of zinc with dilute sulfuric acid to produce zinc sulfate and hydrogen gas"]
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_acids_with_carbonates_bicarbonates'))
    def rule_reaction_of_acids_with_carbonates_bicarbonates(self):
        """Acids react with carbonates or bicarbonates to produce carbon dioxide gas, a salt, and water. This is a characteristic feature used to identify acids."""
        self.response = {
            'concept': 'Reaction of Acids with Carbonates/Bicarbonates',
            'explanation': """Acids react with carbonates or bicarbonates to produce carbon dioxide gas, a salt, and water. This is a characteristic feature used to identify acids.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Properties of Acids',
            'examples': ["CaCO3 (s) + 2HCl (aq) → CaCl2 (aq) + H2O (l) + CO2 (g)", "Adding diluted hydrochloric acid to calcium carbonate to produce carbon dioxide"]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_reaction__acids_with_bases_'))
    def rule_neutralization_reaction__acids_with_bases_(self):
        """Acids react with bases to form salts and water. This reaction is known as a neutralization reaction."""
        self.response = {
            'concept': 'Neutralization Reaction (Acids with Bases)',
            'explanation': """Acids react with bases to form salts and water. This reaction is known as a neutralization reaction.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Properties of Acids',
            'examples': ["H2SO4 (aq) + 2NaOH (aq) → Na2SO4 (aq) + 2H2O (l)", "Mixing hydrochloric acid with sodium hydroxide to form sodium chloride and water"]
        }
        self.halt()

    @Rule(Fact(query_topic='litmus_test_for_acids'))
    def rule_litmus_test_for_acids(self):
        """Acids turn the color of blue litmus paper red. This color change is a simple and common test used to identify the presence of an acid."""
        self.response = {
            'concept': 'Litmus Test for Acids',
            'explanation': """Acids turn the color of blue litmus paper red. This color change is a simple and common test used to identify the presence of an acid.""",
            'topic': 'Chemistry',
            'subtopic': 'Identification of Acids',
            'examples': ["A drop of vinegar turning blue litmus red", "Submerging blue litmus paper in hydrochloric acid causes it to turn red"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_hydrochloric_acid'))
    def rule_uses_of_hydrochloric_acid(self):
        """Hydrochloric acid has various industrial and laboratory applications."""
        self.response = {
            'concept': 'Uses of Hydrochloric Acid',
            'explanation': """Hydrochloric acid has various industrial and laboratory applications.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Acids',
            'examples': ["Removal of rust in steel objects", "Making gelatin from bony materials in food technology", "Making aqua regia (a mixture with concentrated nitric acid)"]
        }
        self.halt()

    @Rule(Fact(query_topic='aqua_regia'))
    def rule_aqua_regia(self):
        """A highly corrosive mixture of nitric acid and hydrochloric acid, used for dissolving noble metals."""
        self.response = {
            'concept': 'Aqua Regia',
            'explanation': """A highly corrosive mixture of nitric acid and hydrochloric acid, used for dissolving noble metals.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids (Uses)',
            'examples': ["Dissolving gold", "Dissolving platinum"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_sulphuric_acid'))
    def rule_uses_of_sulphuric_acid(self):
        """Sulphuric acid is utilized in various industrial and commercial processes."""
        self.response = {
            'concept': 'Uses of Sulphuric Acid',
            'explanation': """Sulphuric acid is utilized in various industrial and commercial processes.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids (Uses)',
            'examples': ["Production of fertilizers such as ammonium sulphate", "Making battery acid", "Production of paints, plastics and detergents"]
        }
        self.halt()

    @Rule(Fact(query_topic='battery_acid'))
    def rule_battery_acid(self):
        """A diluted form of sulphuric acid specifically used in batteries."""
        self.response = {
            'concept': 'Battery Acid',
            'explanation': """A diluted form of sulphuric acid specifically used in batteries.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids (Definitions)',
            'examples': ["Diluted sulphuric acid", "Found in lead-acid batteries"]
        }
        self.halt()

    @Rule(Fact(query_topic='concentrated_sulphuric_acid_as_dehydrating_agent'))
    def rule_concentrated_sulphuric_acid_as_dehydrating_agent(self):
        """Concentrated sulphuric acid has a strong affinity for water and is therefore used to remove water from other substances."""
        self.response = {
            'concept': 'Concentrated Sulphuric Acid as Dehydrating Agent',
            'explanation': """Concentrated sulphuric acid has a strong affinity for water and is therefore used to remove water from other substances.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids (Properties & Uses)',
            'examples': ["Drying gases", "Bubbling a gas through it to remove moisture"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_acetic_acid'))
    def rule_uses_of_acetic_acid(self):
        """Acetic acid, a common organic acid, has applications in food processing and various industries."""
        self.response = {
            'concept': 'Uses of Acetic Acid',
            'explanation': """Acetic acid, a common organic acid, has applications in food processing and various industries.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids (Uses)',
            'examples': ["Processing food where vinegar is used", "Coagulation of rubber latex", "Production of photographic films"]
        }
        self.halt()

    @Rule(Fact(query_topic='examples_of_bases'))
    def rule_examples_of_bases(self):
        """Common substances found in everyday life that exhibit basic properties."""
        self.response = {
            'concept': 'Examples of Bases',
            'explanation': """Common substances found in everyday life that exhibit basic properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Examples)',
            'examples': ["Milk of magnesia", "Toothpaste", "Soap"]
        }
        self.halt()

    @Rule(Fact(query_topic='common_laboratory_bases'))
    def rule_common_laboratory_bases(self):
        """Bases frequently used in laboratory settings, often in their aqueous solution form."""
        self.response = {
            'concept': 'Common Laboratory Bases',
            'explanation': """Bases frequently used in laboratory settings, often in their aqueous solution form.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Examples)',
            'examples': ["Sodium hydroxide (NaOH)", "Potassium hydroxide (KOH)", "Ammonia solution (NH4OH)"]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_a_base'))
    def rule_definition_of_a_base(self):
        """A chemical compound that increases the hydroxyl ion (OH-) concentration of an aqueous solution."""
        self.response = {
            'concept': 'Definition of a Base',
            'explanation': """A chemical compound that increases the hydroxyl ion (OH-) concentration of an aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Definition)',
            'examples': ["Sodium hydroxide (NaOH) ionises to produce OH- ions", "Potassium hydroxide (KOH) ionises to produce OH- ions"]
        }
        self.halt()

    @Rule(Fact(query_topic='strong_bases'))
    def rule_strong_bases(self):
        """Bases that completely ionise (dissociate) into their constituent ions when dissolved in an aqueous solution."""
        self.response = {
            'concept': 'Strong Bases',
            'explanation': """Bases that completely ionise (dissociate) into their constituent ions when dissolved in an aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Types)',
            'examples': ["Sodium hydroxide (NaOH)", "Potassium hydroxide (KOH)"]
        }
        self.halt()

    @Rule(Fact(query_topic='weak_bases'))
    def rule_weak_bases(self):
        """Bases that only partially ionise (dissociate) when dissolved in an aqueous solution."""
        self.response = {
            'concept': 'Weak Bases',
            'explanation': """Bases that only partially ionise (dissociate) when dissolved in an aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Types)',
            'examples': ["Ammonia solution (NH4OH)", "Aqueous ammonia"]
        }
        self.halt()

    @Rule(Fact(query_topic='properties_of_bases'))
    def rule_properties_of_bases(self):
        """Observable characteristics common to many basic substances."""
        self.response = {
            'concept': 'Properties of Bases',
            'explanation': """Observable characteristics common to many basic substances.""",
            'topic': 'Chemistry',
            'subtopic': 'Bases (Properties)',
            'examples': ["Having a slimy texture", "Feeling slippery as in soap"]
        }
        self.halt()

    @Rule(Fact(query_topic='laboratory_safety_rule_for_bases'))
    def rule_laboratory_safety_rule_for_bases(self):
        """It is important not to touch bases in the laboratory to ensure safety."""
        self.response = {
            'concept': 'Laboratory Safety Rule for Bases',
            'explanation': """It is important not to touch bases in the laboratory to ensure safety.""",
            'topic': 'Chemistry',
            'subtopic': 'Laboratory Safety',
            'examples': ["Avoid direct contact with sodium hydroxide.", "Do not touch potassium hydroxide solutions.", "Always wear gloves when handling bases."]
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_bases_with_acids'))
    def rule_reaction_of_bases_with_acids(self):
        """Bases react with acids in a neutralization reaction to produce salts and water."""
        self.response = {
            'concept': 'Reaction of Bases with Acids',
            'explanation': """Bases react with acids in a neutralization reaction to produce salts and water.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Properties of Bases',
            'examples': ["2NaOH (aq) + H2SO4 (aq) → Na2SO4 (aq) + 2H2O (l)", "KOH + HCl → KCl + H2O", "NH4OH + HNO3 → NH4NO3 + H2O"]
        }
        self.halt()

    @Rule(Fact(query_topic='litmus_test_for_bases'))
    def rule_litmus_test_for_bases(self):
        """Bases turn red litmus paper blue, which is a simple and common test used to identify bases."""
        self.response = {
            'concept': 'Litmus Test for Bases',
            'explanation': """Bases turn red litmus paper blue, which is a simple and common test used to identify bases.""",
            'topic': 'Chemistry',
            'subtopic': 'Identification of Bases',
            'examples': ["A solution that turns red litmus paper blue is identified as a base.", "Adding a basic solution to red litmus changes its color to blue.", "Litmus paper is used to distinguish between acids (red) and bases (blue)."]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_alkalis'))
    def rule_definition_of_alkalis(self):
        """Alkalis are a specific type of base that readily dissolve in water."""
        self.response = {
            'concept': 'Definition of Alkalis',
            'explanation': """Alkalis are a specific type of base that readily dissolve in water.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Bases',
            'examples': ["Sodium hydroxide (NaOH)", "Potassium hydroxide (KOH)", "Ammonia solution (NH4OH)"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_sodium_hydroxide__naoh_'))
    def rule_uses_of_sodium_hydroxide__naoh_(self):
        """Sodium hydroxide is a strong base with various industrial applications, including the production of soap, paper, artificial silk, and paints. It is also used in laboratories and for refining petroleum products."""
        self.response = {
            'concept': 'Uses of Sodium Hydroxide (NaOH)',
            'explanation': """Sodium hydroxide is a strong base with various industrial applications, including the production of soap, paper, artificial silk, and paints. It is also used in laboratories and for refining petroleum products.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Bases',
            'examples': ["Used in the production of soap and paper.", "Serves as a strong base in laboratory settings.", "Employed for refining petroleum products."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_magnesium_hydroxide__mg_oh_2_'))
    def rule_uses_of_magnesium_hydroxide__mg_oh_2_(self):
        """Magnesium hydroxide suspension, commonly known as 'milk of magnesia,' is utilized as an antacid to alleviate gastritis (stomach acidity) and in the purification of molasses within the sugar industry."""
        self.response = {
            'concept': 'Uses of Magnesium Hydroxide (Mg(OH)2)',
            'explanation': """Magnesium hydroxide suspension, commonly known as 'milk of magnesia,' is utilized as an antacid to alleviate gastritis (stomach acidity) and in the purification of molasses within the sugar industry.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Bases',
            'examples': ["Milk of magnesia used as an antacid for stomach acidity.", "Purification of molasses in the sugar industry.", "Relief of indigestion due to excess stomach acid."]
        }
        self.halt()

    @Rule(Fact(query_topic='identification_of_acids_and_bases_by_indicators'))
    def rule_identification_of_acids_and_bases_by_indicators(self):
        """Indicators are substances that change color depending on whether they are in an acidic or basic solution, providing a way to approximately identify the nature of a substance."""
        self.response = {
            'concept': 'Identification of Acids and Bases by Indicators',
            'explanation': """Indicators are substances that change color depending on whether they are in an acidic or basic solution, providing a way to approximately identify the nature of a substance.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Tests',
            'examples': ["Using litmus paper to test for acids or bases.", "Employing phenolphthalein to detect basic solutions.", "Adding methyl orange to a solution to determine its acidity."]
        }
        self.halt()

    @Rule(Fact(query_topic='litmus_indicator_color_changes'))
    def rule_litmus_indicator_color_changes(self):
        """Litmus indicator shows distinct color changes in acidic and basic environments, turning red in acids and blue in bases."""
        self.response = {
            'concept': 'Litmus Indicator Color Changes',
            'explanation': """Litmus indicator shows distinct color changes in acidic and basic environments, turning red in acids and blue in bases.""",
            'topic': 'Chemistry',
            'subtopic': 'Indicators',
            'examples': ["Acid color: Red", "Base color: Blue", "Neutral color: Purple (not explicitly mentioned but implied as a mid-point)"]
        }
        self.halt()

    @Rule(Fact(query_topic='phenolphthalein_indicator_color_changes'))
    def rule_phenolphthalein_indicator_color_changes(self):
        """Phenolphthalein indicator is colorless in acidic solutions and turns pink when in a basic solution."""
        self.response = {
            'concept': 'Phenolphthalein Indicator Color Changes',
            'explanation': """Phenolphthalein indicator is colorless in acidic solutions and turns pink when in a basic solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Indicators',
            'examples': ["Acid color: Colorless", "Base color: Pink", "Strong basic solution: Dark pink/magenta"]
        }
        self.halt()

    @Rule(Fact(query_topic='methyl_orange_indicator_color_changes'))
    def rule_methyl_orange_indicator_color_changes(self):
        """Methyl orange indicator displays specific color changes, appearing red in acidic conditions and yellow in basic conditions."""
        self.response = {
            'concept': 'Methyl Orange Indicator Color Changes',
            'explanation': """Methyl orange indicator displays specific color changes, appearing red in acidic conditions and yellow in basic conditions.""",
            'topic': 'Chemistry',
            'subtopic': 'Indicators',
            'examples': ["Acid color: Red", "Base color: Yellow", "Transition range: Orange"]
        }
        self.halt()

    @Rule(Fact(query_topic='limitations_of_indicators_for_acid_base_identification'))
    def rule_limitations_of_indicators_for_acid_base_identification(self):
        """While useful, indicators do not provide a very accurate method for identifying acids and bases. They cannot determine the strength of an acid or a base, only providing an approximate classification."""
        self.response = {
            'concept': 'Limitations of Indicators for Acid/Base Identification',
            'explanation': """While useful, indicators do not provide a very accurate method for identifying acids and bases. They cannot determine the strength of an acid or a base, only providing an approximate classification.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Tests',
            'examples': ["Indicators cannot distinguish between a strong acid and a weak acid.", "The exact pH value cannot be obtained using indicators alone.", "Color changes might be subjective or approximate."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_scale'))
    def rule_ph_scale(self):
        """The pH scale is a numerical scale used to quantify and indicate the degree of acidity or basicity of a given solution."""
        self.response = {
            'concept': 'pH Scale',
            'explanation': """The pH scale is a numerical scale used to quantify and indicate the degree of acidity or basicity of a given solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid-Base Strength',
            'examples': ["A solution with pH 7 is neutral.", "Solutions with pH less than 7 are acidic.", "Solutions with pH greater than 7 are basic."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_scale_definition'))
    def rule_ph_scale_definition(self):
        """The pH scale is a numerical scale, generally ranging from 0 to 14, where each number corresponds to a specific colour, used to indicate the acidity or basicity of a solution."""
        self.response = {
            'concept': 'pH Scale Definition',
            'explanation': """The pH scale is a numerical scale, generally ranging from 0 to 14, where each number corresponds to a specific colour, used to indicate the acidity or basicity of a solution.""",
            'topic': 'Chemistry',
            'subtopic': 'pH and Indicators',
            'examples': ["A scale with values from 0 to 14.", "Each pH number having a distinct colour code."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_values_and_solution_properties'))
    def rule_ph_values_and_solution_properties(self):
        """On the pH scale, a pH value of 7 indicates a neutral substance. Acidic solutions have pH values less than 7 (acidity decreases from 0 to 6), while basic solutions have pH values greater than 7 (basicity increases from 8 to 14)."""
        self.response = {
            'concept': 'pH Values and Solution Properties',
            'explanation': """On the pH scale, a pH value of 7 indicates a neutral substance. Acidic solutions have pH values less than 7 (acidity decreases from 0 to 6), while basic solutions have pH values greater than 7 (basicity increases from 8 to 14).""",
            'topic': 'Chemistry',
            'subtopic': 'pH and Indicators',
            'examples': ["Water has a pH of 7, making it neutral.", "Lemon juice typically has a pH of 2-3, indicating acidity.", "Household ammonia has a pH of 11-12, indicating basicity."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_papers_and_their_use'))
    def rule_ph_papers_and_their_use(self):
        """pH papers are laboratory tools, made by mixing several indicators, available in books or rolls. They are used to determine the pH value, and thus the acidity, basicity, neutrality, and strength of a solution, by dipping the paper into the solution and comparing its resulting colour to a colour code."""
        self.response = {
            'concept': 'pH Papers and Their Use',
            'explanation': """pH papers are laboratory tools, made by mixing several indicators, available in books or rolls. They are used to determine the pH value, and thus the acidity, basicity, neutrality, and strength of a solution, by dipping the paper into the solution and comparing its resulting colour to a colour code.""",
            'topic': 'Chemistry',
            'subtopic': 'pH and Indicators',
            'examples': ["Dipping a pH paper in an unknown liquid to find its pH.", "Using pH paper to distinguish between a strong acid and a weak acid by observing colour intensity.", "Comparing the colour of a dipped pH paper to a chart to determine if a solution is basic."]
        }
        self.halt()

    @Rule(Fact(query_topic='salts__general_'))
    def rule_salts__general_(self):
        """Salts are chemical compounds, exemplified by common table salt (sodium chloride). They are often found as components in mixtures like Jeewani solutions or saline solutions."""
        self.response = {
            'concept': 'Salts (General)',
            'explanation': """Salts are chemical compounds, exemplified by common table salt (sodium chloride). They are often found as components in mixtures like Jeewani solutions or saline solutions.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["Sodium chloride (NaCl) is a common salt.", "Potassium iodide (KI) is a salt.", "Magnesium sulfate (MgSO4) is a salt."]
        }
        self.halt()

    @Rule(Fact(query_topic='formation_of_salts_from_acids_and_bases'))
    def rule_formation_of_salts_from_acids_and_bases(self):
        """Salts are typically formed through the chemical reaction between an acid and a base, often referred to as a neutralization reaction."""
        self.response = {
            'concept': 'Formation of Salts from Acids and Bases',
            'explanation': """Salts are typically formed through the chemical reaction between an acid and a base, often referred to as a neutralization reaction.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["Hydrochloric acid reacts with sodium hydroxide to form sodium chloride.", "Potassium hydroxide reacts with hydrochloric acid to form potassium chloride.", "Nitric acid reacts with magnesium hydroxide to form magnesium nitrate."]
        }
        self.halt()

    @Rule(Fact(query_topic='properties_of_salts_based_on_parent_acid_base_strength'))
    def rule_properties_of_salts_based_on_parent_acid_base_strength(self):
        """The properties of a salt (whether it exhibits acidic, basic, or neutral characteristics) are determined by the strength of the acid and the base that reacted to form it."""
        self.response = {
            'concept': 'Properties of Salts Based on Parent Acid/Base Strength',
            'explanation': """The properties of a salt (whether it exhibits acidic, basic, or neutral characteristics) are determined by the strength of the acid and the base that reacted to form it.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["A salt from a strong acid and a strong base is neutral.", "A salt from a strong acid and a weak base is acidic.", "A salt from a weak acid and a strong base is basic."]
        }
        self.halt()

    @Rule(Fact(query_topic='neutral_salts__strong_acid___strong_base_'))
    def rule_neutral_salts__strong_acid___strong_base_(self):
        """Salts that are formed by the reaction between a strong acid and a strong base will exhibit neutral properties."""
        self.response = {
            'concept': 'Neutral Salts (Strong Acid + Strong Base)',
            'explanation': """Salts that are formed by the reaction between a strong acid and a strong base will exhibit neutral properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["Sodium chloride (NaCl) is a neutral salt formed from strong acid (HCl) and strong base (NaOH).", "Potassium chloride (KCl) is a neutral salt.", "Sodium nitrate (NaNO3) is a neutral salt."]
        }
        self.halt()

    @Rule(Fact(query_topic='properties_of_salts'))
    def rule_properties_of_salts(self):
        """Salts are crystalline, solid compounds that generally possess high melting points and boiling points. Most salts also exhibit solubility in water."""
        self.response = {
            'concept': 'Properties of Salts',
            'explanation': """Salts are crystalline, solid compounds that generally possess high melting points and boiling points. Most salts also exhibit solubility in water.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["Salts are crystalline solids.", "Most salts dissolve in water.", "Salts generally have high melting points."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_sodium_chloride'))
    def rule_uses_of_sodium_chloride(self):
        """Sodium chloride is a versatile salt used for flavoring and preserving food, producing various chemicals (such as chlorine, hydrochloric acid, and sodium hydroxide), manufacturing sodium carbonate via the Solvay process, glazing earthenware, making soap, and in tanning."""
        self.response = {
            'concept': 'Uses of Sodium Chloride',
            'explanation': """Sodium chloride is a versatile salt used for flavoring and preserving food, producing various chemicals (such as chlorine, hydrochloric acid, and sodium hydroxide), manufacturing sodium carbonate via the Solvay process, glazing earthenware, making soap, and in tanning.""",
            'topic': 'Chemistry',
            'subtopic': 'Uses of Salts',
            'examples': ["Used to flavour food during preparation.", "Used as a food preservative.", "Used to produce chemicals like chlorine and hydrochloric acid."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_copper_sulphate'))
    def rule_uses_of_copper_sulphate(self):
        """Copper sulphate is a salt utilized in agriculture as a fungicide, in the preparation of chemical reagents (like Benedict solution and Fehling solution), in electroplating processes, and within the paint industry."""
        self.response = {
            'concept': 'Uses of Copper Sulphate',
            'explanation': """Copper sulphate is a salt utilized in agriculture as a fungicide, in the preparation of chemical reagents (like Benedict solution and Fehling solution), in electroplating processes, and within the paint industry.""",
            'topic': 'Chemistry',
            'subtopic': 'Uses of Salts',
            'examples': ["Used as a fungicide in agriculture.", "Used in making chemical reagents (e.g., Benedict solution).", "Used in electroplating."]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralisation_reaction'))
    def rule_neutralisation_reaction(self):
        """Neutralisation is a chemical process where an acid reacts with a base to form salt and water. This reaction specifically involves the combination of H+ ions released by an acid with OH- ions released by a base to form water molecules, leading to the disappearance of both acidic and basic properties."""
        self.response = {
            'concept': 'Neutralisation Reaction',
            'explanation': """Neutralisation is a chemical process where an acid reacts with a base to form salt and water. This reaction specifically involves the combination of H+ ions released by an acid with OH- ions released by a base to form water molecules, leading to the disappearance of both acidic and basic properties.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid-Base Reactions',
            'examples': ["HCl (aq) + NaOH (aq) → NaCl(aq) + H2O (l)", "H⁺(aq) + OH⁻(aq) → H2O(l)", "Antacid tablets relieving stomach acidity."]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_of_stomach_acidity'))
    def rule_neutralization_of_stomach_acidity(self):
        """Stomach acidity is neutralized by a weak basic substance."""
        self.response = {
            'concept': 'Neutralization of Stomach Acidity',
            'explanation': """Stomach acidity is neutralized by a weak basic substance.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Neutralization',
            'examples': ["a weak base"]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_of_soil_acidity'))
    def rule_neutralization_of_soil_acidity(self):
        """Basic substances are added to soil to reduce soil acidity."""
        self.response = {
            'concept': 'Neutralization of Soil Acidity',
            'explanation': """Basic substances are added to soil to reduce soil acidity.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Neutralization',
            'examples': ["ash", "quicklime (calcium oxide)"]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_of_bee_sting'))
    def rule_neutralization_of_bee_sting(self):
        """Bee stings are painful due to an acidic poisonous substance; applying a weak basic substance relieves the pain."""
        self.response = {
            'concept': 'Neutralization of Bee Sting',
            'explanation': """Bee stings are painful due to an acidic poisonous substance; applying a weak basic substance relieves the pain.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Neutralization',
            'examples': ["baking soda (NaHCO3)", "calcium carbonate (CaCO3)"]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_of_wasp_sting'))
    def rule_neutralization_of_wasp_sting(self):
        """Wasp stings are basic; applying a weak, dilute acid reduces the venomous nature and pain."""
        self.response = {
            'concept': 'Neutralization of Wasp Sting',
            'explanation': """Wasp stings are basic; applying a weak, dilute acid reduces the venomous nature and pain.""",
            'topic': 'Chemistry',
            'subtopic': 'Applications of Neutralization',
            'examples': ["lime juice", "vinegar"]
        }
        self.halt()

    @Rule(Fact(query_topic='acids__definition_'))
    def rule_acids__definition_(self):
        """Substances that release H+ ions in aqueous solution."""
        self.response = {
            'concept': 'Acids (Definition)',
            'explanation': """Substances that release H+ ions in aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Definitions',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='bases__definition_'))
    def rule_bases__definition_(self):
        """Substances that increase the OH- ion concentration in aqueous solution."""
        self.response = {
            'concept': 'Bases (Definition)',
            'explanation': """Substances that increase the OH- ion concentration in aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Definitions',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='acid_base_reaction__overview_'))
    def rule_acid_base_reaction__overview_(self):
        """An acid reacts with a base to form salt and water."""
        self.response = {
            'concept': 'Acid-Base Reaction (Overview)',
            'explanation': """An acid reacts with a base to form salt and water.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='strong_acids'))
    def rule_strong_acids(self):
        """Acids that release H+ ions undergoing complete ionisation in aqueous solution."""
        self.response = {
            'concept': 'Strong Acids',
            'explanation': """Acids that release H+ ions undergoing complete ionisation in aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid and Base Strength',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='weak_acids'))
    def rule_weak_acids(self):
        """Acids that release H+ ions by partial ionisation in aqueous solution."""
        self.response = {
            'concept': 'Weak Acids',
            'explanation': """Acids that release H+ ions by partial ionisation in aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid and Base Strength',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='strong_bases'))
    def rule_strong_bases(self):
        """Bases that increase the OH- concentration undergoing complete ionisation in aqueous medium."""
        self.response = {
            'concept': 'Strong Bases',
            'explanation': """Bases that increase the OH- concentration undergoing complete ionisation in aqueous medium.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid and Base Strength',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='weak_bases'))
    def rule_weak_bases(self):
        """Bases that increase the OH- concentration by partial ionisation in aqueous solution."""
        self.response = {
            'concept': 'Weak Bases',
            'explanation': """Bases that increase the OH- concentration by partial ionisation in aqueous solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Acid and Base Strength',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='indicators'))
    def rule_indicators(self):
        """Both acids and bases change the colour of indicators."""
        self.response = {
            'concept': 'Indicators',
            'explanation': """Both acids and bases change the colour of indicators.""",
            'topic': 'Chemistry',
            'subtopic': 'Properties of Acids and Bases',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='ph_value_of_acids'))
    def rule_ph_value_of_acids(self):
        """An acid has a low pH value."""
        self.response = {
            'concept': 'pH Value of Acids',
            'explanation': """An acid has a low pH value.""",
            'topic': 'Chemistry',
            'subtopic': 'pH Scale',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='ph_value_of_bases'))
    def rule_ph_value_of_bases(self):
        """A base has a higher pH value."""
        self.response = {
            'concept': 'pH Value of Bases',
            'explanation': """A base has a higher pH value.""",
            'topic': 'Chemistry',
            'subtopic': 'pH Scale',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_acids_with_metals'))
    def rule_reaction_of_acids_with_metals(self):
        """Acids react with many metals liberating hydrogen gas."""
        self.response = {
            'concept': 'Reaction of Acids with Metals',
            'explanation': """Acids react with many metals liberating hydrogen gas.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions of Acids',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_acids_with_carbonates_bicarbonates'))
    def rule_reaction_of_acids_with_carbonates_bicarbonates(self):
        """Acids react with carbonates or bicarbonates with the evolution of carbon dioxide gas."""
        self.response = {
            'concept': 'Reaction of Acids with Carbonates/Bicarbonates',
            'explanation': """Acids react with carbonates or bicarbonates with the evolution of carbon dioxide gas.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions of Acids',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='salt_formation'))
    def rule_salt_formation(self):
        """Salts are formed by reacting an acid with a base."""
        self.response = {
            'concept': 'Salt Formation',
            'explanation': """Salts are formed by reacting an acid with a base.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='properties_of_salts'))
    def rule_properties_of_salts(self):
        """A salt can show acidic, basic, or neutral properties, depending on the strength of the acid or the base contributed to form the salt."""
        self.response = {
            'concept': 'Properties of Salts',
            'explanation': """A salt can show acidic, basic, or neutral properties, depending on the strength of the acid or the base contributed to form the salt.""",
            'topic': 'Chemistry',
            'subtopic': 'Salt Properties',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization__detailed_definition_'))
    def rule_neutralization__detailed_definition_(self):
        """The combination of H+ ions released by the acid with the OH- ions released by the base, to form water molecules."""
        self.response = {
            'concept': 'Neutralization (Detailed Definition)',
            'explanation': """The combination of H+ ions released by the acid with the OH- ions released by the base, to form water molecules.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='common_acids'))
    def rule_common_acids(self):
        """Frequently used acids for various purposes."""
        self.response = {
            'concept': 'Common Acids',
            'explanation': """Frequently used acids for various purposes.""",
            'topic': 'Chemistry',
            'subtopic': 'Examples of Acids',
            'examples': ["Hydrochloric acid", "sulphuric acid", "acetic acid"]
        }
        self.halt()

    @Rule(Fact(query_topic='common_bases'))
    def rule_common_bases(self):
        """Examples of bases."""
        self.response = {
            'concept': 'Common Bases',
            'explanation': """Examples of bases.""",
            'topic': 'Chemistry',
            'subtopic': 'Examples of Bases',
            'examples': ["Sodium hydroxide", "magnesium hydroxide"]
        }
        self.halt()

    @Rule(Fact(query_topic='salts__identification_and_usage'))
    def rule_salts__identification_and_usage(self):
        """Salts are ionic compounds typically formed from the neutralization reaction of an acid and a base, and they are utilized in various applications."""
        self.response = {
            'concept': 'Salts: Identification and Usage',
            'explanation': """Salts are ionic compounds typically formed from the neutralization reaction of an acid and a base, and they are utilized in various applications.""",
            'topic': 'Chemistry',
            'subtopic': 'Salts',
            'examples': ["Sodium chloride is a salt used for various tasks.", "Copper sulphate is a salt used for various tasks."]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralization_reactions'))
    def rule_neutralization_reactions(self):
        """A chemical reaction where an acid reacts with a base to produce a salt and water. This is a fundamental type of reaction in acid-base chemistry."""
        self.response = {
            'concept': 'Neutralization Reactions',
            'explanation': """A chemical reaction where an acid reacts with a base to produce a salt and water. This is a fundamental type of reaction in acid-base chemistry.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids, Bases, and Salts; Chemical Reactions',
            'examples': ["Sodium hydroxide and hydrochloric acid react to form sodium chloride and water.", "Potassium hydroxide and sulphuric acid react to form potassium sulphate and water.", "Nitric acid and magnesium hydroxide react to form magnesium nitrate and water."]
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_acids_with_carbonates'))
    def rule_reaction_of_acids_with_carbonates(self):
        """When an acid reacts with a metal carbonate, it typically produces a salt, water, and liberates carbon dioxide gas."""
        self.response = {
            'concept': 'Reaction of Acids with Carbonates',
            'explanation': """When an acid reacts with a metal carbonate, it typically produces a salt, water, and liberates carbon dioxide gas.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Reactions',
            'examples': ["Calcium carbonate and hydrochloric acid react liberating carbon dioxide gas.", "The reaction between sulfuric acid and calcium carbonate produces calcium sulfate, water, and carbon dioxide."]
        }
        self.halt()

    @Rule(Fact(query_topic='reaction_of_acids_with_active_metals'))
    def rule_reaction_of_acids_with_active_metals(self):
        """Acids react with certain active metals to liberate hydrogen gas and form a corresponding salt."""
        self.response = {
            'concept': 'Reaction of Acids with Active Metals',
            'explanation': """Acids react with certain active metals to liberate hydrogen gas and form a corresponding salt.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Reactions',
            'examples': ["Hydrochloric acid reacts with magnesium liberating hydrogen gas and forming magnesium chloride.", "Sulfuric acid reacts with iron, producing iron(II) sulfate and hydrogen gas."]
        }
        self.halt()

    @Rule(Fact(query_topic='litmus_test_for_solution_classification'))
    def rule_litmus_test_for_solution_classification(self):
        """Litmus paper is a pH indicator used to distinguish between acidic, basic, and neutral solutions. Acids turn blue litmus red, bases turn red litmus blue, and neutral solutions do not change the color of litmus."""
        self.response = {
            'concept': 'Litmus Test for Solution Classification',
            'explanation': """Litmus paper is a pH indicator used to distinguish between acidic, basic, and neutral solutions. Acids turn blue litmus red, bases turn red litmus blue, and neutral solutions do not change the color of litmus.""",
            'topic': 'Chemistry',
            'subtopic': 'Indicators; Acids, Bases, and Salts',
            'examples': ["Sodium hydroxide (base) turns red litmus blue.", "Dilute hydrochloric acid (acid) turns blue litmus red.", "Sodium chloride (neutral salt) does not change the color of litmus paper."]
        }
        self.halt()

    @Rule(Fact(query_topic='properties_of_acids_and_bases__ph_and_corrosivity_'))
    def rule_properties_of_acids_and_bases__ph_and_corrosivity_(self):
        """Acids and bases have distinct properties including their pH range and corrosive nature. Strong acids and bases are highly corrosive and can cause severe burns, with strong acids having very low pH and strong bases having very high pH."""
        self.response = {
            'concept': 'Properties of Acids and Bases (pH and Corrosivity)',
            'explanation': """Acids and bases have distinct properties including their pH range and corrosive nature. Strong acids and bases are highly corrosive and can cause severe burns, with strong acids having very low pH and strong bases having very high pH.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids, Bases, pH',
            'examples': ["Sulphuric acid causes severe burns in the skin when spilled.", "Solutions like sulphuric acid and hydrochloric acid act as strong acids.", "Solutions of ammonia (NH3) and calcium hydroxide (Ca(OH)2) have a pH greater than 7."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_scale_and_relative_strengths_of_solutions'))
    def rule_ph_scale_and_relative_strengths_of_solutions(self):
        """The pH scale is a logarithmic scale used to specify the acidity or alkalinity of an aqueous solution. Solutions with pH less than 7 are acidic, pH greater than 7 are basic, and pH equal to 7 is neutral. Stronger acids have lower pH and stronger bases have higher pH."""
        self.response = {
            'concept': 'pH Scale and Relative Strengths of Solutions',
            'explanation': """The pH scale is a logarithmic scale used to specify the acidity or alkalinity of an aqueous solution. Solutions with pH less than 7 are acidic, pH greater than 7 are basic, and pH equal to 7 is neutral. Stronger acids have lower pH and stronger bases have higher pH.""",
            'topic': 'Chemistry',
            'subtopic': 'pH; Acids, Bases',
            'examples': ["Solutions arranged in ascending order of pH: sulphuric acid, vinegar, water, sodium hydroxide.", "Solutions with a pH greater than 7 are basic.", "Water has a neutral pH of 7."]
        }
        self.halt()

    @Rule(Fact(query_topic='common_acids_and_bases'))
    def rule_common_acids_and_bases(self):
        """Identification of common acidic and basic substances found in daily life and in laboratory settings."""
        self.response = {
            'concept': 'Common Acids and Bases',
            'explanation': """Identification of common acidic and basic substances found in daily life and in laboratory settings.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Bases',
            'examples': ["Vinegar used at home is diluted acetic acid (CH3COOH).", "Sulphuric acid (H2SO4) and Hydrochloric acid (HCl) are examples of strong acids.", "Ammonia (NH3) solution and Calcium hydroxide (Ca(OH)2) solution are common bases."]
        }
        self.halt()

    @Rule(Fact(query_topic='formic_acid_skin_irritation'))
    def rule_formic_acid_skin_irritation(self):
        """Formic acid, found in plants like Kahambiliya, causes itching and a severe burning sensation upon skin contact. To relieve this sensation, a suitable substance (typically a mild base) should be applied to neutralize the acid."""
        self.response = {
            'concept': 'Formic Acid Skin Irritation',
            'explanation': """Formic acid, found in plants like Kahambiliya, causes itching and a severe burning sensation upon skin contact. To relieve this sensation, a suitable substance (typically a mild base) should be applied to neutralize the acid.""",
            'topic': 'Chemistry',
            'subtopic': 'Acids and Bases / Everyday Chemistry',
            'examples': ["Contact with the Kahambiliya plant causes itching and burning due to formic acid.", "Applying a basic substance like baking soda solution can relieve formic acid irritation on the skin."]
        }
        self.halt()

    @Rule(Fact(query_topic='acid'))
    def rule_acid(self):
        """A substance with specific chemical properties, often characterized by a sour taste, ability to turn litmus red, and reaction with bases to form salts. (Also provided are Sinhala 'wï,h' and Tamil 'Aª»®' translations)."""
        self.response = {
            'concept': 'Acid',
            'explanation': """A substance with specific chemical properties, often characterized by a sour taste, ability to turn litmus red, and reaction with bases to form salts. (Also provided are Sinhala 'wï,h' and Tamil 'Aª»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Chemistry Terms',
            'examples': ["Formic acid is an example of an acid.", "Acids typically have a pH less than 7.", "Acids react with carbonates to produce carbon dioxide."]
        }
        self.halt()

    @Rule(Fact(query_topic='base'))
    def rule_base(self):
        """A substance with specific chemical properties, often characterized by a bitter taste, a slippery feel, and reaction with acids to form salts. (Also provided are Sinhala 'Niauh' and Tamil '‰»®' translations)."""
        self.response = {
            'concept': 'Base',
            'explanation': """A substance with specific chemical properties, often characterized by a bitter taste, a slippery feel, and reaction with acids to form salts. (Also provided are Sinhala 'Niauh' and Tamil '‰»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Chemistry Terms',
            'examples': ["Sodium hydroxide (NaOH) is a strong base.", "Bases typically have a pH greater than 7.", "Bases can neutralize acids."]
        }
        self.halt()

    @Rule(Fact(query_topic='salt'))
    def rule_salt(self):
        """An ionic compound formed from the neutralization reaction of an acid and a base. (Also provided are Sinhala ',jK' and Tamil 'E¨¦' translations)."""
        self.response = {
            'concept': 'Salt',
            'explanation': """An ionic compound formed from the neutralization reaction of an acid and a base. (Also provided are Sinhala ',jK' and Tamil 'E¨¦' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Basic Chemistry Terms',
            'examples': ["Sodium chloride (table salt) is a common salt.", "Ammonium chloride (NH4Cl) is a salt.", "Salts are formed when the hydrogen ion of an acid is replaced by a metal ion or another cation."]
        }
        self.halt()

    @Rule(Fact(query_topic='neutralisation'))
    def rule_neutralisation(self):
        """A chemical reaction in which an acid and a base react to form a salt and water, typically resulting in a solution with a pH close to 7. (Also provided are Sinhala 'WÞiSkslrKh' and Tamil '|k{ø»¯õUP®' translations)."""
        self.response = {
            'concept': 'Neutralisation',
            'explanation': """A chemical reaction in which an acid and a base react to form a salt and water, typically resulting in a solution with a pH close to 7. (Also provided are Sinhala 'WÞiSkslrKh' and Tamil '|k{ø»¯õUP®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions',
            'examples': ["The reaction between hydrochloric acid and sodium hydroxide is a neutralisation reaction.", "Applying a base to an acid burn helps in neutralisation.", "Neutralisation is crucial in titrations to determine unknown concentrations."]
        }
        self.halt()

    @Rule(Fact(query_topic='strong_acid'))
    def rule_strong_acid(self):
        """An acid that completely dissociates or ionizes in water, releasing all its hydrogen ions (protons) into the solution. (Also provided are Sinhala 'm%n, wï,h' and Tamil 'ÁßÚª»®' translations)."""
        self.response = {
            'concept': 'Strong Acid',
            'explanation': """An acid that completely dissociates or ionizes in water, releasing all its hydrogen ions (protons) into the solution. (Also provided are Sinhala 'm%n, wï,h' and Tamil 'ÁßÚª»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Acid Strength',
            'examples': ["Hydrochloric acid (HCl) is a strong acid.", "Strong acids have very low pH values for a given concentration.", "Sulfuric acid (H2SO4) is another example of a strong acid."]
        }
        self.halt()

    @Rule(Fact(query_topic='weak_acid'))
    def rule_weak_acid(self):
        """An acid that only partially dissociates or ionizes in water, releasing only some of its hydrogen ions (protons) into the solution. (Also provided are Sinhala 'ÿn, wï,h' and Tamil 'ö©ßÚª»®' translations)."""
        self.response = {
            'concept': 'Weak Acid',
            'explanation': """An acid that only partially dissociates or ionizes in water, releasing only some of its hydrogen ions (protons) into the solution. (Also provided are Sinhala 'ÿn, wï,h' and Tamil 'ö©ßÚª»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Acid Strength',
            'examples': ["Formic acid is an example of a weak acid.", "Acetic acid (found in vinegar) is a common weak acid.", "Weak acids have higher pH values than strong acids of the same concentration."]
        }
        self.halt()

    @Rule(Fact(query_topic='strong_base'))
    def rule_strong_base(self):
        """A base that completely dissociates or ionizes in water, releasing all its hydroxide ions into the solution. (Also provided are Sinhala 'm%n, Niauh' and Tamil 'Áß ‰»®' translations)."""
        self.response = {
            'concept': 'Strong Base',
            'explanation': """A base that completely dissociates or ionizes in water, releasing all its hydroxide ions into the solution. (Also provided are Sinhala 'm%n, Niauh' and Tamil 'Áß ‰»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Base Strength',
            'examples': ["Sodium hydroxide (NaOH) is a strong base.", "Potassium hydroxide (KOH) is another strong base.", "Strong bases have very high pH values for a given concentration."]
        }
        self.halt()

    @Rule(Fact(query_topic='weak_base'))
    def rule_weak_base(self):
        """A base that only partially dissociates or ionizes in water, releasing only some of its hydroxide ions into the solution. (Also provided are Sinhala 'ÿn, Niauh' and Tamil 'ö©ß ‰»®' translations)."""
        self.response = {
            'concept': 'Weak Base',
            'explanation': """A base that only partially dissociates or ionizes in water, releasing only some of its hydroxide ions into the solution. (Also provided are Sinhala 'ÿn, Niauh' and Tamil 'ö©ß ‰»®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'Base Strength',
            'examples': ["Ammonia (NH3) is a weak base.", "Weak bases have lower pH values than strong bases of the same concentration.", "Methylamine is an example of a weak organic base."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_scale'))
    def rule_ph_scale(self):
        """A logarithmic scale used to specify the acidity or basicity of an aqueous solution, typically ranging from 0 to 14, where 7 is neutral, below 7 is acidic, and above 7 is basic. (Also provided are Sinhala 'pH mßudKh' and Tamil 'pH AÍÄzvmh®' translations)."""
        self.response = {
            'concept': 'pH Scale',
            'explanation': """A logarithmic scale used to specify the acidity or basicity of an aqueous solution, typically ranging from 0 to 14, where 7 is neutral, below 7 is acidic, and above 7 is basic. (Also provided are Sinhala 'pH mßudKh' and Tamil 'pH AÍÄzvmh®' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'pH Measurement',
            'examples': ["A solution with a pH of 2 is highly acidic.", "Pure water has a neutral pH of 7.", "The pH scale is essential for monitoring environmental and biological systems."]
        }
        self.halt()

    @Rule(Fact(query_topic='ph_papers'))
    def rule_ph_papers(self):
        """Strips of paper impregnated with chemical indicators that change color depending on the pH of the solution they are dipped into, providing a quick, though often less precise, way to estimate pH. (Also provided are Sinhala 'pH lvÞis' and Tamil 'pH uõÒ' translations)."""
        self.response = {
            'concept': 'pH Papers',
            'explanation': """Strips of paper impregnated with chemical indicators that change color depending on the pH of the solution they are dipped into, providing a quick, though often less precise, way to estimate pH. (Also provided are Sinhala 'pH lvÞis' and Tamil 'pH uõÒ' translations).""",
            'topic': 'Chemistry',
            'subtopic': 'pH Measurement',
            'examples': ["pH papers can be used to quickly test the acidity of rainwater.", "The color of pH paper is compared to a standard chart to determine the approximate pH.", "Using pH papers is a common method for initial pH checks in a laboratory."]
        }
        self.halt()

    @Rule(Fact(query_topic='heat_changes_associated_with_chemical_reactions'))
    def rule_heat_changes_associated_with_chemical_reactions(self):
        """Chemical reactions are frequently accompanied by energy changes, specifically in the form of heat, which can either be released (exothermic) or absorbed (endothermic) from the surroundings, causing temperature changes."""
        self.response = {
            'concept': 'Heat Changes Associated with Chemical Reactions',
            'explanation': """Chemical reactions are frequently accompanied by energy changes, specifically in the form of heat, which can either be released (exothermic) or absorbed (endothermic) from the surroundings, causing temperature changes.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry / Chemical Reactions',
            'examples': ["The dissolution of solid sodium hydroxide in water results in a temperature increase.", "Combustion reactions release significant amounts of heat.", "Photosynthesis is an example of a reaction that absorbs heat energy from the environment."]
        }
        self.halt()

    @Rule(Fact(query_topic='exothermic_dissolution'))
    def rule_exothermic_dissolution(self):
        """A process where a solid dissolves in a solvent (e.g., water) and releases heat into the surroundings, leading to an observable rise in the temperature of the solution."""
        self.response = {
            'concept': 'Exothermic Dissolution',
            'explanation': """A process where a solid dissolves in a solvent (e.g., water) and releases heat into the surroundings, leading to an observable rise in the temperature of the solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry / Dissolution',
            'examples': ["When solid sodium hydroxide dissolves in water, the temperature rises, indicating an exothermic process.", "Dissolving concentrated sulfuric acid in water is a highly exothermic process.", "Some ionic compounds release heat when they dissolve, warming the solution."]
        }
        self.halt()

    @Rule(Fact(query_topic='endothermic_dissolution'))
    def rule_endothermic_dissolution(self):
        """A process where a solid dissolves in a solvent (e.g., water) and absorbs heat from the surroundings, leading to an observable drop in the temperature of the solution."""
        self.response = {
            'concept': 'Endothermic Dissolution',
            'explanation': """A process where a solid dissolves in a solvent (e.g., water) and absorbs heat from the surroundings, leading to an observable drop in the temperature of the solution.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry / Dissolution',
            'examples': ["When solid ammonium chloride dissolves in water, the temperature falls, indicating an endothermic process.", "Dissolving potassium nitrate in water causes the solution to become cold.", "Many instant 'cold packs' utilize endothermic dissolution reactions."]
        }
        self.halt()

    @Rule(Fact(query_topic='evidences_of_a_chemical_reaction'))
    def rule_evidences_of_a_chemical_reaction(self):
        """Observable phenomena that indicate a chemical reaction has taken place, such as a change in temperature, formation of a gas, formation of a precipitate, or a change in color."""
        self.response = {
            'concept': 'Evidences of a Chemical Reaction',
            'explanation': """Observable phenomena that indicate a chemical reaction has taken place, such as a change in temperature, formation of a gas, formation of a precipitate, or a change in color.""",
            'topic': 'Chemistry',
            'subtopic': 'Chemical Reactions / Observation',
            'examples': ["A rise or fall in temperature is evidence of a chemical reaction.", "The appearance of bubbles indicates the formation of a gas, a sign of reaction.", "A change in the color of a solution often signals a chemical transformation."]
        }
        self.halt()

    @Rule(Fact(query_topic='temperature_change_and_heat_flow'))
    def rule_temperature_change_and_heat_flow(self):
        """The change in temperature observed in a process serves as a measure of the amount of heat that has been either evolved (released) or absorbed. A decrease in temperature indicates heat absorption, while an increase indicates heat evolution."""
        self.response = {
            'concept': 'Temperature Change and Heat Flow',
            'explanation': """The change in temperature observed in a process serves as a measure of the amount of heat that has been either evolved (released) or absorbed. A decrease in temperature indicates heat absorption, while an increase indicates heat evolution.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry Basics',
            'examples': ["Temperature decreased when solid ammonium chloride was dissolved in water, due to absorption of heat.", "Temperature increased when magnesium metal reacted with hydrochloric acid, due to evolution of heat."]
        }
        self.halt()

    @Rule(Fact(query_topic='exothermic_reactions'))
    def rule_exothermic_reactions(self):
        """Exothermic reactions are chemical reactions that occur with the evolution (release) of heat into their surroundings. This heat release typically causes the temperature of the reaction mixture to increase."""
        self.response = {
            'concept': 'Exothermic Reactions',
            'explanation': """Exothermic reactions are chemical reactions that occur with the evolution (release) of heat into their surroundings. This heat release typically causes the temperature of the reaction mixture to increase.""",
            'topic': 'Chemistry',
            'subtopic': 'Types of Chemical Reactions',
            'examples': ["The reaction between magnesium metal and dilute hydrochloric acid, where the temperature increases.", "Any reaction that can be simply represented as 'Reactants → Products + Heat'.", "Mg (s) + 2HCl (aq) → MgCl2 (aq) + H2 (g) + Heat."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_content_in_exothermic_reactions'))
    def rule_energy_content_in_exothermic_reactions(self):
        """For an exothermic reaction, the total energy contained within the products is less than the total energy content of the reactants. The excess energy is released as heat during the course of the reaction."""
        self.response = {
            'concept': 'Energy Content in Exothermic Reactions',
            'explanation': """For an exothermic reaction, the total energy contained within the products is less than the total energy content of the reactants. The excess energy is released as heat during the course of the reaction.""",
            'topic': 'Chemistry',
            'subtopic': 'Reaction Energetics',
            'examples': ["An energy level diagram for an exothermic reaction shows reactants at a higher energy level than products, with 'Energy is Released' in between.", "In the reaction Mg(s) + HCl(aq) → MgCl2(aq) + H2(g), the energy of MgCl2(aq) + H2(g) is less than Mg(s) + HCl(aq)."]
        }
        self.halt()

    @Rule(Fact(query_topic='endothermic_reaction'))
    def rule_endothermic_reaction(self):
        """A chemical reaction that absorbs heat from its surroundings, causing a decrease in the overall temperature of the system. In endothermic reactions, the energy contained within the products is greater than the energy contained within the reactants."""
        self.response = {
            'concept': 'Endothermic Reaction',
            'explanation': """A chemical reaction that absorbs heat from its surroundings, causing a decrease in the overall temperature of the system. In endothermic reactions, the energy contained within the products is greater than the energy contained within the reactants.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["The reaction between citric acid and sodium bicarbonate, where the temperature of the solution decreases.", "A general representation: Reactants + Heat → Products."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_level_diagram_for_endothermic_reactions'))
    def rule_energy_level_diagram_for_endothermic_reactions(self):
        """A graphical representation illustrating the energy changes in an endothermic reaction. It shows that the energy level of the products is higher than the energy level of the reactants, signifying that energy (heat) is absorbed during the reaction."""
        self.response = {
            'concept': 'Energy Level Diagram for Endothermic Reactions',
            'explanation': """A graphical representation illustrating the energy changes in an endothermic reaction. It shows that the energy level of the products is higher than the energy level of the reactants, signifying that energy (heat) is absorbed during the reaction.""",
            'topic': 'Chemistry',
            'subtopic': 'Energy Diagrams',
            'examples': ["A diagram where 'Reactants' are at a lower energy level and 'Products' are at a higher energy level, with an upward arrow indicating 'Energy is absorbed'.", "Visualizing the energy pathway where the system gains energy from the surroundings to form products."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_determination_of_heat_change'))
    def rule_experimental_determination_of_heat_change(self):
        """A practical methodology to quantitatively measure the heat change of a chemical reaction. This process typically involves recording initial temperatures of reactants, mixing them in an insulated container (such as a polystyrene cup), and observing the temperature change of the mixture."""
        self.response = {
            'concept': 'Experimental Determination of Heat Change',
            'explanation': """A practical methodology to quantitatively measure the heat change of a chemical reaction. This process typically involves recording initial temperatures of reactants, mixing them in an insulated container (such as a polystyrene cup), and observing the temperature change of the mixture.""",
            'topic': 'Chemistry',
            'subtopic': 'Experimental Chemistry',
            'examples': ["Determining the heat change for the reaction between sodium hydroxide solution and hydrochloric acid solution.", "Using a thermometer to measure the initial temperatures of separate solutions before mixing.", "Mixing solutions in a polystyrene cup and stirring with a glass rod to ensure even temperature distribution."]
        }
        self.halt()

    @Rule(Fact(query_topic='heat_change_equation'))
    def rule_heat_change_equation(self):
        """The heat change (Q) associated with a chemical reaction can be calculated using the formula Q = m c θ, where 'm' is the mass of the substance, 'c' is the specific heat capacity, and 'θ' is the temperature change."""
        self.response = {
            'concept': 'Heat Change Equation',
            'explanation': """The heat change (Q) associated with a chemical reaction can be calculated using the formula Q = m c θ, where 'm' is the mass of the substance, 'c' is the specific heat capacity, and 'θ' is the temperature change.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["Q = m c θ"]
        }
        self.halt()

    @Rule(Fact(query_topic='variables_in_heat_change_equation'))
    def rule_variables_in_heat_change_equation(self):
        """In the heat change equation Q = m c θ, 'm' represents the mass of the substance undergoing heat exchange, 'c' is the specific heat capacity of that substance, and 'θ' denotes the temperature change, calculated as the maximum temperature minus the initial temperature. If multiple initial temperatures are present for solutions, their mean should be used as the initial temperature."""
        self.response = {
            'concept': 'Variables in Heat Change Equation',
            'explanation': """In the heat change equation Q = m c θ, 'm' represents the mass of the substance undergoing heat exchange, 'c' is the specific heat capacity of that substance, and 'θ' denotes the temperature change, calculated as the maximum temperature minus the initial temperature. If multiple initial temperatures are present for solutions, their mean should be used as the initial temperature.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["m = Mass of the substance accompanying the exchange of heat", "c = Specific heat capacity of the substance related to the heat change", "θ = Temperature change in the mixture (maximum temperature - initial temperature)"]
        }
        self.halt()

    @Rule(Fact(query_topic='assumptions_for_heat_change_calculation__dilute_solutions_'))
    def rule_assumptions_for_heat_change_calculation__dilute_solutions_(self):
        """When calculating the heat change for reactions involving dilute solutions (e.g., sodium hydroxide and hydrochloric acid), it is assumed that the entire quantity of heat released by the reaction is used solely to raise the temperature of the solution. Additionally, it is assumed that the specific heat capacity of the solution is equal to that of water, and the density of the solution is equal to that of water."""
        self.response = {
            'concept': 'Assumptions for Heat Change Calculation (Dilute Solutions)',
            'explanation': """When calculating the heat change for reactions involving dilute solutions (e.g., sodium hydroxide and hydrochloric acid), it is assumed that the entire quantity of heat released by the reaction is used solely to raise the temperature of the solution. Additionally, it is assumed that the specific heat capacity of the solution is equal to that of water, and the density of the solution is equal to that of water.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["The entire quantity of heat of the reaction is used to raise the temperature of 100 cm3 of the solution.", "The specific heat capacity of the solution is equal to that of water.", "The density of the solution is equal to that of water."]
        }
        self.halt()

    @Rule(Fact(query_topic='standard_physical_properties_of_water'))
    def rule_standard_physical_properties_of_water(self):
        """For heat change calculations involving dilute aqueous solutions, standard physical properties of water are often used. These include water's specific heat capacity of 4200 J kg-1 °C-1 and its density of 1 g cm-3."""
        self.response = {
            'concept': 'Standard Physical Properties of Water',
            'explanation': """For heat change calculations involving dilute aqueous solutions, standard physical properties of water are often used. These include water's specific heat capacity of 4200 J kg-1 °C-1 and its density of 1 g cm-3.""",
            'topic': 'Chemistry',
            'subtopic': 'Physical Constants',
            'examples': ["Specific heat capacity of water = 4200 J kg-1 0C-1", "Density of water = 1 g cm-3", "Mass of 100 cm3 of water = 100 g"]
        }
        self.halt()

    @Rule(Fact(query_topic='example_calculation_of_heat_change__q_'))
    def rule_example_calculation_of_heat_change__q_(self):
        """An example demonstrating the calculation of heat change (Q) using the formula Q = m c θ, assuming a mass of 100g (0.1 kg) of water, its specific heat capacity (4200 J kg-1 °C-1), and an observed temperature change of 10 °C."""
        self.response = {
            'concept': 'Example Calculation of Heat Change (Q)',
            'explanation': """An example demonstrating the calculation of heat change (Q) using the formula Q = m c θ, assuming a mass of 100g (0.1 kg) of water, its specific heat capacity (4200 J kg-1 °C-1), and an observed temperature change of 10 °C.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Change Calculations',
            'examples': ["Q = 100 kg x 4200 J kg-1 0C-1 x 10 0C / 1000", "Q = 4200 J (for 0.1 kg water with 10 °C change)"]
        }
        self.halt()

    @Rule(Fact(query_topic='moles_calculation_from_concentration_and_volume__sodium_hydroxide_'))
    def rule_moles_calculation_from_concentration_and_volume__sodium_hydroxide_(self):
        """To determine the amount of moles of a substance like sodium hydroxide in a solution, multiply the molar concentration (mol dm-3) by the volume of the solution (converted to dm-3 or liters). For example, 50 cm3 is 0.050 dm3."""
        self.response = {
            'concept': 'Moles Calculation from Concentration and Volume (Sodium Hydroxide)',
            'explanation': """To determine the amount of moles of a substance like sodium hydroxide in a solution, multiply the molar concentration (mol dm-3) by the volume of the solution (converted to dm-3 or liters). For example, 50 cm3 is 0.050 dm3.""",
            'topic': 'Chemistry',
            'subtopic': 'Stoichiometry and Molarity',
            'examples': ["Amount of moles of NaOH in 50 cm3 of the 2 mol dm-3 NaOH solution = (2/1000) × 50 mol", "= 0.1 mol"]
        }
        self.halt()

    @Rule(Fact(query_topic='moles_calculation_from_concentration_and_volume__hydrochloric_acid_'))
    def rule_moles_calculation_from_concentration_and_volume__hydrochloric_acid_(self):
        """The amount of moles of a substance such as hydrochloric acid in a solution can be calculated by multiplying its molar concentration (mol dm-3) by the volume of the solution (converted to dm-3 or liters)."""
        self.response = {
            'concept': 'Moles Calculation from Concentration and Volume (Hydrochloric Acid)',
            'explanation': """The amount of moles of a substance such as hydrochloric acid in a solution can be calculated by multiplying its molar concentration (mol dm-3) by the volume of the solution (converted to dm-3 or liters).""",
            'topic': 'Chemistry',
            'subtopic': 'Stoichiometry and Molarity',
            'examples': ["Amount of moles of HCl in 50 cm3 of the 2 mol dm-3 HCl solution = (2/1000) × 50 mol", "= 0.1 mol"]
        }
        self.halt()

    @Rule(Fact(query_topic='heat_of_reaction_calculation'))
    def rule_heat_of_reaction_calculation(self):
        """The quantity of heat released or absorbed during a chemical reaction can be determined by scaling the heat change observed for a specific amount of reactants to their molar quantities. This value, often expressed per mole, is known as the heat of reaction."""
        self.response = {
            'concept': 'Heat of Reaction Calculation',
            'explanation': """The quantity of heat released or absorbed during a chemical reaction can be determined by scaling the heat change observed for a specific amount of reactants to their molar quantities. This value, often expressed per mole, is known as the heat of reaction.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry',
            'examples': ["The quantity of heat released when 0.1 mol of NaOH reacts with 0.1 mol of HCl = 4.2 kJ", "Quantity of heat released when 1.0 mol of NaOH reacts with 1.0 mol of HCl = 42 kJ mol-1", "This is the heat of reaction of the reaction between sodium hydroxide and hydrochloric acid."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_errors_in_heat_change_determination'))
    def rule_experimental_errors_in_heat_change_determination(self):
        """When experimentally measuring the heat change associated with a chemical reaction, common sources of error include the loss of heat to the surroundings and the absorption of heat by the reaction container. Ignoring these factors leads to inaccuracies in the calculated heat change."""
        self.response = {
            'concept': 'Experimental Errors in Heat Change Determination',
            'explanation': """When experimentally measuring the heat change associated with a chemical reaction, common sources of error include the loss of heat to the surroundings and the absorption of heat by the reaction container. Ignoring these factors leads to inaccuracies in the calculated heat change.""",
            'topic': 'Chemistry',
            'subtopic': 'Experimental Techniques',
            'examples': ["loss of heat to the surroundings", "absorption of heat by the container occur", "Neglecting these leads to an error in the calculation."]
        }
        self.halt()

    @Rule(Fact(query_topic='minimizing_errors_in_thermochemical_experiments'))
    def rule_minimizing_errors_in_thermochemical_experiments(self):
        """To minimize experimental errors in thermochemical measurements, such as heat loss or absorption, specific techniques should be employed. This includes using a thermally insulating container, like a polystyrene cup, and ensuring the mixture is well-stirred for uniform temperature distribution."""
        self.response = {
            'concept': 'Minimizing Errors in Thermochemical Experiments',
            'explanation': """To minimize experimental errors in thermochemical measurements, such as heat loss or absorption, specific techniques should be employed. This includes using a thermally insulating container, like a polystyrene cup, and ensuring the mixture is well-stirred for uniform temperature distribution.""",
            'topic': 'Chemistry',
            'subtopic': 'Experimental Techniques',
            'examples': ["a thermally insulating polystyrene cup is used", "the mixture should be stirred well with a stirrer or a glass rod", "To minimize it, a thermally insulating polystyrene cup is used."]
        }
        self.halt()

    @Rule(Fact(query_topic='importance_of_physical_states_in_thermochemical_equations'))
    def rule_importance_of_physical_states_in_thermochemical_equations(self):
        """The physical state (solid, liquid, gas, aqueous) of reactants and products directly influences the heat change accompanying a chemical reaction. Therefore, it is essential to indicate these physical states in thermochemical equations to accurately represent the reaction's energy changes."""
        self.response = {
            'concept': 'Importance of Physical States in Thermochemical Equations',
            'explanation': """The physical state (solid, liquid, gas, aqueous) of reactants and products directly influences the heat change accompanying a chemical reaction. Therefore, it is essential to indicate these physical states in thermochemical equations to accurately represent the reaction's energy changes.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry',
            'examples': ["HCl (aq) + NaOH(s) NaCl (aq) + H2O (l)", "the physical state of the reactants and the products should be indicated (Solid, liquid, gas, aqueous)", "the heat change here is different from the previous value (when using solid NaOH)"]
        }
        self.halt()

    @Rule(Fact(query_topic='exothermic_reactions_and_their_applications'))
    def rule_exothermic_reactions_and_their_applications(self):
        """Exothermic reactions are chemical processes that release energy, typically as heat, to their surroundings. These reactions are vital in various aspects of daily life, providing energy for biological functions, transportation, industry, and other activities."""
        self.response = {
            'concept': 'Exothermic Reactions and Their Applications',
            'explanation': """Exothermic reactions are chemical processes that release energy, typically as heat, to their surroundings. These reactions are vital in various aspects of daily life, providing energy for biological functions, transportation, industry, and other activities.""",
            'topic': 'Chemistry',
            'subtopic': 'Thermochemistry',
            'examples': ["burning fuels (Coal, bio gas (methane), and petrol)", "neutralisation reactions taking place between acids and bases", "Cellular respiration taking place in live bodies"]
        }
        self.halt()

    @Rule(Fact(query_topic='exothermic_reaction'))
    def rule_exothermic_reaction(self):
        """Reactions during which heat is released to the surroundings."""
        self.response = {
            'concept': 'Exothermic Reaction',
            'explanation': """Reactions during which heat is released to the surroundings.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["Adding water to quicklime: CaO (s) + H2O (l) → Ca(OH)2 (s)", "Burning of a candle", "Putting a piece of sodium into water"]
        }
        self.halt()

    @Rule(Fact(query_topic='endothermic_reaction'))
    def rule_endothermic_reaction(self):
        """Reactions in which heat is absorbed from the surroundings."""
        self.response = {
            'concept': 'Endothermic Reaction',
            'explanation': """Reactions in which heat is absorbed from the surroundings.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["Photosynthesis: 6CO2 (g) + 6H2O (l) → C6H12O6 (s) + 6O2 (g) (absorbing solar energy)", "Thermal decomposition of limestone: CaCO3 (s) → CaO (s) + CO2 (g)", "Dissolving the fertilizer urea in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='heat_change_in_chemical_reactions'))
    def rule_heat_change_in_chemical_reactions(self):
        """During every chemical reaction, a heat change also occurs, meaning heat is either released or absorbed."""
        self.response = {
            'concept': 'Heat Change in Chemical Reactions',
            'explanation': """During every chemical reaction, a heat change also occurs, meaning heat is either released or absorbed.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["Exothermic reactions release heat to the surroundings.", "Endothermic reactions absorb heat from the surroundings.", "The amount of heat released or absorbed can be quantified."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculation_of_heat_change__q___mcθ_'))
    def rule_calculation_of_heat_change__q___mcθ_(self):
        """The amount of heat released or absorbed during a reaction can be calculated using the equation Q = mcθ, where Q is heat change, m is mass, c is specific heat capacity, and θ is the temperature change."""
        self.response = {
            'concept': 'Calculation of Heat Change (Q = mcθ)',
            'explanation': """The amount of heat released or absorbed during a reaction can be calculated using the equation Q = mcθ, where Q is heat change, m is mass, c is specific heat capacity, and θ is the temperature change.""",
            'topic': 'Chemistry',
            'subtopic': 'Heat Changes Associated with Chemical Reactions',
            'examples': ["Calculating heat change when 40 cm³ of vinegar and 60 cm³ of lime water are mixed, and the temperature increases by 10 °C.", "Using the density of water (1000 kg m⁻³) to find the mass of the solution.", "Using the specific heat capacity of water (4200 J kg⁻¹ °C⁻¹) in the calculation."]
        }
        self.halt()

    @Rule(Fact(query_topic='textbook_target_audience_and_origin'))
    def rule_textbook_target_audience_and_origin(self):
        """This textbook is specifically compiled by the Educational Publications Department for Grade 11 students in the Sri Lankan school system, adhering to the 2016 syllabus prepared by the National Institute of Education."""
        self.response = {
            'concept': 'Textbook Target Audience and Origin',
            'explanation': """This textbook is specifically compiled by the Educational Publications Department for Grade 11 students in the Sri Lankan school system, adhering to the 2016 syllabus prepared by the National Institute of Education.""",
            'topic': 'Education',
            'subtopic': 'Textbook Demographics',
            'examples': ["For Grade 11 students", "Used in Sri Lankan schools", "Compiled by Educational Publications Department"]
        }
        self.halt()

    @Rule(Fact(query_topic='subject_content_alignment_principles'))
    def rule_subject_content_alignment_principles(self):
        """The subject content is arranged to align with national educational goals, common national competencies, the objectives of teaching science, and the overall syllabus content."""
        self.response = {
            'concept': 'Subject Content Alignment Principles',
            'explanation': """The subject content is arranged to align with national educational goals, common national competencies, the objectives of teaching science, and the overall syllabus content.""",
            'topic': 'Education',
            'subtopic': 'Curriculum Design',
            'examples': ["Suits national educational goals", "Matches common national competencies", "Follows science teaching objectives"]
        }
        self.halt()

    @Rule(Fact(query_topic='pedagogical_aim_of_science_education'))
    def rule_pedagogical_aim_of_science_education(self):
        """The science subject aims to guide students towards an active learning process, fostering the development of knowledge, skills, and attitudes essential for scientific thought."""
        self.response = {
            'concept': 'Pedagogical Aim of Science Education',
            'explanation': """The science subject aims to guide students towards an active learning process, fostering the development of knowledge, skills, and attitudes essential for scientific thought.""",
            'topic': 'Education',
            'subtopic': 'Learning Objectives',
            'examples': ["Directs to active learning", "Develops knowledge, skills, and attitudes", "Aims for developmental scientific thought"]
        }
        self.halt()

    @Rule(Fact(query_topic='chapter_structure_and_features'))
    def rule_chapter_structure_and_features(self):
        """Each chapter is structured around the main subject areas of Biology, Chemistry, and Physics, incorporating pictures, charts, graphs, activities, and assignments to enhance understanding."""
        self.response = {
            'concept': 'Chapter Structure and Features',
            'explanation': """Each chapter is structured around the main subject areas of Biology, Chemistry, and Physics, incorporating pictures, charts, graphs, activities, and assignments to enhance understanding.""",
            'topic': 'Education',
            'subtopic': 'Textbook Components',
            'examples': ["Covers Biology, Chemistry, Physics", "Includes pictures, charts, graphs", "Features activities and assignments"]
        }
        self.halt()

    @Rule(Fact(query_topic='end_of_chapter_assessment_and_review'))
    def rule_end_of_chapter_assessment_and_review(self):
        """Chapters conclude with a summary to help identify basic concepts and revise the subject matter, complemented by a series of exercises for self-evaluation of learning outcomes."""
        self.response = {
            'concept': 'End-of-Chapter Assessment and Review',
            'explanation': """Chapters conclude with a summary to help identify basic concepts and revise the subject matter, complemented by a series of exercises for self-evaluation of learning outcomes.""",
            'topic': 'Education',
            'subtopic': 'Formative Assessment',
            'examples': ["Summary for revision", "Exercises for self-evaluation", "Measures learning outcomes"]
        }
        self.halt()

    @Rule(Fact(query_topic='higher_order_skill_development_strategy'))
    def rule_higher_order_skill_development_strategy(self):
        """Various learning tools like activities, self-evaluative questions, solved examples, assignments, and exercises are designed to develop higher-order skills such as comprehension, application, analysis, synthesis, and evaluation."""
        self.response = {
            'concept': 'Higher Order Skill Development Strategy',
            'explanation': """Various learning tools like activities, self-evaluative questions, solved examples, assignments, and exercises are designed to develop higher-order skills such as comprehension, application, analysis, synthesis, and evaluation.""",
            'topic': 'Education',
            'subtopic': 'Cognitive Skill Enhancement',
            'examples': ["Develops comprehension, application, analysis", "Enhances synthesis and evaluation", "Utilizes solved examples and exercises"]
        }
        self.halt()

    @Rule(Fact(query_topic='supplemental_knowledge_section_purpose'))
    def rule_supplemental_knowledge_section_purpose(self):
        """The 'For extra knowledge' section provides additional information to broaden a student's understanding, explicitly stating that this content will not be subject to questions in term tests."""
        self.response = {
            'concept': 'Supplemental Knowledge Section Purpose',
            'explanation': """The 'For extra knowledge' section provides additional information to broaden a student's understanding, explicitly stating that this content will not be subject to questions in term tests.""",
            'topic': 'Education',
            'subtopic': 'Extended Learning',
            'examples': ["Broadens subject area", "Not for term tests", "Directs to study further"]
        }
        self.halt()

    @Rule(Fact(query_topic='activity_based_learning__abl_'))
    def rule_activity_based_learning__abl_(self):
        """Activity-based learning is a pedagogical approach that fosters a positive attitude towards learning science among students and aids in the effective establishment of scientific concepts."""
        self.response = {
            'concept': 'Activity-Based Learning (ABL)',
            'explanation': """Activity-based learning is a pedagogical approach that fosters a positive attitude towards learning science among students and aids in the effective establishment of scientific concepts.""",
            'topic': 'Science Education',
            'subtopic': 'Teaching Methodologies',
            'examples': ["Students conducting hands-on experiments to observe chemical reactions.", "Building a model of the solar system to understand planetary motion.", "Participating in a field trip to a botanical garden to study plant diversity."]
        }
        self.halt()

