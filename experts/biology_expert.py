"""
Biology Expert System
--------------------
Traditional Experta rule-based expert system for O/L Biology topics.
Uses @Rule decorators and inference engine.
Comprehensive knowledge base integrated from textbook.
"""

from experta import *


class BiologyExpert(KnowledgeEngine):
    """
    Expert system for Biology questions using traditional @Rule format.
    
    Topics covered (comprehensive):
    - Living Tissues (Plant & Animal)
    - Photosynthesis & Plant Nutrition
    - Respiration
    - Digestion
    - Cell Structure
    - Reproduction
    - And many more O/L Biology topics from the complete textbook knowledge base
    """
    
    def __init__(self):
        super().__init__()
        self.response = None
        self.needs_clarification = False
        self.clarification_question = None

    def get_response(self):
        """Return the expert's response."""
        return self.response
    
    def requires_clarification(self):
        """Check if expert needs more information."""
        return self.needs_clarification
    
    def get_clarification_question(self):
        """Get the clarification question to ask user."""
        return self.clarification_question

    # ==================== COMPREHENSIVE KNOWLEDGE BASE RULES ====================
    # Integrated from textbook knowledge base

    @Rule(Fact(query_topic='living_tissues'))

    # ==================== COMPREHENSIVE KNOWLEDGE BASE RULES ====================
    # Integrated from textbook knowledge base

    @Rule(Fact(query_topic='living_tissues'))
    def rule_living_tissues(self):
        """Living tissues represent one of the organizational levels found in multicellular organisms. They are formed when similar types of cells are arranged together, and these tissues can manifest in various forms in both plants and animals."""
        self.response = {
            'concept': 'Living Tissues',
            'explanation': """Living tissues represent one of the organizational levels found in multicellular organisms. They are formed when similar types of cells are arranged together, and these tissues can manifest in various forms in both plants and animals.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues',
            'examples': ["Plant tissues", "Animal tissues"]
        }
        self.halt()

    @Rule(Fact(query_topic='plant_tissues'))
    def rule_plant_tissues(self):
        """Plant tissues are specific forms of living tissues observed in plants. They are composed of different types of cells and can be studied by preparing and observing temporary slides under a microscope."""
        self.response = {
            'concept': 'Plant Tissues',
            'explanation': """Plant tissues are specific forms of living tissues observed in plants. They are composed of different types of cells and can be studied by preparing and observing temporary slides under a microscope.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Tissues from lower epidermis of betel leaf", "Tissues from a potato tuber", "Tissues from a Balsam stem"]
        }
        self.halt()

    @Rule(Fact(query_topic='activity_for_studying_plant_tissues__activity_1_1_'))
    def rule_activity_for_studying_plant_tissues__activity_1_1_(self):
        """Activity 1.1 outlines a practical method for studying plant tissues. It involves preparing temporary slides from various plant materials and then observing these slides under an optical microscope to identify the different tissue forms."""
        self.response = {
            'concept': 'Activity for Studying Plant Tissues (Activity 1.1)',
            'explanation': """Activity 1.1 outlines a practical method for studying plant tissues. It involves preparing temporary slides from various plant materials and then observing these slides under an optical microscope to identify the different tissue forms.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Preparing temporary slides from plant materials", "Observing prepared slides under microscope", "Identifying tissues formed by cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_tissue'))
    def rule_definition_of_tissue(self):
        """A tissue is defined as a group of cells that share a common origin and have been specialized or modified to perform particular functions within the body."""
        self.response = {
            'concept': 'Definition of Tissue',
            'explanation': """A tissue is defined as a group of cells that share a common origin and have been specialized or modified to perform particular functions within the body.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues',
            'examples': ["Epidermal tissue (e.g., from betel leaf)", "Storage tissue (e.g., from potato tuber)", "Vascular tissue (implied in stem cross section)"]
        }
        self.halt()

    @Rule(Fact(query_topic='plant_tissue_classification__by_cell_division_ability_'))
    def rule_plant_tissue_classification__by_cell_division_ability_(self):
        """Plant tissues can be broadly categorized into two main groups based on whether their cells retain the ability to divide: Meristematic tissues, which possess actively dividing cells, and Permanent tissues, which consist of differentiated cells that typically do not divide."""
        self.response = {
            'concept': 'Plant Tissue Classification (by cell division ability)',
            'explanation': """Plant tissues can be broadly categorized into two main groups based on whether their cells retain the ability to divide: Meristematic tissues, which possess actively dividing cells, and Permanent tissues, which consist of differentiated cells that typically do not divide.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Meristematic tissues contribute to plant growth in length and girth.", "Permanent tissues make up the bulk of mature plant structures like leaves and stems.", "This classification helps understand the developmental stages of a plant."]
        }
        self.halt()

    @Rule(Fact(query_topic='meristematic_tissues__definition_and_role_'))
    def rule_meristematic_tissues__definition_and_role_(self):
        """Meristematic tissues are composed of undifferentiated cells that actively divide by mitosis to produce new cells. These tissues are fundamental for the growth of plants, enabling them to increase in size and form new organs."""
        self.response = {
            'concept': 'Meristematic Tissues (Definition and Role)',
            'explanation': """Meristematic tissues are composed of undifferentiated cells that actively divide by mitosis to produce new cells. These tissues are fundamental for the growth of plants, enabling them to increase in size and form new organs.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["The growth of a root tip is due to the activity of meristematic tissues.", "Meristematic cells continually produce new cells for plant development.", "These tissues are responsible for both primary and secondary growth in plants."]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_meristematic_tissues'))
    def rule_features_of_meristematic_tissues(self):
        """Meristematic tissues exhibit specific characteristics including small-sized, living cells, an absence or non-prominence of intercellular spaces, the presence of a distinct nucleus in each cell, the absence of a large central vacuole (though small ones may be present), the absence of chloroplasts, and a large number of mitochondria."""
        self.response = {
            'concept': 'Features of Meristematic Tissues',
            'explanation': """Meristematic tissues exhibit specific characteristics including small-sized, living cells, an absence or non-prominence of intercellular spaces, the presence of a distinct nucleus in each cell, the absence of a large central vacuole (though small ones may be present), the absence of chloroplasts, and a large number of mitochondria.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["The small cell size and lack of large vacuoles facilitate rapid cell division.", "A prominent nucleus indicates active metabolic and genetic processes.", "Numerous mitochondria provide the ample energy required for continuous cell division."]
        }
        self.halt()

    @Rule(Fact(query_topic='root_apex_organization_and_tissue_distribution'))
    def rule_root_apex_organization_and_tissue_distribution(self):
        """Externally, the growing part of a root is soft and light-coloured, while the mature part is rough and dark-coloured. Microscopically, the root apex shows distinct regions: region A-A' contains meristematic tissues (cells with the ability to divide), and region B-B' contains permanent tissues (different types of differentiated cells)."""
        self.response = {
            'concept': 'Root Apex Organization and Tissue Distribution',
            'explanation': """Externally, the growing part of a root is soft and light-coloured, while the mature part is rough and dark-coloured. Microscopically, the root apex shows distinct regions: region A-A' contains meristematic tissues (cells with the ability to divide), and region B-B' contains permanent tissues (different types of differentiated cells).""",
            'topic': 'Biology',
            'subtopic': 'Plant Anatomy / Root Structure',
            'examples': ["The soft tip of a root is where meristematic tissues are actively dividing.", "Region A-A' in a root longitudinal section represents the area of active cell proliferation.", "Differentiated permanent tissues are found in the more mature sections of the root, corresponding to region B-B'."]
        }
        self.halt()

    @Rule(Fact(query_topic='apical_meristems'))
    def rule_apical_meristems(self):
        """Apical meristems are found in shoot apex, root apex and axillary buds. Plant increases its height due to the activity of this tissue."""
        self.response = {
            'concept': 'Apical Meristems',
            'explanation': """Apical meristems are found in shoot apex, root apex and axillary buds. Plant increases its height due to the activity of this tissue.""",
            'topic': 'Biology',
            'subtopic': 'Meristematic Tissues',
            'examples': ["shoot apex", "root apex", "axillary buds"]
        }
        self.halt()

    @Rule(Fact(query_topic='intercalary_meristems'))
    def rule_intercalary_meristems(self):
        """Intercalary meristems are found at nodes. The length of internode increases due to the activity of this tissue. They are found in plants of the grass family."""
        self.response = {
            'concept': 'Intercalary Meristems',
            'explanation': """Intercalary meristems are found at nodes. The length of internode increases due to the activity of this tissue. They are found in plants of the grass family.""",
            'topic': 'Biology',
            'subtopic': 'Meristematic Tissues',
            'examples': ["nodes", "grass family plants"]
        }
        self.halt()

    @Rule(Fact(query_topic='lateral_meristems'))
    def rule_lateral_meristems(self):
        """Lateral meristems are present laterally in the stem and roots of plants. They are found parallel to the longitudinal axis of the plant. The diameter of the plant increases due to the activity of this tissue. Cambium tissue found in dicots is a lateral meristematic tissue."""
        self.response = {
            'concept': 'Lateral Meristems',
            'explanation': """Lateral meristems are present laterally in the stem and roots of plants. They are found parallel to the longitudinal axis of the plant. The diameter of the plant increases due to the activity of this tissue. Cambium tissue found in dicots is a lateral meristematic tissue.""",
            'topic': 'Biology',
            'subtopic': 'Meristematic Tissues',
            'examples': ["stem", "roots", "cambium tissue (in dicots)"]
        }
        self.halt()

    @Rule(Fact(query_topic='permanent_tissue'))
    def rule_permanent_tissue(self):
        """A tissue that lost its ability to divide and specialized to perform a particular function is known as a permanent tissue."""
        self.response = {
            'concept': 'Permanent Tissue',
            'explanation': """A tissue that lost its ability to divide and specialized to perform a particular function is known as a permanent tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Simple Permanent tissues", "Complex Permanent tissues"]
        }
        self.halt()

    @Rule(Fact(query_topic='simple_permanent_tissues'))
    def rule_simple_permanent_tissues(self):
        """Simple permanent tissues are composed of similar cells, meaning one type of cells collected together. According to the shape of the cell and the nature of the cell wall, three types can be identified in plants."""
        self.response = {
            'concept': 'Simple Permanent Tissues',
            'explanation': """Simple permanent tissues are composed of similar cells, meaning one type of cells collected together. According to the shape of the cell and the nature of the cell wall, three types can be identified in plants.""",
            'topic': 'Biology',
            'subtopic': 'Permanent Tissues',
            'examples': ["parenchyma", "collenchyma", "sclerenchyma"]
        }
        self.halt()

    @Rule(Fact(query_topic='complex_permanent_tissues'))
    def rule_complex_permanent_tissues(self):
        """Complex permanent tissues are formed when different types of cells are collected together."""
        self.response = {
            'concept': 'Complex Permanent Tissues',
            'explanation': """Complex permanent tissues are formed when different types of cells are collected together.""",
            'topic': 'Biology',
            'subtopic': 'Permanent Tissues',
            'examples': ["xylem", "phloem"]
        }
        self.halt()

    @Rule(Fact(query_topic='parenchyma'))
    def rule_parenchyma(self):
        """Parenchyma tissue forms the soft parts of the plant body. This is the most abundant tissue."""
        self.response = {
            'concept': 'Parenchyma',
            'explanation': """Parenchyma tissue forms the soft parts of the plant body. This is the most abundant tissue.""",
            'topic': 'Biology',
            'subtopic': 'Simple Permanent Tissues',
            'examples': ["soft parts of the plant body", "fruit pulp", "leaf mesophyll"]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_parenchyma_tissue'))
    def rule_features_of_parenchyma_tissue(self):
        """Parenchyma tissue consists of living, isodiametric (spherical) cells with a large central vacuole and a peripherally located nucleus. The cell wall is thin, made of cellulose, and intercellular spaces are present."""
        self.response = {
            'concept': 'Features of Parenchyma Tissue',
            'explanation': """Parenchyma tissue consists of living, isodiametric (spherical) cells with a large central vacuole and a peripherally located nucleus. The cell wall is thin, made of cellulose, and intercellular spaces are present.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Living cells", "Isodiametric (spherical) cells with large central vacuole", "Thin primary cellulose cell wall"]
        }
        self.halt()

    @Rule(Fact(query_topic='locations_of_parenchyma_tissues'))
    def rule_locations_of_parenchyma_tissues(self):
        """Parenchyma tissues are found in various parts of plants, including the cortex and pith of plant stems and roots, fleshy parts of fruits, seeds (endosperm), and leaves (mesophylls)."""
        self.response = {
            'concept': 'Locations of Parenchyma Tissues',
            'explanation': """Parenchyma tissues are found in various parts of plants, including the cortex and pith of plant stems and roots, fleshy parts of fruits, seeds (endosperm), and leaves (mesophylls).""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Cortex and pith of plant stem", "Fleshy parts of fruits", "Leaves (mesophylls)"]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_parenchyma__photosynthesis'))
    def rule_function_of_parenchyma__photosynthesis(self):
        """Palisade and spongy mesophylls in plant leaves, which are types of parenchyma, contain chlorophyll within chloroplasts, where photosynthesis takes place."""
        self.response = {
            'concept': 'Function of Parenchyma: Photosynthesis',
            'explanation': """Palisade and spongy mesophylls in plant leaves, which are types of parenchyma, contain chlorophyll within chloroplasts, where photosynthesis takes place.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues Functions',
            'examples': ["Palisade mesophylls in leaves", "Spongy mesophylls in leaves", "Chlorophyll within chloroplasts"]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_parenchyma__food_storage'))
    def rule_function_of_parenchyma__food_storage(self):
        """Some parenchyma tissues specialize in storing food and are referred to as storage tissues."""
        self.response = {
            'concept': 'Function of Parenchyma: Food Storage',
            'explanation': """Some parenchyma tissues specialize in storing food and are referred to as storage tissues.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues Functions',
            'examples': ["Potato tuber", "Carrot roots", "Papaw fruits"]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_parenchyma__water_storage'))
    def rule_function_of_parenchyma__water_storage(self):
        """Xerophytic plants specifically store water in their parenchyma tissue as an adaptation."""
        self.response = {
            'concept': 'Function of Parenchyma: Water Storage',
            'explanation': """Xerophytic plants specifically store water in their parenchyma tissue as an adaptation.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues Functions',
            'examples': ["Aloe leaves", "Bryophyllum leaves", "Cactus cladode"]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_parenchyma__providing_support'))
    def rule_function_of_parenchyma__providing_support(self):
        """In herbaceous plants like Balsam, parenchyma cells absorb water into their vacuoles, becoming turgid and thereby providing mechanical support to the plant."""
        self.response = {
            'concept': 'Function of Parenchyma: Providing Support',
            'explanation': """In herbaceous plants like Balsam, parenchyma cells absorb water into their vacuoles, becoming turgid and thereby providing mechanical support to the plant.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues Functions',
            'examples': ["Balsam (herbaceous plant)", "Water absorption into vacuoles", "Turgid cells providing support"]
        }
        self.halt()

    @Rule(Fact(query_topic='collenchyma_tissue_definition_and_role'))
    def rule_collenchyma_tissue_definition_and_role(self):
        """Collenchyma tissue provides mechanical strength and support to the plant body. They are considered modified parenchyma cells specialized for this structural function."""
        self.response = {
            'concept': 'Collenchyma Tissue Definition and Role',
            'explanation': """Collenchyma tissue provides mechanical strength and support to the plant body. They are considered modified parenchyma cells specialized for this structural function.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Provides mechanical strength", "Supports the plant body", "Modified parenchyma cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_collenchyma_tissue'))
    def rule_features_of_collenchyma_tissue(self):
        """Collenchyma tissue consists of living cells, possessing a cytoplasm, nucleus, and central vacuole. Cells are generally elongated and polygonal in cross-section, with conspicuously thickened corners of the cell walls. Intercellular spaces may or may not be present."""
        self.response = {
            'concept': 'Features of Collenchyma Tissue',
            'explanation': """Collenchyma tissue consists of living cells, possessing a cytoplasm, nucleus, and central vacuole. Cells are generally elongated and polygonal in cross-section, with conspicuously thickened corners of the cell walls. Intercellular spaces may or may not be present.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Living cells with nucleus and vacuole", "Elongated and polygonal in cross-section", "Thickened corners of the cell walls"]
        }
        self.halt()

    @Rule(Fact(query_topic='locations_of_collenchyma'))
    def rule_locations_of_collenchyma(self):
        """Collenchyma tissue is found forming a cylindrical layer inner to the epidermis of herbaceous stems and within the veins of dicot leaves."""
        self.response = {
            'concept': 'Locations of Collenchyma',
            'explanation': """Collenchyma tissue is found forming a cylindrical layer inner to the epidermis of herbaceous stems and within the veins of dicot leaves.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Collenchyma',
            'examples': ["Inner to the epidermis of herbaceous stems", "Veins of dicot leaves"]
        }
        self.halt()

    @Rule(Fact(query_topic='support_function_of_collenchyma'))
    def rule_support_function_of_collenchyma(self):
        """Collenchyma provides mechanical support to dicot plant stems before the formation of wood, as well as to plant leaves via the collenchyma in veins. It also supports herbs."""
        self.response = {
            'concept': 'Support Function of Collenchyma',
            'explanation': """Collenchyma provides mechanical support to dicot plant stems before the formation of wood, as well as to plant leaves via the collenchyma in veins. It also supports herbs.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Collenchyma Functions',
            'examples': ["Supporting dicot stems before wood formation", "Supporting plant leaves", "Providing mechanical support to herbs"]
        }
        self.halt()

    @Rule(Fact(query_topic='photosynthesis_function_of_collenchyma'))
    def rule_photosynthesis_function_of_collenchyma(self):
        """Chloroplasts are present in the collenchyma of immature dicot stems, enabling these cells to perform photosynthesis."""
        self.response = {
            'concept': 'Photosynthesis Function of Collenchyma',
            'explanation': """Chloroplasts are present in the collenchyma of immature dicot stems, enabling these cells to perform photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Collenchyma Functions',
            'examples': ["Chloroplasts in immature dicot stems carry out photosynthesis", "Immature dicot stem collenchyma cells producing food"]
        }
        self.halt()

    @Rule(Fact(query_topic='sclerenchyma_tissue_overview'))
    def rule_sclerenchyma_tissue_overview(self):
        """Sclerenchyma tissue provides mechanical strength and support to the plant body. It is composed of two types of cells: sclereids and sclerenchyma fibres."""
        self.response = {
            'concept': 'Sclerenchyma Tissue Overview',
            'explanation': """Sclerenchyma tissue provides mechanical strength and support to the plant body. It is composed of two types of cells: sclereids and sclerenchyma fibres.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Sclerenchyma',
            'examples': ["Provides mechanical strength to plants", "Supports the plant body", "Composed of sclereids and fibres"]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_sclerenchyma_tissue'))
    def rule_features_of_sclerenchyma_tissue(self):
        """Sclerenchyma tissue consists of dead cells with lignin deposited on their cellulose cell walls. The cells are tightly packed, lacking intercellular spaces, and have evenly thickened cell walls that form a central lumen."""
        self.response = {
            'concept': 'Features of Sclerenchyma Tissue',
            'explanation': """Sclerenchyma tissue consists of dead cells with lignin deposited on their cellulose cell walls. The cells are tightly packed, lacking intercellular spaces, and have evenly thickened cell walls that form a central lumen.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Sclerenchyma Features',
            'examples': ["Consists of dead cells", "Lignified cell walls", "No intercellular spaces"]
        }
        self.halt()

    @Rule(Fact(query_topic='locations_of_sclerenchyma_fibres'))
    def rule_locations_of_sclerenchyma_fibres(self):
        """Sclerenchyma fibres are found as xylem fibres within xylem and phloem fibres within phloem. They are also present in structures like coconut fibres, agave fibres, and cotton wool."""
        self.response = {
            'concept': 'Locations of Sclerenchyma Fibres',
            'explanation': """Sclerenchyma fibres are found as xylem fibres within xylem and phloem fibres within phloem. They are also present in structures like coconut fibres, agave fibres, and cotton wool.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Sclerenchyma Locations',
            'examples': ["Xylem fibres", "Phloem fibres", "Coconut fibres"]
        }
        self.halt()

    @Rule(Fact(query_topic='locations_of_sclereids'))
    def rule_locations_of_sclereids(self):
        """Sclereids are found in various plant parts including the endocarp of coconut, Kaduru, and mango fruits, the pericarp of guava fruit, pear fruit, and the seed coat of coffee and dates."""
        self.response = {
            'concept': 'Locations of Sclereids',
            'explanation': """Sclereids are found in various plant parts including the endocarp of coconut, Kaduru, and mango fruits, the pericarp of guava fruit, pear fruit, and the seed coat of coffee and dates.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Sclerenchyma Locations',
            'examples': ["Endocarp of coconut", "Pericarp of guava fruit", "Seed coat of coffee"]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_sclerenchyma'))
    def rule_function_of_sclerenchyma(self):
        """Sclerenchyma tissue primarily functions to provide support to the plant body."""
        self.response = {
            'concept': 'Function of Sclerenchyma',
            'explanation': """Sclerenchyma tissue primarily functions to provide support to the plant body.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Sclerenchyma Functions',
            'examples': ["Provides support to plant stems", "Strengthens fruit rinds"]
        }
        self.halt()

    @Rule(Fact(query_topic='complex_permanent_tissues'))
    def rule_complex_permanent_tissues(self):
        """Complex permanent tissues are formed by different types of cells working together to perform specific functions. Xylem and phloem are two examples of complex permanent tissues found in plants."""
        self.response = {
            'concept': 'Complex Permanent Tissues',
            'explanation': """Complex permanent tissues are formed by different types of cells working together to perform specific functions. Xylem and phloem are two examples of complex permanent tissues found in plants.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Complex Permanent Tissues',
            'examples': ["Xylem", "Phloem"]
        }
        self.halt()

    @Rule(Fact(query_topic='locations_of_xylem_and_phloem'))
    def rule_locations_of_xylem_and_phloem(self):
        """Xylem and phloem, which are complex permanent tissues, are found within the vascular systems of the root, stem, and leaves of plants."""
        self.response = {
            'concept': 'Locations of Xylem and Phloem',
            'explanation': """Xylem and phloem, which are complex permanent tissues, are found within the vascular systems of the root, stem, and leaves of plants.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Complex Permanent Tissues',
            'examples': ["Vascular systems of roots", "Vascular systems of stems", "Vascular systems of leaves"]
        }
        self.halt()

    @Rule(Fact(query_topic='xylem_tissue'))
    def rule_xylem_tissue(self):
        """This tissue is composed of four different types of cells: xylem vessel elements, tracheids, fibres, and parenchyma cells. Its primary functions are the transportation of water and minerals and providing mechanical support to the plant body."""
        self.response = {
            'concept': 'Xylem tissue',
            'explanation': """This tissue is composed of four different types of cells: xylem vessel elements, tracheids, fibres, and parenchyma cells. Its primary functions are the transportation of water and minerals and providing mechanical support to the plant body.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Transports water and minerals to the plant body", "Provides mechanical support to plant body"]
        }
        self.halt()

    @Rule(Fact(query_topic='xylem_vessel_element'))
    def rule_xylem_vessel_element(self):
        """Cylindrical, elongated cells that stack on top of others. Their cross walls are dissolved to form a continuous xylem vessel. This tubular structure helps in the transportation of water in plants. They become dead due to lignification of cell walls."""
        self.response = {
            'concept': 'Xylem vessel element',
            'explanation': """Cylindrical, elongated cells that stack on top of others. Their cross walls are dissolved to form a continuous xylem vessel. This tubular structure helps in the transportation of water in plants. They become dead due to lignification of cell walls.""",
            'topic': 'Biology',
            'subtopic': 'Xylem Tissue Components',
            'examples': ["Forms a continuous xylem vessel", "Helps in transportation of water"]
        }
        self.halt()

    @Rule(Fact(query_topic='tracheids'))
    def rule_tracheids(self):
        """Elongated, spindle-shaped cells that also help in the transportation of water. They become dead due to lignification of cell walls."""
        self.response = {
            'concept': 'Tracheids',
            'explanation': """Elongated, spindle-shaped cells that also help in the transportation of water. They become dead due to lignification of cell walls.""",
            'topic': 'Biology',
            'subtopic': 'Xylem Tissue Components',
            'examples': ["Helps in transportation of water", "Are elongated, spindle shaped cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='xylem_fibres'))
    def rule_xylem_fibres(self):
        """Cells that are narrower and shorter than tracheids. They become dead due to lignification of cell walls and provide support to the xylem tissue."""
        self.response = {
            'concept': 'Xylem Fibres',
            'explanation': """Cells that are narrower and shorter than tracheids. They become dead due to lignification of cell walls and provide support to the xylem tissue.""",
            'topic': 'Biology',
            'subtopic': 'Xylem Tissue Components',
            'examples': ["Provide support to the xylem tissue", "Are narrower and shorter than tracheids"]
        }
        self.halt()

    @Rule(Fact(query_topic='xylem_parenchyma'))
    def rule_xylem_parenchyma(self):
        """Living cells with a thin cell wall, primarily involved in food storage."""
        self.response = {
            'concept': 'Xylem Parenchyma',
            'explanation': """Living cells with a thin cell wall, primarily involved in food storage.""",
            'topic': 'Biology',
            'subtopic': 'Xylem Tissue Components',
            'examples': ["Involve in food storage", "Are living cells with a thin cell wall"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_xylem'))
    def rule_functions_of_xylem(self):
        """The two main functions of xylem tissue include the transportation of water and minerals to the plant body (absorbed by plant roots) and providing mechanical support to the plant body."""
        self.response = {
            'concept': 'Functions of Xylem',
            'explanation': """The two main functions of xylem tissue include the transportation of water and minerals to the plant body (absorbed by plant roots) and providing mechanical support to the plant body.""",
            'topic': 'Biology',
            'subtopic': 'Xylem Tissue',
            'examples': ["Transportation of water and minerals to the plant body", "Providing of mechanical support to plant body"]
        }
        self.halt()

    @Rule(Fact(query_topic='phloem_tissue'))
    def rule_phloem_tissue(self):
        """This tissue is composed of four different types of cells: sieve tube elements, companion cells, phloem fibres, and phloem parenchyma."""
        self.response = {
            'concept': 'Phloem tissue',
            'explanation': """This tissue is composed of four different types of cells: sieve tube elements, companion cells, phloem fibres, and phloem parenchyma.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Composed of sieve tube elements and companion cells", "Transports food throughout the plant"]
        }
        self.halt()

    @Rule(Fact(query_topic='sieve_tube_elements'))
    def rule_sieve_tube_elements(self):
        """These cells fuse end to end, and their cross walls are incompletely dissolved to form a sieve tube. They lack a nucleus, and their activities are controlled by the nucleus of an associated companion cell. They are living cells."""
        self.response = {
            'concept': 'Sieve tube elements',
            'explanation': """These cells fuse end to end, and their cross walls are incompletely dissolved to form a sieve tube. They lack a nucleus, and their activities are controlled by the nucleus of an associated companion cell. They are living cells.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Form a sieve tube when fused end to end", "Lack a nucleus"]
        }
        self.halt()

    @Rule(Fact(query_topic='sieve_plates'))
    def rule_sieve_plates(self):
        """These are the incompletely dissolved cross walls found in sieve tubes."""
        self.response = {
            'concept': 'Sieve plates',
            'explanation': """These are the incompletely dissolved cross walls found in sieve tubes.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Are cross walls in sieve tubes", "Are incompletely dissolved"]
        }
        self.halt()

    @Rule(Fact(query_topic='sieve_tubes'))
    def rule_sieve_tubes(self):
        """Tubular structures formed by the fusion of sieve tube elements. They transport food (mainly sucrose) as a solution throughout the plant."""
        self.response = {
            'concept': 'Sieve tubes',
            'explanation': """Tubular structures formed by the fusion of sieve tube elements. They transport food (mainly sucrose) as a solution throughout the plant.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Transport food (mainly sucrose) throughout the plant", "Formed from sieve tube elements"]
        }
        self.halt()

    @Rule(Fact(query_topic='companion_cells'))
    def rule_companion_cells(self):
        """Elongated, living cells closely associated with sieve tube elements. The nucleus of a companion cell controls the activities of the sieve tube elements."""
        self.response = {
            'concept': 'Companion cells',
            'explanation': """Elongated, living cells closely associated with sieve tube elements. The nucleus of a companion cell controls the activities of the sieve tube elements.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Control the activities of sieve tube elements", "Are elongated cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='phloem_fibres'))
    def rule_phloem_fibres(self):
        """Components of phloem tissue that are dead cells."""
        self.response = {
            'concept': 'Phloem Fibres',
            'explanation': """Components of phloem tissue that are dead cells.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Are dead cells", "Are part of phloem tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='phloem_parenchyma'))
    def rule_phloem_parenchyma(self):
        """Living cells that are part of the phloem tissue."""
        self.response = {
            'concept': 'Phloem Parenchyma',
            'explanation': """Living cells that are part of the phloem tissue.""",
            'topic': 'Biology',
            'subtopic': 'Phloem Tissue Components',
            'examples': ["Are living cells", "Are part of phloem tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_phloem_tissue'))
    def rule_functions_of_phloem_tissue(self):
        """The food synthesized in the leaves is transported throughout the plant body by this tissue, a process known as Translocation."""
        self.response = {
            'concept': 'Functions of Phloem tissue',
            'explanation': """The food synthesized in the leaves is transported throughout the plant body by this tissue, a process known as Translocation.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Transportation of synthesized food", "Translocation"]
        }
        self.halt()

    @Rule(Fact(query_topic='animal_tissues'))
    def rule_animal_tissues(self):
        """The animal body is made up of different types of cells, which form groups with a common origin to perform a particular function in multicellular animal bodies."""
        self.response = {
            'concept': 'Animal Tissues',
            'explanation': """The animal body is made up of different types of cells, which form groups with a common origin to perform a particular function in multicellular animal bodies.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["The human body is made up of about 210 different types of cells.", "Epithelial tissue", "Connective tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='main_types_of_animal_tissues'))
    def rule_main_types_of_animal_tissues(self):
        """Multicellular animal bodies are primarily composed of a few main types of tissues, each specialized for distinct functions."""
        self.response = {
            'concept': 'Main Types of Animal Tissues',
            'explanation': """Multicellular animal bodies are primarily composed of a few main types of tissues, each specialized for distinct functions.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Epithelial tissue", "Connective tissue", "Muscle tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='epithelial_tissue'))
    def rule_epithelial_tissue(self):
        """This tissue lines the free surfaces (both internal and external) of the vertebrate body. It can be composed of a single layer of cells or several cell layers."""
        self.response = {
            'concept': 'Epithelial tissue',
            'explanation': """This tissue lines the free surfaces (both internal and external) of the vertebrate body. It can be composed of a single layer of cells or several cell layers.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Wall of blood capillaries", "Skin (Epidermis)", "Lining of nasal cavity"]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_epithelial_tissues'))
    def rule_features_of_epithelial_tissues(self):
        """Epithelial tissues possess specific characteristics regarding cell arrangement, basal attachment, and supply."""
        self.response = {
            'concept': 'Features of Epithelial tissues',
            'explanation': """Epithelial tissues possess specific characteristics regarding cell arrangement, basal attachment, and supply.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["The cells are placed on a basement membrane", "The cells are tightly packed", "A nerve supply is present within the tissue but there is no blood supply"]
        }
        self.halt()

    @Rule(Fact(query_topic='classification_of_epithelial_tissue'))
    def rule_classification_of_epithelial_tissue(self):
        """Epithelial tissue is categorized based on two primary morphological criteria: the shape of the cell and the number of cell layers."""
        self.response = {
            'concept': 'Classification of Epithelial tissue',
            'explanation': """Epithelial tissue is categorized based on two primary morphological criteria: the shape of the cell and the number of cell layers.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Classification according to the shape of the cell", "Classification according to the number of cell layers"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_epithelial_tissue'))
    def rule_functions_of_epithelial_tissue(self):
        """Epithelial tissue performs several vital roles in the body, including protection, absorption, and sensation."""
        self.response = {
            'concept': 'Functions of Epithelial tissue',
            'explanation': """Epithelial tissue performs several vital roles in the body, including protection, absorption, and sensation.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Lining up of free surfaces and protection (e.g., protecting internal organs from pressure, friction, and microbes)", "Absorptive function (e.g., in the digestive tract)", "Perception of stimuli (e.g., detecting taste and smell)"]
        }
        self.halt()

    @Rule(Fact(query_topic='secretory_function_of_epithelial_tissue'))
    def rule_secretory_function_of_epithelial_tissue(self):
        """Epithelial tissue, specifically the lining epithelium of the respiratory tract, performs a secretory function by producing and releasing mucous."""
        self.response = {
            'concept': 'Secretory function of Epithelial Tissue',
            'explanation': """Epithelial tissue, specifically the lining epithelium of the respiratory tract, performs a secretory function by producing and releasing mucous.""",
            'topic': 'Biology',
            'subtopic': 'Epithelial Tissue Functions',
            'examples': ["Secretion of mucous by the lining epithelium", "Role of epithelium in respiratory tract mucous production"]
        }
        self.halt()

    @Rule(Fact(query_topic='filtering_function_of_epithelial_tissue'))
    def rule_filtering_function_of_epithelial_tissue(self):
        """The epithelium within Bowman's capsule in nephrons demonstrates a filtering function by filtering blood."""
        self.response = {
            'concept': 'Filtering function of Epithelial Tissue',
            'explanation': """The epithelium within Bowman's capsule in nephrons demonstrates a filtering function by filtering blood.""",
            'topic': 'Biology',
            'subtopic': 'Epithelial Tissue Functions',
            'examples': ["Blood filtration by Bowman's capsule epithelium", "Epithelium's role in filtering within nephrons"]
        }
        self.halt()

    @Rule(Fact(query_topic='connective_tissue'))
    def rule_connective_tissue(self):
        """Connective tissue is composed of various cells and fibres embedded in a large matrix. Most types have nerve and blood supply. Its primary role is to connect tissues and organs and provide structural support."""
        self.response = {
            'concept': 'Connective Tissue',
            'explanation': """Connective tissue is composed of various cells and fibres embedded in a large matrix. Most types have nerve and blood supply. Its primary role is to connect tissues and organs and provide structural support.""",
            'topic': 'Biology',
            'subtopic': 'Tissues',
            'examples': ["Blood tissue", "Bone tissue", "Cartilage"]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_tissue__special_connective_tissue_'))
    def rule_blood_tissue__special_connective_tissue_(self):
        """Blood is a unique type of connective tissue. Its distinguishing feature is that its fluid matrix (plasma) is not secreted by the blood cells themselves. It plays a vital role in connecting various organs and tissues throughout the human body."""
        self.response = {
            'concept': 'Blood Tissue (Special Connective Tissue)',
            'explanation': """Blood is a unique type of connective tissue. Its distinguishing feature is that its fluid matrix (plasma) is not secreted by the blood cells themselves. It plays a vital role in connecting various organs and tissues throughout the human body.""",
            'topic': 'Biology',
            'subtopic': 'Connective Tissue Types',
            'examples': ["A special type of connective tissue", "Matrix (plasma) not secreted by blood cells", "Helps maintain proper connection between organs"]
        }
        self.halt()

    @Rule(Fact(query_topic='features_of_blood_tissue'))
    def rule_features_of_blood_tissue(self):
        """Blood tissue consists of a fluid matrix known as plasma. This matrix contains specialized cells such as red blood cells (erythrocytes) and white blood cells (leucocytes), along with cellular fragments called platelets. Fibres are typically absent but become visible during the process of blood clotting."""
        self.response = {
            'concept': 'Features of Blood Tissue',
            'explanation': """Blood tissue consists of a fluid matrix known as plasma. This matrix contains specialized cells such as red blood cells (erythrocytes) and white blood cells (leucocytes), along with cellular fragments called platelets. Fibres are typically absent but become visible during the process of blood clotting.""",
            'topic': 'Biology',
            'subtopic': 'Blood Tissue Composition',
            'examples': ["Plasma (fluid matrix)", "Red blood cells (erythrocytes)", "Platelets (cellular fragments)"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_blood_tissue'))
    def rule_functions_of_blood_tissue(self):
        """Blood tissue performs several critical functions including the transportation of essential materials like respiratory gases, nutrients, excretory substances, and hormones. It also offers protection against foreign bodies through white blood cells and plays a key role in maintaining homeostasis within the body."""
        self.response = {
            'concept': 'Functions of Blood Tissue',
            'explanation': """Blood tissue performs several critical functions including the transportation of essential materials like respiratory gases, nutrients, excretory substances, and hormones. It also offers protection against foreign bodies through white blood cells and plays a key role in maintaining homeostasis within the body.""",
            'topic': 'Biology',
            'subtopic': 'Blood Tissue Functions',
            'examples': ["Transportation of respiratory gases", "White blood cells destroying foreign bodies", "Maintenance of homeostasis"]
        }
        self.halt()

    @Rule(Fact(query_topic='muscle_tissue'))
    def rule_muscle_tissue(self):
        """Muscle tissue is a fundamental component of the human body, made up of muscle cells or fibres. These fibres are capable of contraction and relaxation. Unlike epithelial tissue, muscle tissue is well-supplied with blood, allowing for a high rate of oxygen and nutrient delivery. It functions as an effector in coordinated responses."""
        self.response = {
            'concept': 'Muscle Tissue',
            'explanation': """Muscle tissue is a fundamental component of the human body, made up of muscle cells or fibres. These fibres are capable of contraction and relaxation. Unlike epithelial tissue, muscle tissue is well-supplied with blood, allowing for a high rate of oxygen and nutrient delivery. It functions as an effector in coordinated responses.""",
            'topic': 'Biology',
            'subtopic': 'Tissues',
            'examples': ["Muscle cells (muscle fibres)", "Contraction ability", "Relaxation ability"]
        }
        self.halt()

    @Rule(Fact(query_topic='muscle_tissue_types'))
    def rule_muscle_tissue_types(self):
        """Muscle tissue is categorized into three primary types based on their structure, location, and control mechanisms. These types are Smooth muscle tissue, Skeletal muscle tissue, and Cardiac muscle tissue."""
        self.response = {
            'concept': 'Muscle Tissue Types',
            'explanation': """Muscle tissue is categorized into three primary types based on their structure, location, and control mechanisms. These types are Smooth muscle tissue, Skeletal muscle tissue, and Cardiac muscle tissue.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues - Muscle Tissue',
            'examples': ["Smooth muscle tissue", "Skeletal muscle tissue", "Cardiac muscle tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='smooth_muscle_tissue'))
    def rule_smooth_muscle_tissue(self):
        """Smooth muscle tissue is composed of smooth muscle cells and is typically found in the walls of organs that have cavities. Its cells are spindle-shaped, unbranched, and contain a single nucleus at the center. They lack striations, are resistant to fatigue, and are controlled involuntarily."""
        self.response = {
            'concept': 'Smooth Muscle Tissue',
            'explanation': """Smooth muscle tissue is composed of smooth muscle cells and is typically found in the walls of organs that have cavities. Its cells are spindle-shaped, unbranched, and contain a single nucleus at the center. They lack striations, are resistant to fatigue, and are controlled involuntarily.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues - Muscle Tissue',
            'examples': ["Walls of digestive tract", "Uterus", "Blood vessels", "Bladder"]
        }
        self.halt()

    @Rule(Fact(query_topic='skeletal_muscle_tissue'))
    def rule_skeletal_muscle_tissue(self):
        """Skeletal muscle tissue consists of skeletal muscle fibres that are largely associated with the skeletal system. These muscles are responsible for locomotion and various movements in chordates. The fibres are long, cylindrical, unbranched, multinucleate (with peripherally located nuclei), and possess striations. They are voluntarily controlled but fatigue easily."""
        self.response = {
            'concept': 'Skeletal Muscle Tissue',
            'explanation': """Skeletal muscle tissue consists of skeletal muscle fibres that are largely associated with the skeletal system. These muscles are responsible for locomotion and various movements in chordates. The fibres are long, cylindrical, unbranched, multinucleate (with peripherally located nuclei), and possess striations. They are voluntarily controlled but fatigue easily.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues - Muscle Tissue',
            'examples': ["Bicep muscle", "Tricep muscle", "Muscles in leg", "Facial muscles"]
        }
        self.halt()

    @Rule(Fact(query_topic='cardiac_muscle_tissue'))
    def rule_cardiac_muscle_tissue(self):
        """Cardiac muscle tissue is made up of cardiac muscle cells and is exclusively located in the vertebrate heart. These cells are uninucleate, striated, and short. A distinctive feature is the presence of intercalated discs between cells. Cardiac muscle tissue is involuntarily controlled, contracts rhythmically, and is highly resistant to fatigue."""
        self.response = {
            'concept': 'Cardiac Muscle Tissue',
            'explanation': """Cardiac muscle tissue is made up of cardiac muscle cells and is exclusively located in the vertebrate heart. These cells are uninucleate, striated, and short. A distinctive feature is the presence of intercalated discs between cells. Cardiac muscle tissue is involuntarily controlled, contracts rhythmically, and is highly resistant to fatigue.""",
            'topic': 'Biology',
            'subtopic': 'Living Tissues - Muscle Tissue',
            'examples': ["Vertebrate heart"]
        }
        self.halt()

    @Rule(Fact(query_topic='nervous_tissue'))
    def rule_nervous_tissue(self):
        """An important tissue found in chordate bodies, with the nerve cell or neuron serving as its structural unit."""
        self.response = {
            'concept': 'Nervous Tissue',
            'explanation': """An important tissue found in chordate bodies, with the nerve cell or neuron serving as its structural unit.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Found in chordates", "Structural unit is the neuron", "Transmits impulses"]
        }
        self.halt()

    @Rule(Fact(query_topic='neuron__nerve_cell_'))
    def rule_neuron__nerve_cell_(self):
        """The structural unit of nervous tissue, specialized to transmit impulses. It is composed of a cell body and nerve fibres."""
        self.response = {
            'concept': 'Neuron (Nerve Cell)',
            'explanation': """The structural unit of nervous tissue, specialized to transmit impulses. It is composed of a cell body and nerve fibres.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System Cells',
            'examples': ["Specialized to transmit impulses", "Composed of cell body and nerve fibres", "Structural unit of nervous tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='neuron_structure'))
    def rule_neuron_structure(self):
        """A neuron is composed of two main parts: the cell body and nerve fibres. The nerve fibres include the axon and dendrites."""
        self.response = {
            'concept': 'Neuron Structure',
            'explanation': """A neuron is composed of two main parts: the cell body and nerve fibres. The nerve fibres include the axon and dendrites.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Anatomy',
            'examples': ["Cell body", "Axon", "Dendrites"]
        }
        self.halt()

    @Rule(Fact(query_topic='cell_body__soma_'))
    def rule_cell_body__soma_(self):
        """One of the two main parts of a neuron, containing the nucleus, mitochondria, golgi body, and endoplasmic reticulum."""
        self.response = {
            'concept': 'Cell Body (Soma)',
            'explanation': """One of the two main parts of a neuron, containing the nucleus, mitochondria, golgi body, and endoplasmic reticulum.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Anatomy',
            'examples': ["Contains the nucleus", "Houses mitochondria", "Includes golgi body and endoplasmic reticulum"]
        }
        self.halt()

    @Rule(Fact(query_topic='axon'))
    def rule_axon(self):
        """A single process that arises from the cell body. Its function is to transmit impulses away from the cell body. Most axons in chordates are myelinated."""
        self.response = {
            'concept': 'Axon',
            'explanation': """A single process that arises from the cell body. Its function is to transmit impulses away from the cell body. Most axons in chordates are myelinated.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Anatomy',
            'examples': ["Transmits impulses away from cell body", "Arises as a single process", "Often myelinated in chordates"]
        }
        self.halt()

    @Rule(Fact(query_topic='dendrites'))
    def rule_dendrites(self):
        """Slender processes that receive stimuli and transmit impulses towards the cell body."""
        self.response = {
            'concept': 'Dendrites',
            'explanation': """Slender processes that receive stimuli and transmit impulses towards the cell body.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Anatomy',
            'examples': ["Receive stimuli", "Transmit impulses to the cell body", "Slender processes"]
        }
        self.halt()

    @Rule(Fact(query_topic='myelin_sheath_and_nodes_of_ranvier'))
    def rule_myelin_sheath_and_nodes_of_ranvier(self):
        """The myelin sheath covers most axons in chordates, but it is not continuous; the interrupted places are known as nodes of Ranvier. The myelin sheath increases the speed of impulse transmission."""
        self.response = {
            'concept': 'Myelin Sheath and Nodes of Ranvier',
            'explanation': """The myelin sheath covers most axons in chordates, but it is not continuous; the interrupted places are known as nodes of Ranvier. The myelin sheath increases the speed of impulse transmission.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Physiology',
            'examples': ["Increases speed of impulse transmission", "Not continuous along the axon", "Interrupted by nodes of Ranvier"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_neurons'))
    def rule_functions_of_neurons(self):
        """Neurons receive information from receptors (e.g., eye, ear) or other neurons and transmit these impulses to effectors (e.g., muscles) or to other neurons."""
        self.response = {
            'concept': 'Functions of Neurons',
            'explanation': """Neurons receive information from receptors (e.g., eye, ear) or other neurons and transmit these impulses to effectors (e.g., muscles) or to other neurons.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System Physiology',
            'examples': ["Receive information from the eye", "Transmit impulses to muscles", "Transmit impulses to another neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_neurons__functional_'))
    def rule_types_of_neurons__functional_(self):
        """Based on their function, neurons are divided into three types: Sensory neurons, Interneurons, and Motor neurons."""
        self.response = {
            'concept': 'Types of Neurons (Functional)',
            'explanation': """Based on their function, neurons are divided into three types: Sensory neurons, Interneurons, and Motor neurons.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Classification',
            'examples': ["Sensory neuron", "Interneuron", "Motor neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='sensory_neuron'))
    def rule_sensory_neuron(self):
        """A type of neuron whose cell body is typically in the middle of the nerve fibers, often inside a ganglion. Dendrites are at sensory organs, and the axon is in the central nervous system. They transmit impulses from sensory organs to the central nervous system."""
        self.response = {
            'concept': 'Sensory Neuron',
            'explanation': """A type of neuron whose cell body is typically in the middle of the nerve fibers, often inside a ganglion. Dendrites are at sensory organs, and the axon is in the central nervous system. They transmit impulses from sensory organs to the central nervous system.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Classification',
            'examples': ["Transmits impulses from eye to CNS", "Dendrites present at sensory organs", "Cell body found inside a ganglion"]
        }
        self.halt()

    @Rule(Fact(query_topic='motor_neuron'))
    def rule_motor_neuron(self):
        """A type of neuron that possesses a star-shaped cell body with many fibres, including a long axon (sometimes over 1m). Its function is to transmit impulses from the central nervous system to effectors (muscles)."""
        self.response = {
            'concept': 'Motor Neuron',
            'explanation': """A type of neuron that possesses a star-shaped cell body with many fibres, including a long axon (sometimes over 1m). Its function is to transmit impulses from the central nervous system to effectors (muscles).""",
            'topic': 'Biology',
            'subtopic': 'Neuron Classification',
            'examples': ["Transmits impulses from CNS to muscles", "Possesses a star-shaped cell body", "Can have axons greater than 1m in length"]
        }
        self.halt()

    @Rule(Fact(query_topic='interneuron'))
    def rule_interneuron(self):
        """One of the three types of neurons, classified according to function, serving as an intermediate neuron."""
        self.response = {
            'concept': 'Interneuron',
            'explanation': """One of the three types of neurons, classified according to function, serving as an intermediate neuron.""",
            'topic': 'Biology',
            'subtopic': 'Neuron Classification',
            'examples': ["A functional type of neuron", "Listed alongside sensory and motor neurons", "Shown in Figure 1.22"]
        }
        self.halt()

    @Rule(Fact(query_topic='ganglion'))
    def rule_ganglion(self):
        """A structure formed by the collection of cell bodies."""
        self.response = {
            'concept': 'Ganglion',
            'explanation': """A structure formed by the collection of cell bodies.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System Anatomy',
            'examples': ["A collection of cell bodies", "Where sensory neuron cell bodies are found"]
        }
        self.halt()

    @Rule(Fact(query_topic='interneuron'))
    def rule_interneuron(self):
        """A neuron present within the central nervous system, characterized by short axons and many dendrites, which connects sensory neurons with motor neurons."""
        self.response = {
            'concept': 'Interneuron',
            'explanation': """A neuron present within the central nervous system, characterized by short axons and many dendrites, which connects sensory neurons with motor neurons.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System / Neurons',
            'examples': ["Present within the central nervous system", "Axons are short", "Connects sensory neuron with motor neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='fibres'))
    def rule_fibres(self):
        """A type of tissue component, often found in plants, characterized by being composed of dead cells."""
        self.response = {
            'concept': 'Fibres',
            'explanation': """A type of tissue component, often found in plants, characterized by being composed of dead cells.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Cell Types',
            'examples': ["Composed of dead cells", "Identified as dead cells in plant tissue context"]
        }
        self.halt()

    @Rule(Fact(query_topic='xylem_tissue'))
    def rule_xylem_tissue(self):
        """A type of complex plant tissue."""
        self.response = {
            'concept': 'Xylem tissue',
            'explanation': """A type of complex plant tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Considered a complex tissue", "A type of plant tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='parenchyma_tissue'))
    def rule_parenchyma_tissue(self):
        """A plant tissue characterized by isodiametric cells, large vacuoles, and living cells."""
        self.response = {
            'concept': 'Parenchyma tissue',
            'explanation': """A plant tissue characterized by isodiametric cells, large vacuoles, and living cells.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Cells are isodiametric", "Contains large vacuoles", "Composed of living cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='skeletal_muscle_fibre'))
    def rule_skeletal_muscle_fibre(self):
        """A type of muscle fibre distinguished by the presence of cross striations."""
        self.response = {
            'concept': 'Skeletal muscle fibre',
            'explanation': """A type of muscle fibre distinguished by the presence of cross striations.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues / Muscle Tissue',
            'examples': ["Exhibits cross striations", "A characteristic feature of skeletal muscle"]
        }
        self.halt()

    @Rule(Fact(query_topic='epithelial_tissue'))
    def rule_epithelial_tissue(self):
        """An animal tissue where its cells are observed to be present on a basement membrane."""
        self.response = {
            'concept': 'Epithelial tissue',
            'explanation': """An animal tissue where its cells are observed to be present on a basement membrane.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues',
            'examples': ["Cells are present on a basement membrane", "An animal tissue type"]
        }
        self.halt()

    @Rule(Fact(query_topic='cardiac_muscle_fibres'))
    def rule_cardiac_muscle_fibres(self):
        """A type of muscle fibre that possesses intercalated discs."""
        self.response = {
            'concept': 'Cardiac muscle fibres',
            'explanation': """A type of muscle fibre that possesses intercalated discs.""",
            'topic': 'Biology',
            'subtopic': 'Animal Tissues / Muscle Tissue',
            'examples': ["Possesses intercalated discs", "A feature of cardiac muscle"]
        }
        self.halt()

    @Rule(Fact(query_topic='meristematic_tissues'))
    def rule_meristematic_tissues(self):
        """A category of plant tissues."""
        self.response = {
            'concept': 'Meristematic tissues',
            'explanation': """A category of plant tissues.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["Includes apical meristems", "Includes lateral meristems", "Includes intercalary meristems"]
        }
        self.halt()

    @Rule(Fact(query_topic='apical_meristems'))
    def rule_apical_meristems(self):
        """A type of meristematic tissue."""
        self.response = {
            'concept': 'Apical meristems',
            'explanation': """A type of meristematic tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Meristematic Tissues',
            'examples': ["A type of meristematic tissue", "Found in plants"]
        }
        self.halt()

    @Rule(Fact(query_topic='lateral_meristems'))
    def rule_lateral_meristems(self):
        """A type of meristematic tissue."""
        self.response = {
            'concept': 'Lateral meristems',
            'explanation': """A type of meristematic tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Meristematic Tissues',
            'examples': ["A type of meristematic tissue", "Found in plants"]
        }
        self.halt()

    @Rule(Fact(query_topic='intercalary_meristems'))
    def rule_intercalary_meristems(self):
        """A type of meristematic tissue."""
        self.response = {
            'concept': 'Intercalary meristems',
            'explanation': """A type of meristematic tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues / Meristematic Tissues',
            'examples': ["A type of meristematic tissue", "Found in plants"]
        }
        self.halt()

    @Rule(Fact(query_topic='collenchyma_tissue'))
    def rule_collenchyma_tissue(self):
        """A type of plant tissue."""
        self.response = {
            'concept': 'Collenchyma tissue',
            'explanation': """A type of plant tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["A type of plant tissue", "Mentioned in the context of plant cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='sclerenchyma_tissue'))
    def rule_sclerenchyma_tissue(self):
        """A type of plant tissue."""
        self.response = {
            'concept': 'Sclerenchyma tissue',
            'explanation': """A type of plant tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["A type of plant tissue", "Mentioned in the context of plant cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='phloem_tissue'))
    def rule_phloem_tissue(self):
        """A type of plant tissue."""
        self.response = {
            'concept': 'Phloem tissue',
            'explanation': """A type of plant tissue.""",
            'topic': 'Biology',
            'subtopic': 'Plant Tissues',
            'examples': ["A type of plant tissue", "Mentioned alongside xylem tissue"]
        }
        self.halt()

    @Rule(Fact(query_topic='heterotrophic_mode_of_nutrition'))
    def rule_heterotrophic_mode_of_nutrition(self):
        """A mode of nutrition where organisms depend on other organisms to obtain their food."""
        self.response = {
            'concept': 'Heterotrophic mode of nutrition',
            'explanation': """A mode of nutrition where organisms depend on other organisms to obtain their food.""",
            'topic': 'Biology',
            'subtopic': 'Nutrition',
            'examples': ["Cow obtaining food from grass", "Stork obtaining food from other organisms"]
        }
        self.halt()

    @Rule(Fact(query_topic='autotrophic_mode_of_nutrition'))
    def rule_autotrophic_mode_of_nutrition(self):
        """A mode of nutrition where organisms produce their own food within themselves."""
        self.response = {
            'concept': 'Autotrophic mode of nutrition',
            'explanation': """A mode of nutrition where organisms produce their own food within themselves.""",
            'topic': 'Biology',
            'subtopic': 'Nutrition',
            'examples': ["Green plants synthesizing their own food"]
        }
        self.halt()

    @Rule(Fact(query_topic='photosynthesis'))
    def rule_photosynthesis(self):
        """The process by which cells containing chlorophyll in green plants synthesize food (glucose) using light energy, carbondioxide, and water as raw materials."""
        self.response = {
            'concept': 'Photosynthesis',
            'explanation': """The process by which cells containing chlorophyll in green plants synthesize food (glucose) using light energy, carbondioxide, and water as raw materials.""",
            'topic': 'Biology',
            'subtopic': 'Plant Biology',
            'examples': ["Green plants producing food", "Synthesis of glucose from CO2 and H2O", "Utilizing light energy by chlorophyll-containing cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_necessary_for_photosynthesis'))
    def rule_factors_necessary_for_photosynthesis(self):
        """The essential components and conditions required for the process of photosynthesis, including light energy, chlorophyll, carbondioxide (CO2), and water (H2O)."""
        self.response = {
            'concept': 'Factors Necessary for Photosynthesis',
            'explanation': """The essential components and conditions required for the process of photosynthesis, including light energy, chlorophyll, carbondioxide (CO2), and water (H2O).""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis',
            'examples': ["Light energy", "CO2 absorbed by stomata", "H2O absorbed by root hairs"]
        }
        self.halt()

    @Rule(Fact(query_topic='water_absorption_and_transport_in_terrestrial_plants__for_photosynthesis_'))
    def rule_water_absorption_and_transport_in_terrestrial_plants__for_photosynthesis_(self):
        """Terrestrial plants absorb water from the soil through root hairs via osmosis. This water travels into root xylem through the cortex and endodermis, then transports to mesophyll cells of leaves via stem xylem and veins."""
        self.response = {
            'concept': 'Water Absorption and Transport in Terrestrial Plants (for Photosynthesis)',
            'explanation': """Terrestrial plants absorb water from the soil through root hairs via osmosis. This water travels into root xylem through the cortex and endodermis, then transports to mesophyll cells of leaves via stem xylem and veins.""",
            'topic': 'Biology',
            'subtopic': 'Plant Physiology',
            'examples': ["Water absorption by root hairs via osmosis", "Water traveling into root xylem through cortex and endodermis", "Water transported to mesophyll cells via xylem of stem and veins"]
        }
        self.halt()

    @Rule(Fact(query_topic='water_distribution_in_leaves'))
    def rule_water_distribution_in_leaves(self):
        """The network of veins within leaves is responsible for efficiently distributing water throughout the entire leaf structure to support metabolic processes like photosynthesis."""
        self.response = {
            'concept': 'Water Distribution in Leaves',
            'explanation': """The network of veins within leaves is responsible for efficiently distributing water throughout the entire leaf structure to support metabolic processes like photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Leaf Structure',
            'examples': ["Veins transport water from the stem to all leaf cells.", "A dense network of veins ensures widespread water distribution."]
        }
        self.halt()

    @Rule(Fact(query_topic='carbon_dioxide_uptake_for_photosynthesis'))
    def rule_carbon_dioxide_uptake_for_photosynthesis(self):
        """Carbon dioxide (CO2), essential for photosynthesis, is obtained from the atmosphere. It diffuses into the leaf through small pores called stomata and then travels through intercellular spaces to reach the mesophyll cells where photosynthesis occurs."""
        self.response = {
            'concept': 'Carbon Dioxide Uptake for Photosynthesis',
            'explanation': """Carbon dioxide (CO2), essential for photosynthesis, is obtained from the atmosphere. It diffuses into the leaf through small pores called stomata and then travels through intercellular spaces to reach the mesophyll cells where photosynthesis occurs.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Gas Exchange',
            'examples': ["CO2 enters the leaf through stomata.", "Intercellular spaces facilitate CO2 movement to mesophyll cells.", "Atmospheric CO2 is the source for carbon fixation."]
        }
        self.halt()

    @Rule(Fact(query_topic='role_of_chlorophyll_in_photosynthesis'))
    def rule_role_of_chlorophyll_in_photosynthesis(self):
        """Chlorophyll is a special green pigment located in the chloroplasts within plant cells. Its primary function is to absorb energy from sunlight, which is the initial step in converting light energy into chemical energy during photosynthesis."""
        self.response = {
            'concept': 'Role of Chlorophyll in Photosynthesis',
            'explanation': """Chlorophyll is a special green pigment located in the chloroplasts within plant cells. Its primary function is to absorb energy from sunlight, which is the initial step in converting light energy into chemical energy during photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Pigments',
            'examples': ["Chlorophyll captures light energy.", "The green color of leaves is due to chlorophyll.", "Chlorophyll is found inside chloroplasts."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_photosynthesis'))
    def rule_factors_affecting_photosynthesis(self):
        """The process of photosynthesis is influenced by several critical factors, including the presence of chlorophyll, the availability of water, the intensity and presence of light energy, and the concentration of carbon dioxide."""
        self.response = {
            'concept': 'Factors Affecting Photosynthesis',
            'explanation': """The process of photosynthesis is influenced by several critical factors, including the presence of chlorophyll, the availability of water, the intensity and presence of light energy, and the concentration of carbon dioxide.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Conditions',
            'examples': ["Adequate water is necessary for photosynthesis.", "Photosynthesis requires sufficient light energy.", "The absence of chlorophyll prevents photosynthesis."]
        }
        self.halt()

    @Rule(Fact(query_topic='glucose_storage_and_transport_in_plants'))
    def rule_glucose_storage_and_transport_in_plants(self):
        """Glucose (C6H12O6) produced during photosynthesis is temporarily stored in leaves as starch. This starch is then converted into sucrose (C12H22O11) for transport to other plant tissues via the phloem. Upon reaching storage organs, sucrose is reconverted and stored as starch."""
        self.response = {
            'concept': 'Glucose Storage and Transport in Plants',
            'explanation': """Glucose (C6H12O6) produced during photosynthesis is temporarily stored in leaves as starch. This starch is then converted into sucrose (C12H22O11) for transport to other plant tissues via the phloem. Upon reaching storage organs, sucrose is reconverted and stored as starch.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Products',
            'examples': ["Glucose is stored as starch in leaves.", "Sucrose is transported to storing organs.", "Fruits, vegetables, and yams store energy as starch."]
        }
        self.halt()

    @Rule(Fact(query_topic='oxygen_release_as_a_byproduct_of_photosynthesis'))
    def rule_oxygen_release_as_a_byproduct_of_photosynthesis(self):
        """Oxygen (O2) is a byproduct generated during photosynthesis. This oxygen is released and diffused into the atmosphere primarily through the stomata, the same pores used for carbon dioxide intake."""
        self.response = {
            'concept': 'Oxygen Release as a Byproduct of Photosynthesis',
            'explanation': """Oxygen (O2) is a byproduct generated during photosynthesis. This oxygen is released and diffused into the atmosphere primarily through the stomata, the same pores used for carbon dioxide intake.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Byproducts',
            'examples': ["Plants release oxygen into the atmosphere.", "O2 exits the leaf through stomata.", "Oxygen is a 'waste' product for the plant but vital for animals."]
        }
        self.halt()

    @Rule(Fact(query_topic='word_equation_of_photosynthesis'))
    def rule_word_equation_of_photosynthesis(self):
        """The process of photosynthesis can be summarized by a word equation: Carbon dioxide and Water react, in the presence of Light energy and Chlorophyll, to produce Glucose and Oxygen."""
        self.response = {
            'concept': 'Word Equation of Photosynthesis',
            'explanation': """The process of photosynthesis can be summarized by a word equation: Carbon dioxide and Water react, in the presence of Light energy and Chlorophyll, to produce Glucose and Oxygen.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Equations',
            'examples': ["Carbon dioxide + Water → Glucose + Oxygen", "Light energy and Chlorophyll are conditions for the reaction."]
        }
        self.halt()

    @Rule(Fact(query_topic='balanced_chemical_equation_for_photosynthesis'))
    def rule_balanced_chemical_equation_for_photosynthesis(self):
        """The balanced chemical equation for photosynthesis is 6CO2(g) + 6H2O(l) → C6H12O6(s) + 6O2(g), indicating that six molecules of carbon dioxide and six molecules of water react under light energy and chlorophyll to yield one molecule of glucose and six molecules of oxygen."""
        self.response = {
            'concept': 'Balanced Chemical Equation for Photosynthesis',
            'explanation': """The balanced chemical equation for photosynthesis is 6CO2(g) + 6H2O(l) → C6H12O6(s) + 6O2(g), indicating that six molecules of carbon dioxide and six molecules of water react under light energy and chlorophyll to yield one molecule of glucose and six molecules of oxygen.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Equations',
            'examples': ["6CO2 + 6H2O → C6H12O6 + 6O2", "Light energy and chlorophyll are written above and below the arrow.", "Glucose is produced as a solid, oxygen as a gas."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_absorption_spectrum_for_photosynthesis'))
    def rule_light_absorption_spectrum_for_photosynthesis(self):
        """During photosynthesis, plants primarily absorb red and blue wavelengths of sunlight. These specific parts of the light spectrum are most effective in driving the photosynthetic process."""
        self.response = {
            'concept': 'Light Absorption Spectrum for Photosynthesis',
            'explanation': """During photosynthesis, plants primarily absorb red and blue wavelengths of sunlight. These specific parts of the light spectrum are most effective in driving the photosynthetic process.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis - Light Spectrum',
            'examples': ["Red light is absorbed by chlorophyll.", "Blue light is utilized in photosynthesis.", "Green light is mostly reflected, making plants appear green."]
        }
        self.halt()

    @Rule(Fact(query_topic='starch_test_to_confirm_photosynthesis'))
    def rule_starch_test_to_confirm_photosynthesis(self):
        """To determine if photosynthesis has taken place, a starch test can be performed on a plant leaf. The process involves boiling the leaf in water, then in alcohol (using a water bath for safety) to remove chlorophyll, followed by washing and adding iodine solution. A colour change to blue or dark purple indicates the presence of starch, signifying photosynthesis."""
        self.response = {
            'concept': 'Starch Test to Confirm Photosynthesis',
            'explanation': """To determine if photosynthesis has taken place, a starch test can be performed on a plant leaf. The process involves boiling the leaf in water, then in alcohol (using a water bath for safety) to remove chlorophyll, followed by washing and adding iodine solution. A colour change to blue or dark purple indicates the presence of starch, signifying photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Experiments',
            'examples': ["Boiling a leaf from a plant in sunlight for a starch test.", "Observing a pale leaf after boiling in alcohol.", "Adding iodine solution to a destarched leaf to check for blue/dark purple colour."]
        }
        self.halt()

    @Rule(Fact(query_topic='role_of_alcohol_in_starch_test'))
    def rule_role_of_alcohol_in_starch_test(self):
        """During the starch test, a plant leaf is boiled in alcohol to dissolve and remove chlorophyll. This causes the leaf to turn pale and the alcohol solution to become green. Removing chlorophyll is essential because it would otherwise mask the colour change produced by iodine reacting with starch, making the test results clearer. Alcohol is highly flammable, so it must be boiled in a water bath for safety."""
        self.response = {
            'concept': 'Role of Alcohol in Starch Test',
            'explanation': """During the starch test, a plant leaf is boiled in alcohol to dissolve and remove chlorophyll. This causes the leaf to turn pale and the alcohol solution to become green. Removing chlorophyll is essential because it would otherwise mask the colour change produced by iodine reacting with starch, making the test results clearer. Alcohol is highly flammable, so it must be boiled in a water bath for safety.""",
            'topic': 'Biology',
            'subtopic': 'Experimental Techniques',
            'examples': ["Boiling a leaf in alcohol until the alcohol turns green.", "Placing a test tube with a leaf and alcohol into a beaker of boiling water.", "Using a water bath to safely heat alcohol during chlorophyll extraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='interpreting_starch_test_results'))
    def rule_interpreting_starch_test_results(self):
        """After performing the starch test on a leaf, the final observation of colour change when iodine solution is added allows for a conclusion regarding starch presence. If the leaf turns blue or dark purple, it confirms that starch is present in that part of the leaf. If there is no such colour change, it indicates the absence of starch."""
        self.response = {
            'concept': 'Interpreting Starch Test Results',
            'explanation': """After performing the starch test on a leaf, the final observation of colour change when iodine solution is added allows for a conclusion regarding starch presence. If the leaf turns blue or dark purple, it confirms that starch is present in that part of the leaf. If there is no such colour change, it indicates the absence of starch.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Experiments',
            'examples': ["A leaf turning blue after adding iodine indicates starch is present.", "A part of a leaf remaining pale yellow/brown after iodine addition indicates no starch.", "Concluding that photosynthesis occurred if the leaf shows a dark purple colour with iodine."]
        }
        self.halt()

    @Rule(Fact(query_topic='destarching_a_plant_for_photosynthesis_experiments'))
    def rule_destarching_a_plant_for_photosynthesis_experiments(self):
        """Before conducting experiments to determine factors required for photosynthesis (e.g., light energy, carbon dioxide), plants must be kept in the dark for approximately 48 hours. This process, known as destarching, ensures that any pre-existing stored starch in the leaves is completely utilized or removed, so that any starch detected after the experiment can be attributed solely to the conditions of the experiment."""
        self.response = {
            'concept': 'Destarching a Plant for Photosynthesis Experiments',
            'explanation': """Before conducting experiments to determine factors required for photosynthesis (e.g., light energy, carbon dioxide), plants must be kept in the dark for approximately 48 hours. This process, known as destarching, ensures that any pre-existing stored starch in the leaves is completely utilized or removed, so that any starch detected after the experiment can be attributed solely to the conditions of the experiment.""",
            'topic': 'Biology',
            'subtopic': 'Experimental Design',
            'examples': ["Placing a potted plant in a dark room for two days before an experiment.", "Ensuring that the leaves are completely starch-free before starting an investigation on light.", "Preparing a plant by keeping it in the dark to show that light energy is needed for starch production."]
        }
        self.halt()

    @Rule(Fact(query_topic='experiment_to_show_light_energy_is_required_for_photosynthesis'))
    def rule_experiment_to_show_light_energy_is_required_for_photosynthesis(self):
        """This experiment demonstrates that light energy is crucial for photosynthesis. A destarched plant is used, where parts of two similar leaves are covered with black (no light) and colourless (light) polythene strips, respectively. After exposure to sunlight for several hours, both leaves are subjected to a starch test. The expected result is starch presence only in the areas exposed to light."""
        self.response = {
            'concept': 'Experiment to Show Light Energy is Required for Photosynthesis',
            'explanation': """This experiment demonstrates that light energy is crucial for photosynthesis. A destarched plant is used, where parts of two similar leaves are covered with black (no light) and colourless (light) polythene strips, respectively. After exposure to sunlight for several hours, both leaves are subjected to a starch test. The expected result is starch presence only in the areas exposed to light.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Experiments',
            'examples': ["Covering a part of a destarched leaf with a black polythene strip.", "Covering another part of the leaf with a colourless polythene strip.", "Keeping the treated leaves under sunlight for 3-5 hours before testing for starch."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_energy_is_necessary_for_photosynthesis'))
    def rule_light_energy_is_necessary_for_photosynthesis(self):
        """An experiment comparing two covered areas of leaves, A and B, demonstrates this. Leaf A, completely deprived of light, showed no color change with iodine solution, indicating no starch production and thus no photosynthesis. Leaf B, covered with colorless polythene but receiving light energy, showed a dark purple or blue color with iodine solution, indicating starch production and successful photosynthesis. Therefore, light energy is essential for the process."""
        self.response = {
            'concept': 'Light energy is necessary for photosynthesis',
            'explanation': """An experiment comparing two covered areas of leaves, A and B, demonstrates this. Leaf A, completely deprived of light, showed no color change with iodine solution, indicating no starch production and thus no photosynthesis. Leaf B, covered with colorless polythene but receiving light energy, showed a dark purple or blue color with iodine solution, indicating starch production and successful photosynthesis. Therefore, light energy is essential for the process.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis requirements',
            'examples': ["Leaf A (no light) shows no color change with iodine solution.", "Leaf B (with light) shows a dark purple or blue color with iodine solution.", "Absence of light prevents photosynthesis and starch production."]
        }
        self.halt()

    @Rule(Fact(query_topic='carbon_dioxide__co2__is_required_for_photosynthesis'))
    def rule_carbon_dioxide__co2__is_required_for_photosynthesis(self):
        """Activity 2.4 illustrates this using two similar leaves, C and D. Leaf D was sealed in a polythene bag with KOH solution (which absorbs CO2), while leaf C was sealed in a bag with water (allowing CO2 access). After placing the plant in sunlight and performing a starch test, leaf D showed no color change, signifying no photosynthesis due to lack of CO2. Leaf C, with available CO2, showed a dark purple or blue color, indicating photosynthesis and starch production. This concludes that CO2 is necessary for photosynthesis."""
        self.response = {
            'concept': 'Carbon dioxide (CO2) is required for photosynthesis',
            'explanation': """Activity 2.4 illustrates this using two similar leaves, C and D. Leaf D was sealed in a polythene bag with KOH solution (which absorbs CO2), while leaf C was sealed in a bag with water (allowing CO2 access). After placing the plant in sunlight and performing a starch test, leaf D showed no color change, signifying no photosynthesis due to lack of CO2. Leaf C, with available CO2, showed a dark purple or blue color, indicating photosynthesis and starch production. This concludes that CO2 is necessary for photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis requirements',
            'examples': ["Leaf D (in a bag with KOH, thus no CO2) shows no color change after starch test.", "Leaf C (in a bag with water, thus CO2 available) shows a dark purple or blue color after starch test.", "KOH solution absorbs CO2, preventing photosynthesis in the experimental setup."]
        }
        self.halt()

    @Rule(Fact(query_topic='chlorophyll_is_essential_for_photosynthesis'))
    def rule_chlorophyll_is_essential_for_photosynthesis(self):
        """An experiment using a mosaic plant leaf demonstrates that only the green-colored regions, which contain chlorophyll, undergo photosynthesis and produce starch (indicated by a color change with the starch test). The white-colored regions, lacking chlorophyll, do not produce starch, thus confirming chlorophyll's necessity for photosynthesis."""
        self.response = {
            'concept': 'Chlorophyll is essential for photosynthesis',
            'explanation': """An experiment using a mosaic plant leaf demonstrates that only the green-colored regions, which contain chlorophyll, undergo photosynthesis and produce starch (indicated by a color change with the starch test). The white-colored regions, lacking chlorophyll, do not produce starch, thus confirming chlorophyll's necessity for photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis requirements',
            'examples': ["Mosaic plant leaves like Hibiscus or Croton are used for this experiment.", "Green colored areas show a dark purple or blue color after the starch test.", "White colored areas show no color change after the starch test."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_challenges_in_testing_water_s_need_for_photosynthesis'))
    def rule_experimental_challenges_in_testing_water_s_need_for_photosynthesis(self):
        """Designing a direct laboratory experiment to test the need for water in photosynthesis is difficult because withholding water from a control plant would cause it to die, invalidating the experiment's results. Scientists have overcome this by using isotopic tracing."""
        self.response = {
            'concept': "Experimental challenges in testing water's need for photosynthesis",
            'explanation': """Designing a direct laboratory experiment to test the need for water in photosynthesis is difficult because withholding water from a control plant would cause it to die, invalidating the experiment's results. Scientists have overcome this by using isotopic tracing.""",
            'topic': 'Biology',
            'subtopic': 'Experimental design in photosynthesis',
            'examples': ["A plant in a control experiment without water would die.", "Scientists used water with O-18 isotope to confirm its need.", "The oxygen end product contains the O-18 isotope when water with O-18 is supplied."]
        }
        self.halt()

    @Rule(Fact(query_topic='oxygen_is_produced_during_photosynthesis'))
    def rule_oxygen_is_produced_during_photosynthesis(self):
        """An experiment with an aquatic plant (like Hydrilla or Vallisneria) placed in water and exposed to sunlight demonstrates that gas bubbles are released. This gas collects in an inverted boiling tube and can be tested with a glowing splinter, confirming it is oxygen, a product of photosynthesis."""
        self.response = {
            'concept': 'Oxygen is produced during photosynthesis',
            'explanation': """An experiment with an aquatic plant (like Hydrilla or Vallisneria) placed in water and exposed to sunlight demonstrates that gas bubbles are released. This gas collects in an inverted boiling tube and can be tested with a glowing splinter, confirming it is oxygen, a product of photosynthesis.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis products',
            'examples': ["Aquatic plants such as Hydrilla or Vallisneria are suitable for this experiment.", "Gas bubbles collect at the top of an inverted boiling tube.", "A glowing splinter is used to test the accumulated gas."]
        }
        self.halt()

    @Rule(Fact(query_topic='oxygen_as_a_product_of_photosynthesis'))
    def rule_oxygen_as_a_product_of_photosynthesis(self):
        """The gas released as a product of photosynthesis is oxygen. This can be experimentally verified because oxygen causes a glowing splinter to burn with a bright flame."""
        self.response = {
            'concept': 'Oxygen as a Product of Photosynthesis',
            'explanation': """The gas released as a product of photosynthesis is oxygen. This can be experimentally verified because oxygen causes a glowing splinter to burn with a bright flame.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Products',
            'examples': ["A glowing splinter test confirms the presence of oxygen.", "Plants release oxygen into the atmosphere.", "The gas supporting combustion is oxygen."]
        }
        self.halt()

    @Rule(Fact(query_topic='lavoisier_s_discovery_of_oxygen_from_plants'))
    def rule_lavoisier_s_discovery_of_oxygen_from_plants(self):
        """Antoine Lavoisier was the first scientist credited with demonstrating that green plants release oxygen gas into the environment, specifically when exposed to sunlight."""
        self.response = {
            'concept': "Lavoisier's Discovery of Oxygen from Plants",
            'explanation': """Antoine Lavoisier was the first scientist credited with demonstrating that green plants release oxygen gas into the environment, specifically when exposed to sunlight.""",
            'topic': 'Biology',
            'subtopic': 'History of Photosynthesis',
            'examples': ["Lavoisier linked plant activity to oxygen production.", "An early insight into the role of plants in air quality.", "His work established oxygen diffusion from green plants."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_conversion_in_photosynthesis'))
    def rule_energy_conversion_in_photosynthesis(self):
        """During photosynthesis, light energy from the sun is converted into chemical energy, which is then stored in the food (organic compounds) produced by plants. This process is essential for life on Earth and cannot be artificially replicated."""
        self.response = {
            'concept': 'Energy Conversion in Photosynthesis',
            'explanation': """During photosynthesis, light energy from the sun is converted into chemical energy, which is then stored in the food (organic compounds) produced by plants. This process is essential for life on Earth and cannot be artificially replicated.""",
            'topic': 'Biology',
            'subtopic': 'Importance of Photosynthesis',
            'examples': ["Plants transform solar energy into stored food energy.", "All organisms depend on this energy conversion for food.", "Photosynthesis is a natural, irreplaceable process for energy capture."]
        }
        self.halt()

    @Rule(Fact(query_topic='oxygen_provision_by_photosynthesis'))
    def rule_oxygen_provision_by_photosynthesis(self):
        """Photosynthesis is the primary source of oxygen gas required for the survival of aerobic organisms (those that use oxygen for respiration) and for the combustion of various materials."""
        self.response = {
            'concept': 'Oxygen Provision by Photosynthesis',
            'explanation': """Photosynthesis is the primary source of oxygen gas required for the survival of aerobic organisms (those that use oxygen for respiration) and for the combustion of various materials.""",
            'topic': 'Biology',
            'subtopic': 'Importance of Photosynthesis',
            'examples': ["Animals breathe oxygen produced by plants.", "Oxygen for burning wood originates from photosynthesis.", "Aerobic life forms rely on photosynthetic oxygen."]
        }
        self.halt()

    @Rule(Fact(query_topic='carbon_dioxide_removal_and_atmospheric_balance_by_photosynthesis'))
    def rule_carbon_dioxide_removal_and_atmospheric_balance_by_photosynthesis(self):
        """Photosynthesis removes carbon dioxide that accumulates in the environment due to respiration and combustion. By consuming CO2 and releasing O2, it helps maintain the vital balance of oxygen and carbon dioxide in the atmosphere."""
        self.response = {
            'concept': 'Carbon Dioxide Removal and Atmospheric Balance by Photosynthesis',
            'explanation': """Photosynthesis removes carbon dioxide that accumulates in the environment due to respiration and combustion. By consuming CO2 and releasing O2, it helps maintain the vital balance of oxygen and carbon dioxide in the atmosphere.""",
            'topic': 'Biology',
            'subtopic': 'Importance of Photosynthesis',
            'examples': ["Plants absorb CO2, reducing its atmospheric concentration.", "Helps regulate Earth's climate by managing CO2 levels.", "Maintains the O2:CO2 ratio for stable atmospheric conditions."]
        }
        self.halt()

    @Rule(Fact(query_topic='photosynthesis__role_in_the_carbon_cycle'))
    def rule_photosynthesis__role_in_the_carbon_cycle(self):
        """Photosynthesis is a fundamental process that helps to maintain and drive the global carbon cycle by fixing atmospheric carbon dioxide into organic molecules within living organisms."""
        self.response = {
            'concept': "Photosynthesis' Role in the Carbon Cycle",
            'explanation': """Photosynthesis is a fundamental process that helps to maintain and drive the global carbon cycle by fixing atmospheric carbon dioxide into organic molecules within living organisms.""",
            'topic': 'Biology',
            'subtopic': 'Importance of Photosynthesis',
            'examples': ["Carbon moves from the atmosphere to plants through photosynthesis.", "It is a key component of the global carbon flow.", "Contributes to the continuous recycling of carbon on Earth."]
        }
        self.halt()

    @Rule(Fact(query_topic='requirements_for_photosynthesis'))
    def rule_requirements_for_photosynthesis(self):
        """For photosynthesis to occur, green plants require several essential components: light energy (usually from the sun), water (H2O), carbon dioxide (CO2), and the pigment chlorophyll."""
        self.response = {
            'concept': 'Requirements for Photosynthesis',
            'explanation': """For photosynthesis to occur, green plants require several essential components: light energy (usually from the sun), water (H2O), carbon dioxide (CO2), and the pigment chlorophyll.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Process',
            'examples': ["Sunlight is the energy source for photosynthesis.", "Plants absorb water through their roots.", "Chlorophyll captures light energy in plant cells."]
        }
        self.halt()

    @Rule(Fact(query_topic='products_of_photosynthesis'))
    def rule_products_of_photosynthesis(self):
        """The main product synthesized during photosynthesis is glucose (a sugar), which serves as food for the plant. Oxygen gas is produced as a byproduct and is released into the environment."""
        self.response = {
            'concept': 'Products of Photosynthesis',
            'explanation': """The main product synthesized during photosynthesis is glucose (a sugar), which serves as food for the plant. Oxygen gas is produced as a byproduct and is released into the environment.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Products',
            'examples': ["Glucose provides energy for plant growth.", "Oxygen is a gaseous release from the process.", "Plants make sugar and expel breathable air."]
        }
        self.halt()

    @Rule(Fact(query_topic='photosynthesis_balanced_chemical_equation'))
    def rule_photosynthesis_balanced_chemical_equation(self):
        """The overall process of photosynthesis can be represented by the balanced chemical equation: 6CO2(g) + 6H2O(l) → C6H12O6(s) + 6O2(g). This reaction requires light energy and chlorophyll to proceed."""
        self.response = {
            'concept': 'Photosynthesis Balanced Chemical Equation',
            'explanation': """The overall process of photosynthesis can be represented by the balanced chemical equation: 6CO2(g) + 6H2O(l) → C6H12O6(s) + 6O2(g). This reaction requires light energy and chlorophyll to proceed.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Process',
            'examples': ["Carbon dioxide and water are the reactants.", "Glucose and oxygen are the products.", "Chlorophyll and light energy are necessary conditions."]
        }
        self.halt()

    @Rule(Fact(query_topic='global_importance_of_photosynthesis__summary_'))
    def rule_global_importance_of_photosynthesis__summary_(self):
        """The global significance of photosynthesis lies in its roles in providing food for all organisms directly or indirectly, maintaining the crucial oxygen and carbon dioxide balance in the atmosphere, and sustaining the Earth's carbon cycle."""
        self.response = {
            'concept': 'Global Importance of Photosynthesis (Summary)',
            'explanation': """The global significance of photosynthesis lies in its roles in providing food for all organisms directly or indirectly, maintaining the crucial oxygen and carbon dioxide balance in the atmosphere, and sustaining the Earth's carbon cycle.""",
            'topic': 'Biology',
            'subtopic': 'Global Significance of Photosynthesis',
            'examples': ["Photosynthesis underpins all food webs.", "It stabilizes atmospheric gas composition.", "Crucial for the Earth's life support systems."]
        }
        self.halt()

    @Rule(Fact(query_topic='identification_of_main_product_of_photosynthesis'))
    def rule_identification_of_main_product_of_photosynthesis(self):
        """When asked to identify the main product of photosynthesis, glucose is the correct answer. It is the primary carbohydrate produced and utilized by plants."""
        self.response = {
            'concept': 'Identification of Main Product of Photosynthesis',
            'explanation': """When asked to identify the main product of photosynthesis, glucose is the correct answer. It is the primary carbohydrate produced and utilized by plants.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Products',
            'examples': ["Glucose is the direct output of sugar synthesis.", "It is not starch or sucrose initially.", "The plant's energy storage molecule is glucose."]
        }
        self.halt()

    @Rule(Fact(query_topic='phloem_s_role_in_transporting_photosynthesis_products'))
    def rule_phloem_s_role_in_transporting_photosynthesis_products(self):
        """Phloem is the specialized plant tissue responsible for transporting the products of photosynthesis (sugars like glucose, often converted to sucrose) from the leaves, where they are produced, to other parts of the plant, including storage organs."""
        self.response = {
            'concept': "Phloem's Role in Transporting Photosynthesis Products",
            'explanation': """Phloem is the specialized plant tissue responsible for transporting the products of photosynthesis (sugars like glucose, often converted to sucrose) from the leaves, where they are produced, to other parts of the plant, including storage organs.""",
            'topic': 'Biology',
            'subtopic': 'Plant Anatomy and Transport',
            'examples': ["Phloem moves sugars from leaves to roots.", "It is the plant's 'food pipeline'.", "Translocation of food occurs via phloem."]
        }
        self.halt()

    @Rule(Fact(query_topic='gas_emitted_during_photosynthesis'))
    def rule_gas_emitted_during_photosynthesis(self):
        """Photosynthesis is a process by which green plants convert light energy into chemical energy, and during this process, a specific gas is released into the atmosphere as a byproduct."""
        self.response = {
            'concept': 'Gas Emitted During Photosynthesis',
            'explanation': """Photosynthesis is a process by which green plants convert light energy into chemical energy, and during this process, a specific gas is released into the atmosphere as a byproduct.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis',
            'examples': ["Oxygen is the gas emitted during photosynthesis.", "Plants release oxygen when performing photosynthesis."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_conversion_in_photosynthesis'))
    def rule_energy_conversion_in_photosynthesis(self):
        """During photosynthesis, plants transform solar energy (light energy) from the sun into a different form of energy, which is stored within chemical bonds of organic molecules."""
        self.response = {
            'concept': 'Energy Conversion in Photosynthesis',
            'explanation': """During photosynthesis, plants transform solar energy (light energy) from the sun into a different form of energy, which is stored within chemical bonds of organic molecules.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis, Energy Transformations',
            'examples': ["Solar energy is converted to chemical energy during photosynthesis.", "The light energy absorbed by chlorophyll is stored as chemical energy in sugars."]
        }
        self.halt()

    @Rule(Fact(query_topic='starch_test_and_light_requirement'))
    def rule_starch_test_and_light_requirement(self):
        """For a leaf to produce starch, it requires light. A leaf kept in darkness for an extended period (e.g., 48 hours) will deplete its starch reserves and will therefore not show a positive colour change with the starch test, indicating the absence of starch."""
        self.response = {
            'concept': 'Starch Test and Light Requirement',
            'explanation': """For a leaf to produce starch, it requires light. A leaf kept in darkness for an extended period (e.g., 48 hours) will deplete its starch reserves and will therefore not show a positive colour change with the starch test, indicating the absence of starch.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Experiments, Plant Nutrition',
            'examples': ["Colour change with the starch test cannot be seen in a leaf after keeping it in dark for 48 hours.", "Light is essential for starch production in leaves, as demonstrated by the starch test."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_boiling_leaves_in_water_for_starch_test'))
    def rule_effect_of_boiling_leaves_in_water_for_starch_test(self):
        """Boiling a leaf in water is a preliminary step in the starch test. It serves to kill the plant cells, break down cell walls, and increase the permeability of the leaf, which facilitates the removal of chlorophyll in subsequent steps and allows iodine to penetrate for the starch test."""
        self.response = {
            'concept': 'Effect of Boiling Leaves in Water for Starch Test',
            'explanation': """Boiling a leaf in water is a preliminary step in the starch test. It serves to kill the plant cells, break down cell walls, and increase the permeability of the leaf, which facilitates the removal of chlorophyll in subsequent steps and allows iodine to penetrate for the starch test.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis Experiments, Plant Physiology',
            'examples': ["Leaf should be boiled in water for the starch test.", "When leaves are boiled in water the permeability of them increases.", "Boiling helps soften the leaf tissue, preparing it for chlorophyll extraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='primary_location_of_photosynthesis'))
    def rule_primary_location_of_photosynthesis(self):
        """Photosynthesis predominantly occurs in the leaves of plants, which are specialized organs containing a high concentration of chloroplasts, the organelles responsible for this process."""
        self.response = {
            'concept': 'Primary Location of Photosynthesis',
            'explanation': """Photosynthesis predominantly occurs in the leaves of plants, which are specialized organs containing a high concentration of chloroplasts, the organelles responsible for this process.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis, Plant Anatomy',
            'examples': ["Photosynthesis takes place in leaves.", "Leaves are the primary sites for photosynthesis in most plants."]
        }
        self.halt()

    @Rule(Fact(query_topic='organisms_capable_of_photosynthesis'))
    def rule_organisms_capable_of_photosynthesis(self):
        """Photosynthesis is a metabolic process primarily carried out by organisms that possess chlorophyll or similar photosynthetic pigments, most notably green plants, algae, and some bacteria."""
        self.response = {
            'concept': 'Organisms Capable of Photosynthesis',
            'explanation': """Photosynthesis is a metabolic process primarily carried out by organisms that possess chlorophyll or similar photosynthetic pigments, most notably green plants, algae, and some bacteria.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis, Plant Diversity',
            'examples': ["Photosynthesis takes place only in green plants.", "Green plants use photosynthesis to produce their food."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_light_deprivation_on_plant_color'))
    def rule_effect_of_light_deprivation_on_plant_color(self):
        """When green plants are deprived of light for an extended period, they stop producing chlorophyll, the green pigment. This leads to the degradation of existing chlorophyll and the visible loss of green color, causing the plant to turn yellow (a process known as etiolation)."""
        self.response = {
            'concept': 'Effect of Light Deprivation on Plant Color',
            'explanation': """When green plants are deprived of light for an extended period, they stop producing chlorophyll, the green pigment. This leads to the degradation of existing chlorophyll and the visible loss of green color, causing the plant to turn yellow (a process known as etiolation).""",
            'topic': 'Biology',
            'subtopic': 'Plant Physiology, Photosynthesis',
            'examples': ["When grass is covered for three days with a black coloured polythene, it becomes yellow in colour.", "Lack of light prevents chlorophyll synthesis, causing plants to turn yellow."]
        }
        self.halt()

    @Rule(Fact(query_topic='photosynthesis__technical_term_'))
    def rule_photosynthesis__technical_term_(self):
        """Photosynthesis (m%NdixYaf,aIKh JÎzöuõS¨¦) is the biochemical process by which plants, algae, and some bacteria convert light energy into chemical energy, usually in the form of glucose."""
        self.response = {
            'concept': 'Photosynthesis (Technical Term)',
            'explanation': """Photosynthesis (m%NdixYaf,aIKh JÎzöuõS¨¦) is the biochemical process by which plants, algae, and some bacteria convert light energy into chemical energy, usually in the form of glucose.""",
            'topic': 'Biology',
            'subtopic': 'Photosynthesis, Vocabulary',
            'examples': ["Photosynthesis (m%NdixYaf,aIKh JÎzöuõS¨¦) is vital for life on Earth.", "It is the process plants use to create food from sunlight."]
        }
        self.halt()

    @Rule(Fact(query_topic='chloroplasts__technical_term_'))
    def rule_chloroplasts__technical_term_(self):
        """Chloroplasts (yß;,j £aø\¯Ä¸©o) are specialized organelles found in plant cells and some other eukaryotic cells that conduct photosynthesis. They contain chlorophyll and are the sites of light-dependent and light-independent reactions."""
        self.response = {
            'concept': 'Chloroplasts (Technical Term)',
            'explanation': """Chloroplasts (yß;,j £aø\¯Ä¸©o) are specialized organelles found in plant cells and some other eukaryotic cells that conduct photosynthesis. They contain chlorophyll and are the sites of light-dependent and light-independent reactions.""",
            'topic': 'Biology',
            'subtopic': 'Cell Biology, Photosynthesis, Vocabulary',
            'examples': ["Chloroplasts (yß;,j £aø\\¯Ä¸©o) are where photosynthesis takes place.", "They are green due to the presence of chlorophyll."]
        }
        self.halt()

    @Rule(Fact(query_topic='chlorophyll__technical_term_'))
    def rule_chlorophyll__technical_term_(self):
        """Chlorophyll (yß;m%o £aø\®) is the primary green pigment found in plants, algae, and cyanobacteria. It is essential for photosynthesis as it absorbs light energy, particularly in the red and blue parts of the electromagnetic spectrum."""
        self.response = {
            'concept': 'Chlorophyll (Technical Term)',
            'explanation': """Chlorophyll (yß;m%o £aø\®) is the primary green pigment found in plants, algae, and cyanobacteria. It is essential for photosynthesis as it absorbs light energy, particularly in the red and blue parts of the electromagnetic spectrum.""",
            'topic': 'Biology',
            'subtopic': 'Biochemistry, Photosynthesis, Vocabulary',
            'examples': ["Chlorophyll (yß;m%o £aø\\®) gives plants their green color.", "It is responsible for capturing sunlight during photosynthesis."]
        }
        self.halt()

    @Rule(Fact(query_topic='aquatic_plants__technical_term_'))
    def rule_aquatic_plants__technical_term_(self):
        """Aquatic plants (c,rey Ydl }ºÁõÌ uõÁµ[PÒ) are plants that have adapted to live in aquatic environments, such as oceans, lakes, rivers, or wetlands. They can be submerged, emergent, or floating."""
        self.response = {
            'concept': 'Aquatic Plants (Technical Term)',
            'explanation': """Aquatic plants (c,rey Ydl }ºÁõÌ uõÁµ[PÒ) are plants that have adapted to live in aquatic environments, such as oceans, lakes, rivers, or wetlands. They can be submerged, emergent, or floating.""",
            'topic': 'Biology',
            'subtopic': 'Botany, Ecology, Vocabulary',
            'examples': ["Aquatic plants (c,rey Ydl }ºÁõÌ uõÁµ[PÒ) are found in water bodies.", "Water lilies and duckweed are examples of aquatic plants."]
        }
        self.halt()

    @Rule(Fact(query_topic='diverse_animal_hearing_ranges'))
    def rule_diverse_animal_hearing_ranges(self):
        """Animals possess varied hearing ranges, allowing some to hear frequencies (like infra-sound or ultrasound) that are outside the human audible spectrum."""
        self.response = {
            'concept': 'Diverse Animal Hearing Ranges',
            'explanation': """Animals possess varied hearing ranges, allowing some to hear frequencies (like infra-sound or ultrasound) that are outside the human audible spectrum.""",
            'topic': 'Biology',
            'subtopic': 'Animal Senses',
            'examples': ["Elephants can hear very low frequencies (infra-sound).", "Rabbits, dolphins, and bats can hear very high frequencies (ultrasound).", "Dogs can hear sounds up to approximately 40,000 Hz."]
        }
        self.halt()

    @Rule(Fact(query_topic='bat_echolocation_using_ultrasound'))
    def rule_bat_echolocation_using_ultrasound(self):
        """Bats use ultrasound waves to navigate and avoid obstacles, particularly at night. They emit ultrasound pulses, and by receiving the reflected waves, they can judge the position of objects."""
        self.response = {
            'concept': 'Bat Echolocation using Ultrasound',
            'explanation': """Bats use ultrasound waves to navigate and avoid obstacles, particularly at night. They emit ultrasound pulses, and by receiving the reflected waves, they can judge the position of objects.""",
            'topic': 'Biology',
            'subtopic': 'Animal Behavior / Applications of Ultrasound',
            'examples': ["A bat emits ultrasound to detect a tree in its flight path.", "Reflected ultrasound waves allow bats to build a 'sound map' of their surroundings.", "This process helps bats avoid collisions while flying in darkness."]
        }
        self.halt()

    @Rule(Fact(query_topic='dolphin_uses_of_ultrasound'))
    def rule_dolphin_uses_of_ultrasound(self):
        """Dolphins utilize ultrasound waves for various critical tasks, including locating small fish for prey, detecting and avoiding predators like sharks, and communicating with other dolphins."""
        self.response = {
            'concept': 'Dolphin Uses of Ultrasound',
            'explanation': """Dolphins utilize ultrasound waves for various critical tasks, including locating small fish for prey, detecting and avoiding predators like sharks, and communicating with other dolphins.""",
            'topic': 'Biology',
            'subtopic': 'Animal Behavior / Applications of Ultrasound',
            'examples': ["Dolphins use ultrasound to find hidden fish.", "They can identify the presence of sharks through ultrasound.", "Ultrasound is a key method of communication among dolphins."]
        }
        self.halt()

    @Rule(Fact(query_topic='digestion_of_food'))
    def rule_digestion_of_food(self):
        """The process by which complex organic compounds are converted into simple organic products to be absorbed into the human body."""
        self.response = {
            'concept': 'Digestion of food',
            'explanation': """The process by which complex organic compounds are converted into simple organic products to be absorbed into the human body.""",
            'topic': 'Biology',
            'subtopic': 'Food Digestion',
            'examples': ["Breaking down carbohydrates from bread into simple sugars.", "Converting proteins from meat into amino acids.", "Lipids from oils being broken down into fatty acids and glycerol."]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_process__digestion_'))
    def rule_mechanical_process__digestion_(self):
        """During digestion, the physical alteration of the food's nature, involving actions like breaking, grinding, and mixing, without changing its chemical composition."""
        self.response = {
            'concept': 'Mechanical process (digestion)',
            'explanation': """During digestion, the physical alteration of the food's nature, involving actions like breaking, grinding, and mixing, without changing its chemical composition.""",
            'topic': 'Biology',
            'subtopic': 'Food Digestion',
            'examples': ["Breaking down of food into small pieces by teeth inside mouth.", "Churning of food in the stomach.", "Segmentation contractions in the small intestine."]
        }
        self.halt()

    @Rule(Fact(query_topic='chemical_process__digestion_'))
    def rule_chemical_process__digestion_(self):
        """During digestion, the breakdown of insoluble complex compounds into simple molecules by the action of enzymes, changing their chemical composition."""
        self.response = {
            'concept': 'Chemical process (digestion)',
            'explanation': """During digestion, the breakdown of insoluble complex compounds into simple molecules by the action of enzymes, changing their chemical composition.""",
            'topic': 'Biology',
            'subtopic': 'Food Digestion',
            'examples': ["Starch is converted into maltose by salivary amylase (ptyalin).", "Proteins are broken down into polypeptides by pepsin in the stomach.", "Fats are emulsified by bile and then broken down by lipase."]
        }
        self.halt()

    @Rule(Fact(query_topic='nutrients_usable_without_digestion'))
    def rule_nutrients_usable_without_digestion(self):
        """Some nutrients can be directly utilized by the body without undergoing any prior digestive processes."""
        self.response = {
            'concept': 'Nutrients Usable Without Digestion',
            'explanation': """Some nutrients can be directly utilized by the body without undergoing any prior digestive processes.""",
            'topic': 'Biology',
            'subtopic': 'Nutrition/Digestion',
            'examples': ["mineral salts", "some vitamins", "glucose, fructose and galactose"]
        }
        self.halt()

    @Rule(Fact(query_topic='digestive_system__organs_'))
    def rule_digestive_system__organs_(self):
        """The organs that are involved in the process of food digestion are collectively referred to as the digestive system."""
        self.response = {
            'concept': 'Digestive System (Organs)',
            'explanation': """The organs that are involved in the process of food digestion are collectively referred to as the digestive system.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestive System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='human_digestive_system__structure___functions_'))
    def rule_human_digestive_system__structure___functions_(self):
        """The human digestive system is a continuous tube that extends from the mouth to the anus. Its structure is modified at different points, and various glands (salivary glands, pancreas, liver) connect to it at different sites to supply enzymes and other substances like bile. Its primary functions include food digestion, absorption of digested end products, and the removal of undigested materials from the body."""
        self.response = {
            'concept': 'Human Digestive System (Structure & Functions)',
            'explanation': """The human digestive system is a continuous tube that extends from the mouth to the anus. Its structure is modified at different points, and various glands (salivary glands, pancreas, liver) connect to it at different sites to supply enzymes and other substances like bile. Its primary functions include food digestion, absorption of digested end products, and the removal of undigested materials from the body.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestive System',
            'examples': ["salivary glands supply enzymes", "liver supplies bile", "removal of undigested materials from the body"]
        }
        self.halt()

    @Rule(Fact(query_topic='parts_of_the_human_digestive_tract'))
    def rule_parts_of_the_human_digestive_tract(self):
        """These are the individual structures that collectively form the human digestive tract, through which food passes and is processed."""
        self.response = {
            'concept': 'Parts of the Human Digestive Tract',
            'explanation': """These are the individual structures that collectively form the human digestive tract, through which food passes and is processed.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestive System',
            'examples': ["Buccal cavity", "Oesophagus", "Stomach", "Small intestine", "Large intestine", "Anus"]
        }
        self.halt()

    @Rule(Fact(query_topic='buccal_cavity__mouth_'))
    def rule_buccal_cavity__mouth_(self):
        """The buccal cavity, or mouth, is the initial segment of the digestive tract, opening to the external environment. It is bordered by muscular lips, composed of upper and lower jaws (where only the lower jaw is movable), and surrounded by cheeks. Teeth are present in both jaws, and the tongue is anchored to its floor. It also houses three salivary glands."""
        self.response = {
            'concept': 'Buccal Cavity (Mouth)',
            'explanation': """The buccal cavity, or mouth, is the initial segment of the digestive tract, opening to the external environment. It is bordered by muscular lips, composed of upper and lower jaws (where only the lower jaw is movable), and surrounded by cheeks. Teeth are present in both jaws, and the tongue is anchored to its floor. It also houses three salivary glands.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestion in Mouth',
            'examples': ["surrounded by muscular lips", "teeth present in both jaws", "tongue attached to the floor"]
        }
        self.halt()

    @Rule(Fact(query_topic='salivary_glands__buccal_cavity_'))
    def rule_salivary_glands__buccal_cavity_(self):
        """Three salivary glands are situated within the buccal cavity, and their primary function is to secrete saliva."""
        self.response = {
            'concept': 'Salivary Glands (Buccal Cavity)',
            'explanation': """Three salivary glands are situated within the buccal cavity, and their primary function is to secrete saliva.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestive Glands',
            'examples': ["Presence of three salivary glands", "Secretion of saliva"]
        }
        self.halt()

    @Rule(Fact(query_topic='tongue__functions_in_digestion_'))
    def rule_tongue__functions_in_digestion_(self):
        """The tongue, which is attached to the floor of the buccal cavity, performs multiple roles in digestion, including identifying tastes, mixing food thoroughly with saliva, and assisting in swallowing."""
        self.response = {
            'concept': 'Tongue (Functions in Digestion)',
            'explanation': """The tongue, which is attached to the floor of the buccal cavity, performs multiple roles in digestion, including identifying tastes, mixing food thoroughly with saliva, and assisting in swallowing.""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy/Digestion in Mouth',
            'examples': ["identification of taste", "mixing of food with saliva", "swallowing"]
        }
        self.halt()

    @Rule(Fact(query_topic='salivary_amylase_action'))
    def rule_salivary_amylase_action(self):
        """The salivary amylase enzyme (ptyalin) acts on starch during food digestion in the mouth, partially breaking it down into maltose. This marks the beginning of food digestion."""
        self.response = {
            'concept': 'Salivary Amylase Action',
            'explanation': """The salivary amylase enzyme (ptyalin) acts on starch during food digestion in the mouth, partially breaking it down into maltose. This marks the beginning of food digestion.""",
            'topic': 'Biology',
            'subtopic': 'Digestion in Mouth',
            'examples': ["When rice is chewed for some time, its starch is digested into maltose.", "Bread, when chewed for a while, undergoes partial starch digestion by salivary amylase.", "The initial breakdown of complex carbohydrates like starch begins in the oral cavity."]
        }
        self.halt()

    @Rule(Fact(query_topic='maltose_and_sweet_taste_sensation'))
    def rule_maltose_and_sweet_taste_sensation(self):
        """As starch is digested into maltose by salivary amylase in the mouth, and because maltose is a sweet-tasting disaccharide, we perceive a sweet taste."""
        self.response = {
            'concept': 'Maltose and Sweet Taste Sensation',
            'explanation': """As starch is digested into maltose by salivary amylase in the mouth, and because maltose is a sweet-tasting disaccharide, we perceive a sweet taste.""",
            'topic': 'Biology',
            'subtopic': 'Sensory Perception / Digestion in Mouth',
            'examples': ["Chewing a piece of plain bread for a prolonged period makes it taste slightly sweet.", "The sweet sensation felt after holding cooked rice in the mouth is due to maltose formation.", "The sweetness experienced is a direct result of starch conversion to maltose."]
        }
        self.halt()

    @Rule(Fact(query_topic='bolus_formation_and_initial_transport'))
    def rule_bolus_formation_and_initial_transport(self):
        """After initial digestion and chewing in the mouth, food is formed into a soft mass called a bolus, which is then pushed to the posterior part of the buccal cavity (mouth) and subsequently into the pharynx."""
        self.response = {
            'concept': 'Bolus Formation and Initial Transport',
            'explanation': """After initial digestion and chewing in the mouth, food is formed into a soft mass called a bolus, which is then pushed to the posterior part of the buccal cavity (mouth) and subsequently into the pharynx.""",
            'topic': 'Biology',
            'subtopic': 'Food Transport',
            'examples': ["After mastication, food is compacted into a bolus for easier swallowing.", "The tongue helps in forming the bolus and moving it towards the back of the throat.", "The bolus is the initial form of ingested food prepared for passage down the digestive tract."]
        }
        self.halt()

    @Rule(Fact(query_topic='pharynx_as_a_common_passage'))
    def rule_pharynx_as_a_common_passage(self):
        """The pharynx is an anatomical region that serves as a shared pathway for both the respiratory system (air passage) and the digestive system (food passage)."""
        self.response = {
            'concept': 'Pharynx as a Common Passage',
            'explanation': """The pharynx is an anatomical region that serves as a shared pathway for both the respiratory system (air passage) and the digestive system (food passage).""",
            'topic': 'Biology',
            'subtopic': 'Anatomy of Digestive/Respiratory System',
            'examples': ["Air inhaled through the nasal cavity passes through the pharynx on its way to the larynx.", "Swallowed food from the mouth passes through the pharynx on its way to the oesophagus.", "Problems in the pharynx can affect both breathing and swallowing."]
        }
        self.halt()

    @Rule(Fact(query_topic='epiglottis_function_in_swallowing'))
    def rule_epiglottis_function_in_swallowing(self):
        """The epiglottis is a movable cartilaginous flap located just above the opening of the trachea. When a bolus is swallowed, the epiglottis moves downwards to close the trachea's opening, preventing food from entering the respiratory tract and directing it into the oesophagus."""
        self.response = {
            'concept': 'Epiglottis Function in Swallowing',
            'explanation': """The epiglottis is a movable cartilaginous flap located just above the opening of the trachea. When a bolus is swallowed, the epiglottis moves downwards to close the trachea's opening, preventing food from entering the respiratory tract and directing it into the oesophagus.""",
            'topic': 'Biology',
            'subtopic': 'Swallowing Mechanism',
            'examples': ["When you drink water, the epiglottis automatically closes off your windpipe.", "Without the epiglottis, food would frequently enter the trachea, causing choking.", "The epiglottis acts as a protective lid for the respiratory pathway during deglutition."]
        }
        self.halt()

    @Rule(Fact(query_topic='dangers_of_tracheal_blockage'))
    def rule_dangers_of_tracheal_blockage(self):
        """If food accidentally enters the trachea and is not removed instantly, the epiglottis blocks the respiratory tract. This prolonged blockage can obstruct breathing and potentially lead to death."""
        self.response = {
            'concept': 'Dangers of Tracheal Blockage',
            'explanation': """If food accidentally enters the trachea and is not removed instantly, the epiglottis blocks the respiratory tract. This prolonged blockage can obstruct breathing and potentially lead to death.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory Safety / Choking Hazards',
            'examples': ["Choking occurs when food lodges in the trachea, preventing air flow.", "If the respiratory tract remains blocked by food, the person may suffocate.", "Heimlich maneuver is used to dislodge food from a blocked trachea."]
        }
        self.halt()

    @Rule(Fact(query_topic='peristaltic_movements_in_oesophagus'))
    def rule_peristaltic_movements_in_oesophagus(self):
        """The oesophagus is a muscular, constricted tube. Food (bolus) is propelled through it by peristaltic movements, which are wave-like contractions and relaxations of its muscular wall, providing the force to move the bolus forward."""
        self.response = {
            'concept': 'Peristaltic Movements in Oesophagus',
            'explanation': """The oesophagus is a muscular, constricted tube. Food (bolus) is propelled through it by peristaltic movements, which are wave-like contractions and relaxations of its muscular wall, providing the force to move the bolus forward.""",
            'topic': 'Biology',
            'subtopic': 'Food Transport / Oesophagus',
            'examples': ["Food travels down the oesophagus even when a person is eating upside down, due to peristalsis.", "The rhythmic squeezing of the oesophageal muscles pushes swallowed food towards the stomach.", "Peristalsis ensures one-way movement of the bolus without relying on gravity."]
        }
        self.halt()

    @Rule(Fact(query_topic='food_transport_to_stomach'))
    def rule_food_transport_to_stomach(self):
        """Following its passage through the oesophagus, food continues its journey into the stomach, primarily driven by ongoing peristaltic movements."""
        self.response = {
            'concept': 'Food Transport to Stomach',
            'explanation': """Following its passage through the oesophagus, food continues its journey into the stomach, primarily driven by ongoing peristaltic movements.""",
            'topic': 'Biology',
            'subtopic': 'Food Transport',
            'examples': ["After leaving the oesophagus, the bolus is passed into the stomach.", "The muscular contractions of the digestive tract ensure food reaches the stomach from the oesophagus.", "Peristalsis is responsible for the final push of food into the stomach's opening."]
        }
        self.halt()

    @Rule(Fact(query_topic='digestion_in_stomach_and_chyme_formation'))
    def rule_digestion_in_stomach_and_chyme_formation(self):
        """The stomach is a dilated, sac-like organ. Through the peristaltic activity of its muscular walls, the bolus is mechanically broken down and thoroughly mixed with digestive secretions, transforming it into a semi-liquid substance called chyme."""
        self.response = {
            'concept': 'Digestion in Stomach and Chyme Formation',
            'explanation': """The stomach is a dilated, sac-like organ. Through the peristaltic activity of its muscular walls, the bolus is mechanically broken down and thoroughly mixed with digestive secretions, transforming it into a semi-liquid substance called chyme.""",
            'topic': 'Biology',
            'subtopic': 'Digestion in Stomach',
            'examples': ["The churning motion of the stomach muscles helps in mixing food with gastric juices.", "After several hours in the stomach, solid food is converted into a thick, acidic chyme.", "Mechanical digestion in the stomach contributes to the formation of chyme."]
        }
        self.halt()

    @Rule(Fact(query_topic='gastric_juice'))
    def rule_gastric_juice(self):
        """Several different secretions are released into the stomach lumen, and these are collectively referred to as gastric juice. This juice plays a crucial role in chemical digestion."""
        self.response = {
            'concept': 'Gastric Juice',
            'explanation': """Several different secretions are released into the stomach lumen, and these are collectively referred to as gastric juice. This juice plays a crucial role in chemical digestion.""",
            'topic': 'Biology',
            'subtopic': 'Digestion in Stomach',
            'examples': ["Gastric juice contains hydrochloric acid, which helps kill bacteria and denature proteins.", "Enzymes like pepsinogen are components of gastric juice.", "The acidic environment created by gastric juice is optimal for certain digestive enzymes."]
        }
        self.halt()

    @Rule(Fact(query_topic='gastric_juice_composition_and_initial_digestion'))
    def rule_gastric_juice_composition_and_initial_digestion(self):
        """Gastric juice, secreted in the stomach, primarily contains hydrochloric acid (HCl) and pepsin enzyme. HCl activates pepsin, which then initiates protein digestion by breaking them down into polypeptides. In infants, renin is also present, causing milk coagulation."""
        self.response = {
            'concept': 'Gastric Juice Composition and Initial Digestion',
            'explanation': """Gastric juice, secreted in the stomach, primarily contains hydrochloric acid (HCl) and pepsin enzyme. HCl activates pepsin, which then initiates protein digestion by breaking them down into polypeptides. In infants, renin is also present, causing milk coagulation.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Stomach',
            'examples': ["Hydrochloric acid (HCl) activates pepsin in the stomach.", "Pepsin begins the breakdown of proteins into polypeptides.", "Renin helps infants coagulate milk in their stomachs."]
        }
        self.halt()

    @Rule(Fact(query_topic='stomach_function_and_absorption_capacity'))
    def rule_stomach_function_and_absorption_capacity(self):
        """Food remains in the stomach for approximately three hours. While the final digested end products are not absorbed here, the stomach can absorb some water, glucose, and certain drugs."""
        self.response = {
            'concept': 'Stomach Function and Absorption Capacity',
            'explanation': """Food remains in the stomach for approximately three hours. While the final digested end products are not absorbed here, the stomach can absorb some water, glucose, and certain drugs.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Stomach',
            'examples': ["Food typically stays in the stomach for about three hours.", "The stomach can absorb water and glucose.", "Certain drugs can be absorbed directly from the stomach."]
        }
        self.halt()

    @Rule(Fact(query_topic='chyme_composition_and_release'))
    def rule_chyme_composition_and_release(self):
        """Chyme is the semi-digested food mixture released from the stomach into the duodenum (the proximal part of the small intestine). It consists of partially digested proteins, digested and undigested carbohydrates, undigested lipids, water, minerals, and vitamins."""
        self.response = {
            'concept': 'Chyme Composition and Release',
            'explanation': """Chyme is the semi-digested food mixture released from the stomach into the duodenum (the proximal part of the small intestine). It consists of partially digested proteins, digested and undigested carbohydrates, undigested lipids, water, minerals, and vitamins.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Stomach to Small Intestine Transition',
            'examples': ["Chyme contains partially digested proteins and undigested lipids.", "Water, minerals, and vitamins are components of chyme.", "Chyme is released into the duodenum part by part."]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanism_of_hunger_sensation'))
    def rule_mechanism_of_hunger_sensation(self):
        """When the stomach is empty, it continues to contract. If it remains empty for an extended period, the rate of contraction increases significantly, leading to pain. This pain provides a sense of hunger, signaling the body's need for food."""
        self.response = {
            'concept': 'Mechanism of Hunger Sensation',
            'explanation': """When the stomach is empty, it continues to contract. If it remains empty for an extended period, the rate of contraction increases significantly, leading to pain. This pain provides a sense of hunger, signaling the body's need for food.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System Physiology',
            'examples': ["Empty stomach contractions increase in rate over time.", "High rates of stomach contraction cause a painful sensation.", "Hunger is a signal indicating the body needs food."]
        }
        self.halt()

    @Rule(Fact(query_topic='role_of_small_intestine_in_chemical_digestion'))
    def rule_role_of_small_intestine_in_chemical_digestion(self):
        """The small intestine is the primary site for the chemical digestion of food. This extensive digestion involves both pancreatic enzymes and enzymes secreted by the intestinal walls. The small intestine is approximately 7 meters long, with its C-shaped proximal part known as the duodenum."""
        self.response = {
            'concept': 'Role of Small Intestine in Chemical Digestion',
            'explanation': """The small intestine is the primary site for the chemical digestion of food. This extensive digestion involves both pancreatic enzymes and enzymes secreted by the intestinal walls. The small intestine is approximately 7 meters long, with its C-shaped proximal part known as the duodenum.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Small Intestine',
            'examples': ["Most chemical digestion occurs in the small intestine.", "Pancreatic and intestinal enzymes are crucial for small intestine digestion.", "The small intestine, about 7 m long, starts with the duodenum."]
        }
        self.halt()

    @Rule(Fact(query_topic='duodenum_as_an_entry_point_for_digestive_juices'))
    def rule_duodenum_as_an_entry_point_for_digestive_juices(self):
        """The duodenum, the C-shaped proximal part of the small intestine, serves as the entry point for digestive fluids from accessory organs. The ducts from the pancreas and the gall bladder both open into the duodenum through a single pore, delivering pancreatic juice and bile, respectively."""
        self.response = {
            'concept': 'Duodenum as an Entry Point for Digestive Juices',
            'explanation': """The duodenum, the C-shaped proximal part of the small intestine, serves as the entry point for digestive fluids from accessory organs. The ducts from the pancreas and the gall bladder both open into the duodenum through a single pore, delivering pancreatic juice and bile, respectively.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Small Intestine Anatomy',
            'examples': ["The pancreatic duct opens into the duodenum.", "Bile from the gall bladder enters the duodenum.", "A single pore in the duodenum receives secretions from the pancreas and gall bladder."]
        }
        self.halt()

    @Rule(Fact(query_topic='pancreatic_juice_and_its_enzymes'))
    def rule_pancreatic_juice_and_its_enzymes(self):
        """Pancreatic juice is secreted into the duodenum via the pancreatic duct. It contains three main enzymes essential for digestion: trypsin, which digests proteins; amylase, which digests carbohydrates; and lipase, which digests lipids."""
        self.response = {
            'concept': 'Pancreatic Juice and its Enzymes',
            'explanation': """Pancreatic juice is secreted into the duodenum via the pancreatic duct. It contains three main enzymes essential for digestion: trypsin, which digests proteins; amylase, which digests carbohydrates; and lipase, which digests lipids.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Pancreatic Secretions',
            'examples': ["Pancreatic juice is secreted into the duodenum.", "Trypsin, amylase, and lipase are the main enzymes in pancreatic juice.", "Lipase in pancreatic juice digests lipids."]
        }
        self.halt()

    @Rule(Fact(query_topic='bile__production__storage__and_components'))
    def rule_bile__production__storage__and_components(self):
        """Bile is a digestive fluid produced by the liver and stored in the gall bladder before being carried through the bile duct to the duodenum. Its composition includes bile pigments, bile salts, bicarbonate ions, and water."""
        self.response = {
            'concept': 'Bile: Production, Storage, and Components',
            'explanation': """Bile is a digestive fluid produced by the liver and stored in the gall bladder before being carried through the bile duct to the duodenum. Its composition includes bile pigments, bile salts, bicarbonate ions, and water.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Bile',
            'examples': ["Bile is produced in the liver and stored in the gall bladder.", "Bile is delivered to the duodenum via the bile duct.", "Bile contains bile salts, bile pigments, and water."]
        }
        self.halt()

    @Rule(Fact(query_topic='emulsification_of_lipids_by_bile'))
    def rule_emulsification_of_lipids_by_bile(self):
        """When bile mixes with food in the duodenum, it causes the lipids to break down into smaller droplets through a process called emulsification. This action significantly increases the surface area of the lipids, making them more accessible for enzymatic digestion by lipase."""
        self.response = {
            'concept': 'Emulsification of Lipids by Bile',
            'explanation': """When bile mixes with food in the duodenum, it causes the lipids to break down into smaller droplets through a process called emulsification. This action significantly increases the surface area of the lipids, making them more accessible for enzymatic digestion by lipase.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Lipid Digestion',
            'examples': ["Bile emulsifies lipids in the duodenum.", "Emulsification breaks down large lipid globules into small droplets.", "Increased surface area from emulsification enhances enzyme action on lipids."]
        }
        self.halt()

    @Rule(Fact(query_topic='intestinal_juice_composition_and_function'))
    def rule_intestinal_juice_composition_and_function(self):
        """Intestinal juice is secreted by the walls of the small intestine. It contains several key enzymes, including maltase, sucrase, and lactase for carbohydrate digestion, peptidase for protein digestion, and mucus. The mucus lubricates food, facilitating its passage along the gut."""
        self.response = {
            'concept': 'Intestinal Juice Composition and Function',
            'explanation': """Intestinal juice is secreted by the walls of the small intestine. It contains several key enzymes, including maltase, sucrase, and lactase for carbohydrate digestion, peptidase for protein digestion, and mucus. The mucus lubricates food, facilitating its passage along the gut.""",
            'topic': 'Biology',
            'subtopic': 'Digestion - Intestinal Secretions',
            'examples': ["Maltase, sucrase, and lactase are found in intestinal juice.", "Peptidase in intestinal juice aids protein digestion.", "Mucus lubricates food, easing its movement through the gut."]
        }
        self.halt()

    @Rule(Fact(query_topic='protection_of_gut_wall_from_digestive_enzymes'))
    def rule_protection_of_gut_wall_from_digestive_enzymes(self):
        """The inner lining of the gut wall, specifically the stomach and intestine, is protected from its own protein-digesting enzymes by a layer of mucus. This mucus acts as a barrier, preventing the enzymes from damaging the organ walls."""
        self.response = {
            'concept': 'Protection of Gut Wall from Digestive Enzymes',
            'explanation': """The inner lining of the gut wall, specifically the stomach and intestine, is protected from its own protein-digesting enzymes by a layer of mucus. This mucus acts as a barrier, preventing the enzymes from damaging the organ walls.""",
            'topic': 'Biology',
            'subtopic': 'Digestion',
            'examples': ["Mucus forms a protective layer on the stomach lining.", "Protein digestive enzymes are prevented from self-digestion of the gut wall by mucus."]
        }
        self.halt()

    @Rule(Fact(query_topic='pancreatic_enzymes_for_digestion_in_small_intestine'))
    def rule_pancreatic_enzymes_for_digestion_in_small_intestine(self):
        """The pancreas secretes several key enzymes into the small intestine to break down food components. Trypsin digests proteins into polypeptides, amylase breaks down starch into maltose, and lipase breaks down lipids into fatty acids and glycerol."""
        self.response = {
            'concept': 'Pancreatic Enzymes for Digestion in Small Intestine',
            'explanation': """The pancreas secretes several key enzymes into the small intestine to break down food components. Trypsin digests proteins into polypeptides, amylase breaks down starch into maltose, and lipase breaks down lipids into fatty acids and glycerol.""",
            'topic': 'Biology',
            'subtopic': 'Enzymes in Digestion',
            'examples': ["Trypsin converts protein into polypeptides.", "Pancreatic amylase breaks down starch into maltose.", "Lipase digests lipids into fatty acids and glycerol."]
        }
        self.halt()

    @Rule(Fact(query_topic='small_intestine_enzymes_for_final_digestion'))
    def rule_small_intestine_enzymes_for_final_digestion(self):
        """The small intestine itself produces enzymes that complete the breakdown of food molecules. Maltase digests maltose into glucose, sucrase digests sucrose into glucose and fructose, lactase digests lactose into glucose and galactose, and peptidase digests polypeptides into amino acids."""
        self.response = {
            'concept': 'Small Intestine Enzymes for Final Digestion',
            'explanation': """The small intestine itself produces enzymes that complete the breakdown of food molecules. Maltase digests maltose into glucose, sucrase digests sucrose into glucose and fructose, lactase digests lactose into glucose and galactose, and peptidase digests polypeptides into amino acids.""",
            'topic': 'Biology',
            'subtopic': 'Enzymes in Digestion',
            'examples': ["Maltase breaks down maltose into glucose.", "Lactase digests lactose into glucose and galactose.", "Peptidase converts polypeptides into amino acids."]
        }
        self.halt()

    @Rule(Fact(query_topic='final_end_products_of_digestion'))
    def rule_final_end_products_of_digestion(self):
        """The complete breakdown of macronutrients results in specific end products ready for absorption. Carbohydrates are broken down into monosaccharides (glucose, fructose, galactose), proteins into amino acids, and lipids into fatty acids and glycerol."""
        self.response = {
            'concept': 'Final End Products of Digestion',
            'explanation': """The complete breakdown of macronutrients results in specific end products ready for absorption. Carbohydrates are broken down into monosaccharides (glucose, fructose, galactose), proteins into amino acids, and lipids into fatty acids and glycerol.""",
            'topic': 'Biology',
            'subtopic': 'Digestion',
            'examples': ["Monosaccharides are the end products of carbohydrate digestion.", "Amino acids are the end products of protein digestion.", "Fatty acids and glycerol are the end products of lipid digestion."]
        }
        self.halt()

    @Rule(Fact(query_topic='adaptations_of_small_intestine_for_absorption'))
    def rule_adaptations_of_small_intestine_for_absorption(self):
        """The small intestine is highly adapted to efficiently absorb digested food products. Its adaptations include being a long tube, having circular folds in its inner wall, possessing finger-like projections called villi, and microvilli on the epithelial cells of the villi. Villi also have a thin epithelial lining and are highly vascularized."""
        self.response = {
            'concept': 'Adaptations of Small Intestine for Absorption',
            'explanation': """The small intestine is highly adapted to efficiently absorb digested food products. Its adaptations include being a long tube, having circular folds in its inner wall, possessing finger-like projections called villi, and microvilli on the epithelial cells of the villi. Villi also have a thin epithelial lining and are highly vascularized.""",
            'topic': 'Biology',
            'subtopic': 'Absorption / Digestive System Anatomy',
            'examples': ["The small intestine's long length maximizes contact time for absorption.", "Villi and microvilli increase the surface area available for nutrient absorption.", "Circular folds in the inner wall enhance the efficiency of absorption."]
        }
        self.halt()

    @Rule(Fact(query_topic='pathways_of_absorption_for_digested_end_products'))
    def rule_pathways_of_absorption_for_digested_end_products(self):
        """Different digested end products are absorbed into the circulatory system via specific pathways within the villi. Amino acids, vitamins, mineral salts, and monosaccharides (glucose, galactose, fructose) are absorbed directly into the blood capillaries. Fatty acids and glycerol, however, are absorbed into the lacteals before eventually entering the blood circulatory system."""
        self.response = {
            'concept': 'Pathways of Absorption for Digested End Products',
            'explanation': """Different digested end products are absorbed into the circulatory system via specific pathways within the villi. Amino acids, vitamins, mineral salts, and monosaccharides (glucose, galactose, fructose) are absorbed directly into the blood capillaries. Fatty acids and glycerol, however, are absorbed into the lacteals before eventually entering the blood circulatory system.""",
            'topic': 'Biology',
            'subtopic': 'Absorption',
            'examples': ["Glucose and amino acids are absorbed into blood capillaries of the villi.", "Fatty acids and glycerol are absorbed into lacteals.", "Vitamins and mineral salts enter the bloodstream via capillaries."]
        }
        self.halt()

    @Rule(Fact(query_topic='glucose_homeostasis__storage_and_release'))
    def rule_glucose_homeostasis__storage_and_release(self):
        """The body regulates blood glucose levels by storing excess glucose and releasing it when needed. High blood glucose is converted into glycogen and stored primarily in the liver. When blood glucose concentration decreases, stored glycogen breaks down to form glucose, which is then added back to the blood."""
        self.response = {
            'concept': 'Glucose Homeostasis: Storage and Release',
            'explanation': """The body regulates blood glucose levels by storing excess glucose and releasing it when needed. High blood glucose is converted into glycogen and stored primarily in the liver. When blood glucose concentration decreases, stored glycogen breaks down to form glucose, which is then added back to the blood.""",
            'topic': 'Biology',
            'subtopic': 'Metabolism / Homeostasis',
            'examples': ["Excess glucose in the blood is converted into glycogen and stored in the liver.", "Glycogen is broken down to produce glucose when blood sugar levels are low.", "The liver acts as a storage site for glucose in the form of glycogen."]
        }
        self.halt()

    @Rule(Fact(query_topic='constipation'))
    def rule_constipation(self):
        """Constipation is characterized by difficulty in defaecation due to the hardening of faecal matter. This occurs when faeces remain in the large intestine for an extended period, leading to excessive absorption of water. It can be caused by certain habits and conditions, and forceful defaecation may damage the anal canal or lead to haemorrhage."""
        self.response = {
            'concept': 'Constipation',
            'explanation': """Constipation is characterized by difficulty in defaecation due to the hardening of faecal matter. This occurs when faeces remain in the large intestine for an extended period, leading to excessive absorption of water. It can be caused by certain habits and conditions, and forceful defaecation may damage the anal canal or lead to haemorrhage.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System Disorders',
            'examples': ["Consumption of food with low dietary fibres", "Not taking required volume of water", "Postponing of defaecation"]
        }
        self.halt()

    @Rule(Fact(query_topic='typhoid'))
    def rule_typhoid(self):
        """Typhoid is an infectious disease caused by a bacterium, with the pathogen transmitted through contaminated food and water. It can enter the body orally, for example, by swimming or bathing in contaminated water, or through contact with a patient's faecal matter, contaminated food, or flies. Symptoms gradually worsen over time."""
        self.response = {
            'concept': 'Typhoid',
            'explanation': """Typhoid is an infectious disease caused by a bacterium, with the pathogen transmitted through contaminated food and water. It can enter the body orally, for example, by swimming or bathing in contaminated water, or through contact with a patient's faecal matter, contaminated food, or flies. Symptoms gradually worsen over time.""",
            'topic': 'Biology',
            'subtopic': 'Infectious Diseases',
            'examples': ["Pain in arms and legs, headache and fever", "Tongue is covered by a plaque", "Ulcers can form in the small intestine and cause bleeding"]
        }
        self.halt()

    @Rule(Fact(query_topic='diarrhoea'))
    def rule_diarrhoea(self):
        """Diarrhoea occurs when the intestines are infected with a virus, bacteria, or a parasite. It is transmitted by the faeces of an infected person. The main symptom is the release of faecal matter in a liquid state due to improper absorption of water in the large intestine, which can lead to dehydration."""
        self.response = {
            'concept': 'Diarrhoea',
            'explanation': """Diarrhoea occurs when the intestines are infected with a virus, bacteria, or a parasite. It is transmitted by the faeces of an infected person. The main symptom is the release of faecal matter in a liquid state due to improper absorption of water in the large intestine, which can lead to dehydration.""",
            'topic': 'Biology',
            'subtopic': 'Infectious Diseases',
            'examples': ["Intestines are infected with a virus, bacteria or a parasite", "Release of faecal matter in liquid state", "Dehydration may occur"]
        }
        self.halt()

    @Rule(Fact(query_topic='dehydration'))
    def rule_dehydration(self):
        """A condition resulting from the loss of fluid from the body. If it worsens due to diarrhoea, it can become fatal, necessitating increased water consumption and immediate medical consultation."""
        self.response = {
            'concept': 'Dehydration',
            'explanation': """A condition resulting from the loss of fluid from the body. If it worsens due to diarrhoea, it can become fatal, necessitating increased water consumption and immediate medical consultation.""",
            'topic': 'Biology',
            'subtopic': 'Health and Diseases',
            'examples': ["due to loss of fluid.", "If dehydration becomes worse due to diarrhoea, it may be fatal.", "So it is needed to consume more water and consult a doctor immediately."]
        }
        self.halt()

    @Rule(Fact(query_topic='disease_preventive_measures'))
    def rule_disease_preventive_measures(self):
        """Actions taken to avoid contracting diseases, which include ensuring water safety, maintaining food hygiene, preventing vector access to food, proper sanitation, and personal hygiene."""
        self.response = {
            'concept': 'Disease Preventive Measures',
            'explanation': """Actions taken to avoid contracting diseases, which include ensuring water safety, maintaining food hygiene, preventing vector access to food, proper sanitation, and personal hygiene.""",
            'topic': 'Biology',
            'subtopic': 'Health and Diseases',
            'examples': ["Consumption of boiled drinking water", "Removal of breeding places of flies and cover the food to prevent entering of flies to food", "Proper washing of hands with soap after using the toilet"]
        }
        self.halt()

    @Rule(Fact(query_topic='respiration'))
    def rule_respiration(self):
        """A fundamental biological process involving gas exchange. In humans, it is a complex process that occurs in three main stages: gas exchange between the external environment and lungs, gas exchange in alveoli, and cellular respiration."""
        self.response = {
            'concept': 'Respiration',
            'explanation': """A fundamental biological process involving gas exchange. In humans, it is a complex process that occurs in three main stages: gas exchange between the external environment and lungs, gas exchange in alveoli, and cellular respiration.""",
            'topic': 'Biology',
            'subtopic': 'Human Physiology',
            'examples': ["Gas exchange can be observed in some animals externally.", "Gas exchange between external environment and lungs", "Cellular respiration"]
        }
        self.halt()

    @Rule(Fact(query_topic='external_gas_exchange__human_respiration_'))
    def rule_external_gas_exchange__human_respiration_(self):
        """The initial stage of human respiration involving the intake of oxygen into the lungs and the removal of gaseous waste. This process is driven by changes in the volume of the lungs, similar to how air moves in and out of balloons in a bell jar model."""
        self.response = {
            'concept': 'External Gas Exchange (Human Respiration)',
            'explanation': """The initial stage of human respiration involving the intake of oxygen into the lungs and the removal of gaseous waste. This process is driven by changes in the volume of the lungs, similar to how air moves in and out of balloons in a bell jar model.""",
            'topic': 'Biology',
            'subtopic': 'Human Physiology',
            'examples': ["Intake of oxygen into lungs and removal of gaseous waste in cells occurs in external gas exchange.", "When rubber membrane is pulled down... external gas enters and balloons get inflated.", "When rubber sheath is released, gas inside balloons go out as the volume of bell jar decreases."]
        }
        self.halt()

    @Rule(Fact(query_topic='human_respiratory_system'))
    def rule_human_respiratory_system(self):
        """The biological system responsible for facilitating the entry of oxygen into the lungs and the expulsion of gaseous waste products generated during the body's biological processes."""
        self.response = {
            'concept': 'Human Respiratory System',
            'explanation': """The biological system responsible for facilitating the entry of oxygen into the lungs and the expulsion of gaseous waste products generated during the body's biological processes.""",
            'topic': 'Biology',
            'subtopic': 'Human Physiology',
            'examples': ["The system involved in entering O2 into lungs.", "release of gaseous waste products produced during biological processes.", "Nasal cavity"]
        }
        self.halt()

    @Rule(Fact(query_topic='main_parts_of_the_respiratory_system'))
    def rule_main_parts_of_the_respiratory_system(self):
        """The human respiratory system is comprised of several principal organs, including the nasal cavity, pharynx, larynx, trachea, bronchi, bronchioles, and alveoli, which facilitate the process of breathing."""
        self.response = {
            'concept': 'Main Parts of the Respiratory System',
            'explanation': """The human respiratory system is comprised of several principal organs, including the nasal cavity, pharynx, larynx, trachea, bronchi, bronchioles, and alveoli, which facilitate the process of breathing.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiratory System Anatomy',
            'examples': ["Nasal cavity", "Trachea", "Bronchi"]
        }
        self.halt()

    @Rule(Fact(query_topic='nasal_cavity_function_and_characteristics'))
    def rule_nasal_cavity_function_and_characteristics(self):
        """The nasal cavity's internal surface is covered with a moist mucus lining and numerous cilia. This structure is responsible for moisturizing/humidifying and warming inhaled air to body temperature, as well as trapping and removing foreign matter like bacteria, dust, and other wastes before they reach the lungs. Trapped materials are either expelled by ciliary movement or removed with saliva."""
        self.response = {
            'concept': 'Nasal Cavity Function and Characteristics',
            'explanation': """The nasal cavity's internal surface is covered with a moist mucus lining and numerous cilia. This structure is responsible for moisturizing/humidifying and warming inhaled air to body temperature, as well as trapping and removing foreign matter like bacteria, dust, and other wastes before they reach the lungs. Trapped materials are either expelled by ciliary movement or removed with saliva.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiratory System Physiology',
            'examples': ["Moisturizing inhaled air", "Warming inhaled air to body temperature", "Filtering dust and bacteria from inhaled air"]
        }
        self.halt()

    @Rule(Fact(query_topic='thoracic_cavity_structure_and_protection'))
    def rule_thoracic_cavity_structure_and_protection(self):
        """The thoracic cavity houses the lungs and is protected by the ribs, which contain inter-costal muscles. The lower boundary of the thoracic cavity is formed by the diaphragm."""
        self.response = {
            'concept': 'Thoracic Cavity Structure and Protection',
            'explanation': """The thoracic cavity houses the lungs and is protected by the ribs, which contain inter-costal muscles. The lower boundary of the thoracic cavity is formed by the diaphragm.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiratory System Anatomy',
            'examples': ["Lungs are located in the thoracic cavity", "Ribs protect the thoracic cavity", "Diaphragm forms the base of the thoracic cavity"]
        }
        self.halt()

    @Rule(Fact(query_topic='inspiration__inhalation__mechanism'))
    def rule_inspiration__inhalation__mechanism(self):
        """During inspiration, air enters the lungs due to an increase in lung volume, which is achieved by increasing the volume of the thoracic cavity. This process involves the contraction of inter-costal muscles, causing the ribs to move up and the sternum to move forward. Simultaneously, the diaphragm contracts and flattens (reduces its curvature). These combined actions enlarge the thoracic cavity, leading to increased lung volume and air intake through the nose."""
        self.response = {
            'concept': 'Inspiration (Inhalation) Mechanism',
            'explanation': """During inspiration, air enters the lungs due to an increase in lung volume, which is achieved by increasing the volume of the thoracic cavity. This process involves the contraction of inter-costal muscles, causing the ribs to move up and the sternum to move forward. Simultaneously, the diaphragm contracts and flattens (reduces its curvature). These combined actions enlarge the thoracic cavity, leading to increased lung volume and air intake through the nose.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiratory System Physiology',
            'examples': ["Inter-costal muscles contract", "Diaphragm contracts and flattens", "Ribs move up and sternum moves forward"]
        }
        self.halt()

    @Rule(Fact(query_topic='expiration__exhalation__initial_mechanism'))
    def rule_expiration__exhalation__initial_mechanism(self):
        """For expiration to occur and air to leave the lungs, the volume of the lungs must decrease. This is achieved by reducing the volume of the thoracic cavity."""
        self.response = {
            'concept': 'Expiration (Exhalation) Initial Mechanism',
            'explanation': """For expiration to occur and air to leave the lungs, the volume of the lungs must decrease. This is achieved by reducing the volume of the thoracic cavity.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiratory System Physiology',
            'examples': ["Decreased thoracic cavity volume", "Reduction in lung volume", "Air leaves the lungs"]
        }
        self.halt()

    @Rule(Fact(query_topic='expiration_mechanism'))
    def rule_expiration_mechanism(self):
        """During expiration, the intercostal muscles relax, causing the sternum and ribs to move back to their original position. Concurrently, the diaphragm relaxes and becomes curved. These actions decrease the volume of the lungs, which forces gas inside the lungs to move out through the trachea and then the nasal cavity."""
        self.response = {
            'concept': 'Expiration Mechanism',
            'explanation': """During expiration, the intercostal muscles relax, causing the sternum and ribs to move back to their original position. Concurrently, the diaphragm relaxes and becomes curved. These actions decrease the volume of the lungs, which forces gas inside the lungs to move out through the trachea and then the nasal cavity.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiration',
            'examples': ["Intercostal muscles relax", "Diaphragm relaxes and curves upwards", "Lung volume decreases, forcing air out"]
        }
        self.halt()

    @Rule(Fact(query_topic='gas_exchange_in_alveoli'))
    def rule_gas_exchange_in_alveoli(self):
        """The inhaled air reaches the alveoli. Oxygen concentration is greater in the alveoli than in the surrounding blood capillaries, causing O2 to diffuse into the blood capillaries. Similarly, carbon dioxide and water vapour concentrations are greater in the blood capillaries than in the alveoli, causing them to diffuse into the alveoli to be exhaled."""
        self.response = {
            'concept': 'Gas Exchange in Alveoli',
            'explanation': """The inhaled air reaches the alveoli. Oxygen concentration is greater in the alveoli than in the surrounding blood capillaries, causing O2 to diffuse into the blood capillaries. Similarly, carbon dioxide and water vapour concentrations are greater in the blood capillaries than in the alveoli, causing them to diffuse into the alveoli to be exhaled.""",
            'topic': 'Biology',
            'subtopic': 'Human Respiration / Gas Exchange',
            'examples': ["Oxygen diffuses from alveoli to blood", "Carbon dioxide diffuses from blood to alveoli", "Water vapour diffuses from blood to alveoli"]
        }
        self.halt()

    @Rule(Fact(query_topic='pathway_of_inhaled_air_to_alveoli'))
    def rule_pathway_of_inhaled_air_to_alveoli(self):
        """The inhaled air travels through a specific sequence of structures to reach the alveoli. This pathway includes the nasal cavity, trachea, bronchi, and bronchioles, before finally reaching the alveoli."""
        self.response = {
            'concept': 'Pathway of Inhaled Air to Alveoli',
            'explanation': """The inhaled air travels through a specific sequence of structures to reach the alveoli. This pathway includes the nasal cavity, trachea, bronchi, and bronchioles, before finally reaching the alveoli.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Anatomy',
            'examples': ["Air enters via nasal cavity", "Air passes through trachea and bronchi", "Air reaches alveoli via bronchioles"]
        }
        self.halt()

    @Rule(Fact(query_topic='respiratory_surface_definition_and_location'))
    def rule_respiratory_surface_definition_and_location(self):
        """A respiratory surface is the specific place where gas exchange between the external environment and blood takes place. In humans, the wall of the alveoli serves as the respiratory surface, and the exchange of gases occurs by the process of diffusion."""
        self.response = {
            'concept': 'Respiratory Surface Definition and Location',
            'explanation': """A respiratory surface is the specific place where gas exchange between the external environment and blood takes place. In humans, the wall of the alveoli serves as the respiratory surface, and the exchange of gases occurs by the process of diffusion.""",
            'topic': 'Biology',
            'subtopic': 'Respiration',
            'examples': ["The wall of alveoli in humans", "Gas exchange happens by diffusion", "Interface for gas exchange between environment and blood"]
        }
        self.halt()

    @Rule(Fact(query_topic='characteristics_of_an_efficient_respiratory_surface'))
    def rule_characteristics_of_an_efficient_respiratory_surface(self):
        """For efficient gas exchange, a respiratory surface must have specific adaptations: it should be moistened and permeable, thin for rapid diffusion, possess a large surface area to exchange large volumes of gas, and be highly vascularized (richly supplied with blood vessels)."""
        self.response = {
            'concept': 'Characteristics of an Efficient Respiratory Surface',
            'explanation': """For efficient gas exchange, a respiratory surface must have specific adaptations: it should be moistened and permeable, thin for rapid diffusion, possess a large surface area to exchange large volumes of gas, and be highly vascularized (richly supplied with blood vessels).""",
            'topic': 'Biology',
            'subtopic': 'Respiration / Adaptations',
            'examples': ["Surface should be moistened and permeable", "Surface should be thin for diffusion", "Surface should have a large area and be highly vascularized"]
        }
        self.halt()

    @Rule(Fact(query_topic='cellular_respiration'))
    def rule_cellular_respiration(self):
        """Cellular respiration is the process of oxidation of simple foods (like glucose) to produce energy for biological activities within living cells. Oxygen moves through alveoli and reacts with simple organic compounds in cells, releasing energy."""
        self.response = {
            'concept': 'Cellular Respiration',
            'explanation': """Cellular respiration is the process of oxidation of simple foods (like glucose) to produce energy for biological activities within living cells. Oxygen moves through alveoli and reacts with simple organic compounds in cells, releasing energy.""",
            'topic': 'Biology',
            'subtopic': 'Respiration',
            'examples': ["Glucose + Oxygen → Carbon dioxide + Water + Energy", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy", "Production of energy for biological activities in cells."]
        }
        self.halt()

    @Rule(Fact(query_topic='aerobic_respiration'))
    def rule_aerobic_respiration(self):
        """Aerobic respiration is a type of cellular respiration that takes place inside cells in the presence of oxygen."""
        self.response = {
            'concept': 'Aerobic Respiration',
            'explanation': """Aerobic respiration is a type of cellular respiration that takes place inside cells in the presence of oxygen.""",
            'topic': 'Biology',
            'subtopic': 'Types of Respiration',
            'examples': ["Respiration in cells when oxygen is available.", "The process described by Glucose + Oxygen → Carbon dioxide + Water + Energy.", "The chemical equation C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy."]
        }
        self.halt()

    @Rule(Fact(query_topic='anaerobic_respiration'))
    def rule_anaerobic_respiration(self):
        """Anaerobic respiration is a type of cellular respiration carried out by organisms without the presence of oxygen."""
        self.response = {
            'concept': 'Anaerobic Respiration',
            'explanation': """Anaerobic respiration is a type of cellular respiration carried out by organisms without the presence of oxygen.""",
            'topic': 'Biology',
            'subtopic': 'Types of Respiration',
            'examples': ["Respiration in organisms that can function without O₂.", "Alcohol fermentation in plants and yeast.", "Lactic acid fermentation in animal cells."]
        }
        self.halt()

    @Rule(Fact(query_topic='alcohol_fermentation'))
    def rule_alcohol_fermentation(self):
        """Alcohol fermentation is a type of anaerobic respiration that occurs in plants and yeast cells, producing carbon dioxide, ethyl alcohol, and energy."""
        self.response = {
            'concept': 'Alcohol Fermentation',
            'explanation': """Alcohol fermentation is a type of anaerobic respiration that occurs in plants and yeast cells, producing carbon dioxide, ethyl alcohol, and energy.""",
            'topic': 'Biology',
            'subtopic': 'Anaerobic Respiration / Fermentation',
            'examples': ["Glucose → Carbon dioxide + Ethyl alcohol + Energy", "Yeast carrying out anaerobic respiration.", "Production of CO₂ and Ethyl alcohol during fermentation."]
        }
        self.halt()

    @Rule(Fact(query_topic='lactic_acid_fermentation'))
    def rule_lactic_acid_fermentation(self):
        """Lactic acid fermentation is a type of anaerobic respiration that takes place within animal cells (including human cells), producing lactic acid and energy."""
        self.response = {
            'concept': 'Lactic Acid Fermentation',
            'explanation': """Lactic acid fermentation is a type of anaerobic respiration that takes place within animal cells (including human cells), producing lactic acid and energy.""",
            'topic': 'Biology',
            'subtopic': 'Anaerobic Respiration / Fermentation',
            'examples': ["Glucose → Lactic acid + Energy", "Muscle pain and cramps after an instant activity like a 100m race.", "Accumulation of lactic acid in muscles due to anaerobic respiration."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_production_in_respiration__aerobic_vs__anaerobic_'))
    def rule_energy_production_in_respiration__aerobic_vs__anaerobic_(self):
        """Aerobic respiration produces a higher amount of energy compared to anaerobic respiration. This difference arises because aerobic respiration involves the complete breakdown of glucose, while anaerobic respiration results in an incomplete breakdown. Part of the produced energy is lost as heat, and the remainder is stored as chemical energy in ATP."""
        self.response = {
            'concept': 'Energy Production in Respiration (Aerobic vs. Anaerobic)',
            'explanation': """Aerobic respiration produces a higher amount of energy compared to anaerobic respiration. This difference arises because aerobic respiration involves the complete breakdown of glucose, while anaerobic respiration results in an incomplete breakdown. Part of the produced energy is lost as heat, and the remainder is stored as chemical energy in ATP.""",
            'topic': 'Biology',
            'subtopic': 'Respiration and Energy Metabolism',
            'examples': ["Aerobic respiration: complete glucose breakdown, high energy yield", "Anaerobic respiration: incomplete glucose breakdown, lower energy yield", "Energy stored in ATP or lost as heat"]
        }
        self.halt()

    @Rule(Fact(query_topic='atp__adenosine_tri___phosphate_'))
    def rule_atp__adenosine_tri___phosphate_(self):
        """ATP (Adenosine Tri - Phosphate) is a crucial molecule that functions as the primary energy currency of the cell. It is responsible for storing energy produced during respiration and subsequently releasing this stored energy when needed for various biological processes within organisms."""
        self.response = {
            'concept': 'ATP (Adenosine Tri - Phosphate)',
            'explanation': """ATP (Adenosine Tri - Phosphate) is a crucial molecule that functions as the primary energy currency of the cell. It is responsible for storing energy produced during respiration and subsequently releasing this stored energy when needed for various biological processes within organisms.""",
            'topic': 'Biology',
            'subtopic': 'Cellular Energy and Metabolism',
            'examples': ["Storage of energy", "Release of energy", "Act as an energy carrier"]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_energy_stored_in_atp'))
    def rule_uses_of_energy_stored_in_atp(self):
        """The chemical energy stored within ATP molecules powers a diverse range of biological activities essential for life. These requirements include muscle contraction, active transport of substances across cell membranes, driving various chemical reactions, and the synthesis of complex compounds from simpler ones."""
        self.response = {
            'concept': 'Uses of Energy Stored in ATP',
            'explanation': """The chemical energy stored within ATP molecules powers a diverse range of biological activities essential for life. These requirements include muscle contraction, active transport of substances across cell membranes, driving various chemical reactions, and the synthesis of complex compounds from simpler ones.""",
            'topic': 'Biology',
            'subtopic': 'Biological Processes Requiring Energy',
            'examples': ["Movement of muscles", "Active transportation", "Synthesis of complex compounds (e.g., Amino acids to Proteins)"]
        }
        self.halt()

    @Rule(Fact(query_topic='common_cold'))
    def rule_common_cold(self):
        """The common cold is a viral infection primarily affecting the respiratory system. It is characterized by symptoms such as headache, sneezing, running nose, and cough. As it is a viral infection, there is no specific medical treatment, but symptoms can be managed, and recovery is aided by avoiding conditions like dust and mist."""
        self.response = {
            'concept': 'Common Cold',
            'explanation': """The common cold is a viral infection primarily affecting the respiratory system. It is characterized by symptoms such as headache, sneezing, running nose, and cough. As it is a viral infection, there is no specific medical treatment, but symptoms can be managed, and recovery is aided by avoiding conditions like dust and mist.""",
            'topic': 'Biology',
            'subtopic': 'Diseases of the Respiratory System',
            'examples': ["Causative agent is a virus", "Symptoms: Headache, sneezing, running nose", "No medical treatment for the virus, treat symptoms"]
        }
        self.halt()

    @Rule(Fact(query_topic='pneumonia'))
    def rule_pneumonia(self):
        """Pneumonia is an infection that affects the lungs, often caused by bacteria or viruses. This condition can lead to the accumulation of fluid in the lungs and is frequently associated with prolonged cold and cough. Immediate medical treatment is crucial for recovery."""
        self.response = {
            'concept': 'Pneumonia',
            'explanation': """Pneumonia is an infection that affects the lungs, often caused by bacteria or viruses. This condition can lead to the accumulation of fluid in the lungs and is frequently associated with prolonged cold and cough. Immediate medical treatment is crucial for recovery.""",
            'topic': 'Biology',
            'subtopic': 'Diseases of the Respiratory System',
            'examples': ["Causative agent: Bacteria or virus", "Lungs are infected; fluid may accumulate", "Requires immediate medical treatment"]
        }
        self.halt()

    @Rule(Fact(query_topic='asthma'))
    def rule_asthma(self):
        """Asthma is an inflammatory condition affecting the bronchioles within the respiratory system. It can be triggered by various causative agents such as dust, pollen, fur, or smoke. The inflammation reduces the cross-sectional area of the bronchioles, leading to difficulty in breathing, often accompanied by a characteristic sound."""
        self.response = {
            'concept': 'Asthma',
            'explanation': """Asthma is an inflammatory condition affecting the bronchioles within the respiratory system. It can be triggered by various causative agents such as dust, pollen, fur, or smoke. The inflammation reduces the cross-sectional area of the bronchioles, leading to difficulty in breathing, often accompanied by a characteristic sound.""",
            'topic': 'Biology',
            'subtopic': 'Diseases of the Respiratory System',
            'examples': ["Inflammation of bronchioles", "Causative agents: Dust, pollen, smoke", "Reduced bronchiolar cross-area causing breathing difficulty"]
        }
        self.halt()

    @Rule(Fact(query_topic='bronchitis_or_bronchiolar_inflammation'))
    def rule_bronchitis_or_bronchiolar_inflammation(self):
        """Bronchitis, also known as bronchiolar inflammation, is a condition characterized by the swelling of the bronchioles. This swelling can lead to various respiratory symptoms, often causing discomfort and difficulty in breathing."""
        self.response = {
            'concept': 'Bronchitis or Bronchiolar Inflammation',
            'explanation': """Bronchitis, also known as bronchiolar inflammation, is a condition characterized by the swelling of the bronchioles. This swelling can lead to various respiratory symptoms, often causing discomfort and difficulty in breathing.""",
            'topic': 'Biology',
            'subtopic': 'Diseases of the Respiratory System',
            'examples': ["Bronchioles swell up", "Inflammation in the bronchioles", "Can cause breathing difficulties"]
        }
        self.halt()

    @Rule(Fact(query_topic='respiratory_tract_inflammation__viral_bacterial_'))
    def rule_respiratory_tract_inflammation__viral_bacterial_(self):
        """This refers to inflammations within the respiratory tract that are caused by viral or bacterial infections. Common symptoms include a heavy cough and difficulty in breathing. Beyond the bronchioles, the larynx may also become infected, potentially leading to issues with proper voice production."""
        self.response = {
            'concept': 'Respiratory Tract Inflammation (Viral/Bacterial)',
            'explanation': """This refers to inflammations within the respiratory tract that are caused by viral or bacterial infections. Common symptoms include a heavy cough and difficulty in breathing. Beyond the bronchioles, the larynx may also become infected, potentially leading to issues with proper voice production.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Diseases',
            'examples': ["A person suffering from a persistent cough and wheezing after a viral infection.", "An individual experiencing hoarseness and difficulty speaking due to a bacterial infection of the larynx.", "Swelling and inflammation in the bronchioles making breathing difficult during a common cold."]
        }
        self.halt()

    @Rule(Fact(query_topic='tuberculosis'))
    def rule_tuberculosis(self):
        """Tuberculosis (TB) is an infectious disease caused by a specific bacterium. The primary site of infection is the lungs, where the multiplication of bacteria damages tissues, leading to deterioration and perforation. Although primarily affecting the lungs, TB can also impact other body parts. Damage to blood vessels can result in blood being released with phlegm during coughing. Key symptoms include tiredness, loss of appetite, weight loss, release of blood during coughing, and fever. Precautions and vaccines are important for prevention, and the disease is curable with proper treatment."""
        self.response = {
            'concept': 'Tuberculosis',
            'explanation': """Tuberculosis (TB) is an infectious disease caused by a specific bacterium. The primary site of infection is the lungs, where the multiplication of bacteria damages tissues, leading to deterioration and perforation. Although primarily affecting the lungs, TB can also impact other body parts. Damage to blood vessels can result in blood being released with phlegm during coughing. Key symptoms include tiredness, loss of appetite, weight loss, release of blood during coughing, and fever. Precautions and vaccines are important for prevention, and the disease is curable with proper treatment.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Diseases',
            'examples': ["A patient presenting with a chronic cough and bloody phlegm.", "An individual experiencing significant weight loss, fever, and night sweats.", "Lungs showing signs of perforation and tissue damage in a diagnosed TB case."]
        }
        self.halt()

    @Rule(Fact(query_topic='diseases_associated_with_smoking'))
    def rule_diseases_associated_with_smoking(self):
        """Smoking is a significant cause of various severe diseases, including lung cancer and bronchitis, and can sometimes lead to death. The harmful effects are attributed to compounds like carbon monoxide (CO) and nicotine, and the destruction of respiratory tract structures. Carbon monoxide in cigarette smoke readily binds with haemoglobin, reducing the blood's capacity to carry oxygen. Nicotine temporarily increases heart rate. The destruction of cilia in the respiratory tract can cause bronchioles to swell and become inflamed, leading to difficulty in breathing. Furthermore, exposure of epithelial cells to cigarette smoke can cause them to form abnormal cells that may develop into cancers. Passive smokers also suffer from these harmful effects."""
        self.response = {
            'concept': 'Diseases Associated with Smoking',
            'explanation': """Smoking is a significant cause of various severe diseases, including lung cancer and bronchitis, and can sometimes lead to death. The harmful effects are attributed to compounds like carbon monoxide (CO) and nicotine, and the destruction of respiratory tract structures. Carbon monoxide in cigarette smoke readily binds with haemoglobin, reducing the blood's capacity to carry oxygen. Nicotine temporarily increases heart rate. The destruction of cilia in the respiratory tract can cause bronchioles to swell and become inflamed, leading to difficulty in breathing. Furthermore, exposure of epithelial cells to cigarette smoke can cause them to form abnormal cells that may develop into cancers. Passive smokers also suffer from these harmful effects.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Diseases',
            'examples': ["A long-term smoker developing chronic bronchitis with persistent coughing.", "A person experiencing reduced oxygen transport in their blood due to carbon monoxide binding with haemoglobin.", "A passive smoker developing respiratory issues similar to active smokers due to secondhand smoke exposure."]
        }
        self.halt()

    @Rule(Fact(query_topic='silicosis'))
    def rule_silicosis(self):
        """Silicosis is a lung disease that occurs in individuals exposed to silicon-containing compounds, typically workers in industries such as quarries, coal mines, and glass manufacturing. When these workers inhale air containing these compounds, the particles accumulate in the alveoli. This accumulation leads to the gradual deterioration of lung tissues over time."""
        self.response = {
            'concept': 'Silicosis',
            'explanation': """Silicosis is a lung disease that occurs in individuals exposed to silicon-containing compounds, typically workers in industries such as quarries, coal mines, and glass manufacturing. When these workers inhale air containing these compounds, the particles accumulate in the alveoli. This accumulation leads to the gradual deterioration of lung tissues over time.""",
            'topic': 'Biology',
            'subtopic': 'Occupational Lung Diseases',
            'examples': ["A quarry worker developing shortness of breath and a dry cough after years of exposure to silica dust.", "A coal miner's lung tissues showing signs of gradual deterioration on an X-ray.", "Workers in the glass industry being advised on protective measures to prevent inhalation of silicon compounds."]
        }
        self.halt()

    @Rule(Fact(query_topic='asbestosis'))
    def rule_asbestosis(self):
        """Asbestosis is a severe respiratory disorder caused by the inhalation of air containing asbestos particles and fibres. The accumulation of these harmful fibres within the respiratory tract leads to the destruction of lung tissues."""
        self.response = {
            'concept': 'Asbestosis',
            'explanation': """Asbestosis is a severe respiratory disorder caused by the inhalation of air containing asbestos particles and fibres. The accumulation of these harmful fibres within the respiratory tract leads to the destruction of lung tissues.""",
            'topic': 'Biology',
            'subtopic': 'Occupational Lung Diseases',
            'examples': ["An individual who worked in construction years ago developing severe lung scarring due to asbestos exposure.", "A patient with a history of shipbuilding work presenting with progressively worsening breathing difficulties.", "Destruction of respiratory tract tissues observed in a person with prolonged inhalation of asbestos fibres."]
        }
        self.halt()

    @Rule(Fact(query_topic='metabolism'))
    def rule_metabolism(self):
        """The summation of biochemical reactions that take place in the living body."""
        self.response = {
            'concept': 'Metabolism',
            'explanation': """The summation of biochemical reactions that take place in the living body.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["Production of carbon dioxide, water, and energy during cellular respiration.", "Production of urea, uric acid in protein catabolism in liver."]
        }
        self.halt()

    @Rule(Fact(query_topic='excretory_materials'))
    def rule_excretory_materials(self):
        """Waste products that are produced during metabolic processes in the cells and should be removed from the body."""
        self.response = {
            'concept': 'Excretory Materials',
            'explanation': """Waste products that are produced during metabolic processes in the cells and should be removed from the body.""",
            'topic': 'Biology',
            'subtopic': 'Excretion',
            'examples': ["CO2", "Water vapour", "Urea"]
        }
        self.halt()

    @Rule(Fact(query_topic='excretion'))
    def rule_excretion(self):
        """The removal of excretory products produced during metabolism from the body."""
        self.response = {
            'concept': 'Excretion',
            'explanation': """The removal of excretory products produced during metabolism from the body.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes / Excretion',
            'examples': ["Removal of CO2 and water vapour via lungs as exhaled air.", "Removal of urea, uric acid, salts, and water via kidneys as urine.", "Removal of urea, uric acid, NaCl, and water via skin as sweat."]
        }
        self.halt()

    @Rule(Fact(query_topic='faecal_matter__not_an_excretory_substance_'))
    def rule_faecal_matter__not_an_excretory_substance_(self):
        """Faeces is the undigested materials of the digestion process, which takes place within the digestive system and is not a biochemical reaction in cells. Thus, it is not considered an excretory material, though bile pigments within it are excretory."""
        self.response = {
            'concept': 'Faecal Matter (Not an Excretory Substance)',
            'explanation': """Faeces is the undigested materials of the digestion process, which takes place within the digestive system and is not a biochemical reaction in cells. Thus, it is not considered an excretory material, though bile pigments within it are excretory.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes / Excretion / Digestion',
            'examples': ["Undigested food.", "Indigestible fibers.", "Bile pigments (which are an excretory substance)."]
        }
        self.halt()

    @Rule(Fact(query_topic='urinary_system'))
    def rule_urinary_system(self):
        """A system composed of a pair of kidneys and other associated organs, primarily responsible for carrying out nitrogenous excretion."""
        self.response = {
            'concept': 'Urinary System',
            'explanation': """A system composed of a pair of kidneys and other associated organs, primarily responsible for carrying out nitrogenous excretion.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes / Excretion',
            'examples': ["Kidneys", "Ureters", "Urinary bladder"]
        }
        self.halt()

    @Rule(Fact(query_topic='urinary_system_process'))
    def rule_urinary_system_process(self):
        """The human urinary system processes waste materials from the blood. Waste enters the kidneys via renal arteries, where it is filtered to form urine. This urine is then transported through ureters, stored temporarily in the urinary bladder, and finally released from the body through the urethra."""
        self.response = {
            'concept': 'Urinary System Process',
            'explanation': """The human urinary system processes waste materials from the blood. Waste enters the kidneys via renal arteries, where it is filtered to form urine. This urine is then transported through ureters, stored temporarily in the urinary bladder, and finally released from the body through the urethra.""",
            'topic': 'Biology',
            'subtopic': 'Human Body Processes',
            'examples': ["Waste materials in blood enter through renal arteries.", "Urine is transported through ureters and stored in the urinary bladder.", "Urine is released out of the body through the urethra."]
        }
        self.halt()

    @Rule(Fact(query_topic='kidney_function'))
    def rule_kidney_function(self):
        """The kidney is an organ of the excretory system responsible for filtering waste materials from the blood and forming urine. It serves as the primary site for blood filtration and initial urine production."""
        self.response = {
            'concept': 'Kidney Function',
            'explanation': """The kidney is an organ of the excretory system responsible for filtering waste materials from the blood and forming urine. It serves as the primary site for blood filtration and initial urine production.""",
            'topic': 'Biology',
            'subtopic': 'Urinary System',
            'examples': ["Waste materials in blood are filtered inside the kidney.", "The filtrate known as urine is formed inside the kidney.", "Kidneys are part of the overall waste management system."]
        }
        self.halt()

    @Rule(Fact(query_topic='internal_structure_of_a_kidney'))
    def rule_internal_structure_of_a_kidney(self):
        """The internal structure of a kidney includes several distinct parts. Externally, it is covered by a Capsule. Major internal regions include the Cortex and Medulla (containing Pyramids). Blood supply involves the Renal artery and Renal vein, while urine collects in the Pelvis before exiting via the Ureter. Nephrons are the functional units within these regions."""
        self.response = {
            'concept': 'Internal Structure of a Kidney',
            'explanation': """The internal structure of a kidney includes several distinct parts. Externally, it is covered by a Capsule. Major internal regions include the Cortex and Medulla (containing Pyramids). Blood supply involves the Renal artery and Renal vein, while urine collects in the Pelvis before exiting via the Ureter. Nephrons are the functional units within these regions.""",
            'topic': 'Biology',
            'subtopic': 'Kidney Anatomy',
            'examples': ["The kidney includes a Capsule, Cortex, Pyramids, and Medulla.", "The Renal artery brings blood to the kidney, and the Renal vein carries it away.", "The Pelvis collects urine before it flows into the Ureter."]
        }
        self.halt()

    @Rule(Fact(query_topic='nephron'))
    def rule_nephron(self):
        """The nephron is the microscopic structural and functional unit of the kidney. Each kidney contains approximately one million nephrons, which are solely responsible for the filtration of blood and the intricate process of urine formation."""
        self.response = {
            'concept': 'Nephron',
            'explanation': """The nephron is the microscopic structural and functional unit of the kidney. Each kidney contains approximately one million nephrons, which are solely responsible for the filtration of blood and the intricate process of urine formation.""",
            'topic': 'Biology',
            'subtopic': 'Kidney Structure',
            'examples': ["The structural and functional unit of kidney is nephron.", "Nephron is microscopic.", "There are about one million nephrons in a kidney."]
        }
        self.halt()

    @Rule(Fact(query_topic='structure_of_a_nephron'))
    def rule_structure_of_a_nephron(self):
        """A nephron is a complex microscopic tubule with distinct parts crucial for its function. Key components include the Glomerulus, Bowman's capsule, Proximal convoluted tubules, the Loop of Henle (comprising descending and ascending limbs), Distal convoluted tubules, and a Collecting duct. Blood capillaries are intricately associated with these structures."""
        self.response = {
            'concept': 'Structure of a Nephron',
            'explanation': """A nephron is a complex microscopic tubule with distinct parts crucial for its function. Key components include the Glomerulus, Bowman's capsule, Proximal convoluted tubules, the Loop of Henle (comprising descending and ascending limbs), Distal convoluted tubules, and a Collecting duct. Blood capillaries are intricately associated with these structures.""",
            'topic': 'Biology',
            'subtopic': 'Nephron Anatomy',
            'examples': ["A nephron includes a Glomerulus and Bowman's capsule.", "The Loop of Henle has distinct descending and ascending limbs.", "Distal convoluted tubules lead to a Collecting duct."]
        }
        self.halt()

    @Rule(Fact(query_topic='process_of_urine_formation'))
    def rule_process_of_urine_formation(self):
        """Urine formation in the kidney is a multi-step process involving three main physiological stages: Ultrafiltration, where blood plasma is filtered; Selective reabsorption, where essential substances are reabsorbed back into the blood; and Secretion, where additional waste products are actively transported into the filtrate."""
        self.response = {
            'concept': 'Process of Urine Formation',
            'explanation': """Urine formation in the kidney is a multi-step process involving three main physiological stages: Ultrafiltration, where blood plasma is filtered; Selective reabsorption, where essential substances are reabsorbed back into the blood; and Secretion, where additional waste products are actively transported into the filtrate.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["Urine formation in kidney follows three main processes.", "Ultrafiltration is the first step in urine formation.", "Selective reabsorption and Secretion are subsequent stages."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrafiltration'))
    def rule_ultrafiltration(self):
        """Ultrafiltration is the initial stage of urine formation, occurring at the renal corpuscle (Glomerulus and Bowman's capsule). Blood enters the glomerulus via the afferent arteriole, which branches into a dense capillary network. A high blood pressure is maintained within the glomerulus due to the efferent arteriole having a smaller diameter than the afferent arteriole, forcing plasma to filter through the glomerular and Bowman's capsule walls, forming glomerular filtrate."""
        self.response = {
            'concept': 'Ultrafiltration',
            'explanation': """Ultrafiltration is the initial stage of urine formation, occurring at the renal corpuscle (Glomerulus and Bowman's capsule). Blood enters the glomerulus via the afferent arteriole, which branches into a dense capillary network. A high blood pressure is maintained within the glomerulus due to the efferent arteriole having a smaller diameter than the afferent arteriole, forcing plasma to filter through the glomerular and Bowman's capsule walls, forming glomerular filtrate.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["Blood enters the glomerulus through the afferent arteriole.", "A dense network of capillaries in the glomerulus aids filtration.", "High blood pressure in the glomerulus forces filtration into Bowman's capsule."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrafiltration'))
    def rule_ultrafiltration(self):
        """This is the initial process of urine formation where glomerular filtrate is collected into the cavity of Bowman’s capsule. Large molecules like plasma proteins and blood cells are not filtered during this stage."""
        self.response = {
            'concept': 'Ultrafiltration',
            'explanation': """This is the initial process of urine formation where glomerular filtrate is collected into the cavity of Bowman’s capsule. Large molecules like plasma proteins and blood cells are not filtered during this stage.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["Glomerular filtrate collected into the cavity of Bowman’s capsule", "Large molecules like plasma proteins and blood cells are not filtered into the glomerular filtrate"]
        }
        self.halt()

    @Rule(Fact(query_topic='glomerular_filtrate'))
    def rule_glomerular_filtrate(self):
        """The filtered fluid that results from ultrafiltration, collected in Bowman's capsule. It is similar in composition to blood plasma but lacks large molecules such as plasma proteins and blood cells."""
        self.response = {
            'concept': 'Glomerular Filtrate',
            'explanation': """The filtered fluid that results from ultrafiltration, collected in Bowman's capsule. It is similar in composition to blood plasma but lacks large molecules such as plasma proteins and blood cells.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["Constituents include water, glucose, amino acids, vitamins, drugs, various ions, hormones and urea", "Is as same as blood plasma", "Does not contain large molecules like plasma proteins and blood cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='selective_reabsorption'))
    def rule_selective_reabsorption(self):
        """As the glomerular filtrate moves along the nephron, most of its useful constituents are absorbed back into the blood capillaries associated with the nephron, changing the filtrate's composition."""
        self.response = {
            'concept': 'Selective Reabsorption',
            'explanation': """As the glomerular filtrate moves along the nephron, most of its useful constituents are absorbed back into the blood capillaries associated with the nephron, changing the filtrate's composition.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["90% of the water, all glucose, amino acids and vitamins reabsorb into blood", "Part of salts, small amount of urea, uric acid and drugs reabsorb into blood", "The composition of glomerular filtrate changes with selective reabsorption"]
        }
        self.halt()

    @Rule(Fact(query_topic='glomerular_filtrate_volume_and_fate'))
    def rule_glomerular_filtrate_volume_and_fate(self):
        """In a healthy adult, about 120 cm³ of glomerular filtrate is formed per minute. However, 95% of this volume is reabsorbed along the nephron, with the remaining fluid released into collecting ducts and then to the pelvis."""
        self.response = {
            'concept': 'Glomerular Filtrate Volume and Fate',
            'explanation': """In a healthy adult, about 120 cm³ of glomerular filtrate is formed per minute. However, 95% of this volume is reabsorbed along the nephron, with the remaining fluid released into collecting ducts and then to the pelvis.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["About 120 cm3 of glomerular filtrate formed during one minute in a healthy adult", "95% of the glomerular filtrate reabsorbs when it moves along the nephron", "Remaining filtrate is released into collecting ducts and then to the pelvis"]
        }
        self.halt()

    @Rule(Fact(query_topic='glucose_reabsorption_in_health_and_diabetes'))
    def rule_glucose_reabsorption_in_health_and_diabetes(self):
        """In a healthy adult, 100% of glucose in the glomerular filtrate is reabsorbed. However, in diabetes patients, glucose is not totally reabsorbed, and the remaining glucose is released with urine."""
        self.response = {
            'concept': 'Glucose Reabsorption in Health and Diabetes',
            'explanation': """In a healthy adult, 100% of glucose in the glomerular filtrate is reabsorbed. However, in diabetes patients, glucose is not totally reabsorbed, and the remaining glucose is released with urine.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation / Pathology',
            'examples': ["100% of glucose is reabsorbed in a healthy adult", "In diabetes patients glucose is not totally reabsorbed", "Remaining glucose in diabetes patients is released with urine"]
        }
        self.halt()

    @Rule(Fact(query_topic='secretion'))
    def rule_secretion(self):
        """This process involves certain materials from the blood capillaries associated with the nephron entering the tubules of the nephron, further modifying the composition of the fluid that will become urine."""
        self.response = {
            'concept': 'Secretion',
            'explanation': """This process involves certain materials from the blood capillaries associated with the nephron entering the tubules of the nephron, further modifying the composition of the fluid that will become urine.""",
            'topic': 'Biology',
            'subtopic': 'Urine Formation',
            'examples': ["Hydrogen ions (H+)", "Potassium ions (K+), Ammonium ions (NH4+)", "Creatinine, drugs, Vitamin B"]
        }
        self.halt()

    @Rule(Fact(query_topic='urine_removal_pathway'))
    def rule_urine_removal_pathway(self):
        """After formation, urine released into the renal pelvis is transported along the ureters into the bladder, where it is temporarily stored before being released from the body."""
        self.response = {
            'concept': 'Urine Removal Pathway',
            'explanation': """After formation, urine released into the renal pelvis is transported along the ureters into the bladder, where it is temporarily stored before being released from the body.""",
            'topic': 'Biology',
            'subtopic': 'Urinary System Function',
            'examples': ["Urine released into the pelvis is transported along ureters", "Ureters transport urine into the bladder", "Urine is temporally stored in bladder"]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_of_urine_in_a_healthy_person'))
    def rule_composition_of_urine_in_a_healthy_person(self):
        """Urine in a healthy individual consists primarily of water (about 96%), with smaller percentages of salts (about 2%) and urea (about 2%). Trace amounts of uric acid and creatinine are also present."""
        self.response = {
            'concept': 'Composition of Urine in a Healthy Person',
            'explanation': """Urine in a healthy individual consists primarily of water (about 96%), with smaller percentages of salts (about 2%) and urea (about 2%). Trace amounts of uric acid and creatinine are also present.""",
            'topic': 'Biology',
            'subtopic': 'Human Body Processes / Urinary System',
            'examples': ["Water constitutes about 96% of healthy urine.", "Approximately 2% of urine is made up of salts.", "Trace amounts of creatinine are found in healthy urine."]
        }
        self.halt()

    @Rule(Fact(query_topic='renal_failure'))
    def rule_renal_failure(self):
        """Renal failure occurs when kidneys lose their ability to filter urine effectively due to weakening of the filtration process in nephrons. It can be caused by infections, heavy metals (like mercury, arsenic), certain medicines, and carbon tetrachloride. Key symptoms include oedema (swelling) and increased blood pressure due to water and salt accumulation, and a decrease in blood pH due to the buildup of urea and other excretory materials. If acute renal failure occurs (within 8-14 days without treatment), blood may need to be filtered by a machine in a process called dialysis. When both kidneys fail, a kidney transplant from a donor is required."""
        self.response = {
            'concept': 'Renal Failure',
            'explanation': """Renal failure occurs when kidneys lose their ability to filter urine effectively due to weakening of the filtration process in nephrons. It can be caused by infections, heavy metals (like mercury, arsenic), certain medicines, and carbon tetrachloride. Key symptoms include oedema (swelling) and increased blood pressure due to water and salt accumulation, and a decrease in blood pH due to the buildup of urea and other excretory materials. If acute renal failure occurs (within 8-14 days without treatment), blood may need to be filtered by a machine in a process called dialysis. When both kidneys fail, a kidney transplant from a donor is required.""",
            'topic': 'Biology',
            'subtopic': 'Diseases Associated with Urinary System',
            'examples': ["Mercury poisoning can lead to renal failure.", "A symptom of renal failure is oedema, causing swelling.", "Dialysis is used to filter blood when kidneys fail acutely."]
        }
        self.halt()

    @Rule(Fact(query_topic='nephritis'))
    def rule_nephritis(self):
        """Nephritis, or swelling of the kidney, is caused by infections and toxins, including infections in the ureters. This condition affects both the glomerulus and uriniferous tubules. Damage to the glomerulus reduces the volume of blood flow, which in turn decreases the amount of urine formed and leads to an accumulation of waste materials in the body. Furthermore, damage to the glomeruli can impair the filtering process, allowing red blood cells and essential proteins to pass into the glomerular filtrate."""
        self.response = {
            'concept': 'Nephritis',
            'explanation': """Nephritis, or swelling of the kidney, is caused by infections and toxins, including infections in the ureters. This condition affects both the glomerulus and uriniferous tubules. Damage to the glomerulus reduces the volume of blood flow, which in turn decreases the amount of urine formed and leads to an accumulation of waste materials in the body. Furthermore, damage to the glomeruli can impair the filtering process, allowing red blood cells and essential proteins to pass into the glomerular filtrate.""",
            'topic': 'Biology',
            'subtopic': 'Diseases Associated with Urinary System',
            'examples': ["Kidney infections are a common cause of nephritis.", "Nephritis can reduce the volume of urine produced.", "One consequence of nephritis can be finding red blood cells in urine."]
        }
        self.halt()

    @Rule(Fact(query_topic='calculi_in_kidney_and_bladder__kidney_stones_'))
    def rule_calculi_in_kidney_and_bladder__kidney_stones_(self):
        """This condition is caused by the crystallization of calcium oxalate in the kidney and bladder. When these stones obstruct the ureters, severe pain occurs. Treatment involves drugs, surgery, or Lithotripsy technology. Contributing factors include certain feeding habits and postponing urination. Prevention can be achieved by drinking an adequate volume of water daily."""
        self.response = {
            'concept': 'Calculi in Kidney and Bladder (Kidney Stones)',
            'explanation': """This condition is caused by the crystallization of calcium oxalate in the kidney and bladder. When these stones obstruct the ureters, severe pain occurs. Treatment involves drugs, surgery, or Lithotripsy technology. Contributing factors include certain feeding habits and postponing urination. Prevention can be achieved by drinking an adequate volume of water daily.""",
            'topic': 'Biology',
            'subtopic': 'Human Disorders',
            'examples': ["Crystallization of calcium oxalate", "Blockage of ureters causing severe pain", "Prevention by drinking required volume of water daily"]
        }
        self.halt()

    @Rule(Fact(query_topic='lithotripsy_technology'))
    def rule_lithotripsy_technology(self):
        """Lithotripsy is a medical technique used to crush calculi (stones) in the kidney and bladder. This is achieved by applying laser rays or ultrasound waves to break down the stones into smaller pieces, allowing them to be passed more easily."""
        self.response = {
            'concept': 'Lithotripsy Technology',
            'explanation': """Lithotripsy is a medical technique used to crush calculi (stones) in the kidney and bladder. This is achieved by applying laser rays or ultrasound waves to break down the stones into smaller pieces, allowing them to be passed more easily.""",
            'topic': 'Biology',
            'subtopic': 'Medical Technology',
            'examples': ["Crushing stones using laser rays", "Crushing stones using ultrasound waves", "A technique for removing kidney stones"]
        }
        self.halt()

    @Rule(Fact(query_topic='blood__function_and_basic_nature_'))
    def rule_blood__function_and_basic_nature_(self):
        """Blood is a special connective tissue that appears as a red-colored fluid. Its primary function is to serve as the transport medium for essential components like glucose and oxygen to the cells, and for waste products out of the cells. While appearing homogeneous, blood is composed of plasma and suspended corpuscles."""
        self.response = {
            'concept': 'Blood (Function and Basic Nature)',
            'explanation': """Blood is a special connective tissue that appears as a red-colored fluid. Its primary function is to serve as the transport medium for essential components like glucose and oxygen to the cells, and for waste products out of the cells. While appearing homogeneous, blood is composed of plasma and suspended corpuscles.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["Transports glucose to cells", "Transports oxygen to cells", "Removes waste out of cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_components__centrifugation_'))
    def rule_blood_components__centrifugation_(self):
        """When blood is centrifuged and allowed to settle, it separates into two distinct layers. The upper layer, making up approximately 55% of the blood volume, is the plasma (a pale yellow fluid). The lower, dark red layer, constituting about 45%, consists of blood corpuscles."""
        self.response = {
            'concept': 'Blood Components (Centrifugation)',
            'explanation': """When blood is centrifuged and allowed to settle, it separates into two distinct layers. The upper layer, making up approximately 55% of the blood volume, is the plasma (a pale yellow fluid). The lower, dark red layer, constituting about 45%, consists of blood corpuscles.""",
            'topic': 'Biology',
            'subtopic': 'Blood Composition',
            'examples': ["Plasma (55%, pale yellow fluid)", "Corpuscles (45%, dark red materials)", "Separation into two layers upon centrifugation"]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_blood_corpuscles'))
    def rule_types_of_blood_corpuscles(self):
        """Blood corpuscles, the solid components suspended in plasma, are categorized into several types: Red Blood Cells, White Blood Cells, and Platelets. White Blood Cells are further subdivided into Granulocytes (Neutrophils, Eosinophils, Basophils) and Non-granulocytes (Lymphocytes, Monocytes)."""
        self.response = {
            'concept': 'Types of Blood Corpuscles',
            'explanation': """Blood corpuscles, the solid components suspended in plasma, are categorized into several types: Red Blood Cells, White Blood Cells, and Platelets. White Blood Cells are further subdivided into Granulocytes (Neutrophils, Eosinophils, Basophils) and Non-granulocytes (Lymphocytes, Monocytes).""",
            'topic': 'Biology',
            'subtopic': 'Blood Composition',
            'examples': ["Red Blood Cells", "White Blood Cells (e.g., Lymphocytes, Neutrophils)", "Platelets"]
        }
        self.halt()

    @Rule(Fact(query_topic='red_blood_cells__erythrocytes_'))
    def rule_red_blood_cells__erythrocytes_(self):
        """Red Blood Cells, also known as Erythrocytes, are red-colored, biconcave disc-like cells found in human blood, with approximately five million present per cubic millimeter. They are formed in the red bone marrow, have a life span of about four months (120 days), and notably lack a nucleus."""
        self.response = {
            'concept': 'Red Blood Cells (Erythrocytes)',
            'explanation': """Red Blood Cells, also known as Erythrocytes, are red-colored, biconcave disc-like cells found in human blood, with approximately five million present per cubic millimeter. They are formed in the red bone marrow, have a life span of about four months (120 days), and notably lack a nucleus.""",
            'topic': 'Biology',
            'subtopic': 'Blood Cells',
            'examples': ["About five million per cubic millimeter of blood", "Biconcave disc shape", "Life span of 120 days"]
        }
        self.halt()

    @Rule(Fact(query_topic='haemoglobin'))
    def rule_haemoglobin(self):
        """A pigment present in red blood cells that binds with oxygen and forms oxyhaemoglobin to transport oxygen to cells."""
        self.response = {
            'concept': 'Haemoglobin',
            'explanation': """A pigment present in red blood cells that binds with oxygen and forms oxyhaemoglobin to transport oxygen to cells.""",
            'topic': 'Biology',
            'subtopic': 'Red Blood Cells Function',
            'examples': ["Haemoglobin absorbs more oxygen.", "Haemoglobin binds with oxygen to form oxyhaemoglobin.", "Haemoglobin transports oxygen to cells."]
        }
        self.halt()

    @Rule(Fact(query_topic='white_blood_cells__wbc____characteristics'))
    def rule_white_blood_cells__wbc____characteristics(self):
        """A type of corpuscle in blood, larger than red blood cells but smaller in number. They have nuclei, are colourless, and form in bone marrow. The ratio of red blood cells to white blood cells is 600:1."""
        self.response = {
            'concept': 'White Blood Cells (WBC) - Characteristics',
            'explanation': """A type of corpuscle in blood, larger than red blood cells but smaller in number. They have nuclei, are colourless, and form in bone marrow. The ratio of red blood cells to white blood cells is 600:1.""",
            'topic': 'Biology',
            'subtopic': 'Human Blood Components',
            'examples': ["WBC are larger than red blood cells.", "WBC have nuclei.", "The ratio of RBC to WBC is 600:1."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_wbc___granulocytes'))
    def rule_types_of_wbc___granulocytes(self):
        """One of the two main types of White Blood Cells (WBC) found in blood. Granulocytes are further divided into three specific types: Neutrophils, Eosinophils, and Basophils."""
        self.response = {
            'concept': 'Types of WBC - Granulocytes',
            'explanation': """One of the two main types of White Blood Cells (WBC) found in blood. Granulocytes are further divided into three specific types: Neutrophils, Eosinophils, and Basophils.""",
            'topic': 'Biology',
            'subtopic': 'White Blood Cell Classification',
            'examples': ["Neutrophils are a type of granulocyte.", "Eosinophils are granulocytes.", "Basophils are classified as granulocytes."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_wbc___non_granulocytes'))
    def rule_types_of_wbc___non_granulocytes(self):
        """One of the two main types of White Blood Cells (WBC) found in blood. Non-granulocytes are divided into two specific types: Lymphocytes and Monocytes."""
        self.response = {
            'concept': 'Types of WBC - Non-granulocytes',
            'explanation': """One of the two main types of White Blood Cells (WBC) found in blood. Non-granulocytes are divided into two specific types: Lymphocytes and Monocytes.""",
            'topic': 'Biology',
            'subtopic': 'White Blood Cell Classification',
            'examples': ["Lymphocytes are non-granulocytes.", "Monocytes are a type of non-granulocyte."]
        }
        self.halt()

    @Rule(Fact(query_topic='wbc_count_and_disease_diagnosis'))
    def rule_wbc_count_and_disease_diagnosis(self):
        """One cubic millimeter (1 mm³) of human blood contains 4,000 - 11,000 WBC. The percentages of WBC increase above normal levels in microbial infections, making WBC counts useful for diagnosing diseases."""
        self.response = {
            'concept': 'WBC Count and Disease Diagnosis',
            'explanation': """One cubic millimeter (1 mm³) of human blood contains 4,000 - 11,000 WBC. The percentages of WBC increase above normal levels in microbial infections, making WBC counts useful for diagnosing diseases.""",
            'topic': 'Biology',
            'subtopic': 'Clinical Significance of Blood',
            'examples': ["A healthy person has 4,000 - 11,000 WBC per mm³.", "Increased WBC percentages indicate microbial infections.", "Investigation of WBC counts helps diagnose diseases."]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_white_blood_cells__wbc_'))
    def rule_function_of_white_blood_cells__wbc_(self):
        """The function of WBC is to protect the body from infectious particles that enter it. This is achieved through phagocytosis and by producing antibodies."""
        self.response = {
            'concept': 'Function of White Blood Cells (WBC)',
            'explanation': """The function of WBC is to protect the body from infectious particles that enter it. This is achieved through phagocytosis and by producing antibodies.""",
            'topic': 'Biology',
            'subtopic': 'Immune System',
            'examples': ["WBC destroy infectious particles.", "WBC protect the body through phagocytosis.", "WBC produce antibodies to fight infections."]
        }
        self.halt()

    @Rule(Fact(query_topic='platelets'))
    def rule_platelets(self):
        """Fragments of cells in human blood that are not considered whole cells. These corpuscles lack nuclei, form in bone marrow, and have an approximate lifespan of 5-7 days. One cubic millimeter of blood contains 150,000-400,000 platelets. Their count can decrease due to diseases like Dengue and Leptospirosis."""
        self.response = {
            'concept': 'Platelets',
            'explanation': """Fragments of cells in human blood that are not considered whole cells. These corpuscles lack nuclei, form in bone marrow, and have an approximate lifespan of 5-7 days. One cubic millimeter of blood contains 150,000-400,000 platelets. Their count can decrease due to diseases like Dengue and Leptospirosis.""",
            'topic': 'Biology',
            'subtopic': 'Human Blood Components',
            'examples': ["Platelets are cell fragments without nuclei.", "Normal platelet count is 150,000-400,000 per mm³.", "Platelet count decreases in diseases like Dengue."]
        }
        self.halt()

    @Rule(Fact(query_topic='platelets_and_blood_coagulation'))
    def rule_platelets_and_blood_coagulation(self):
        """Platelets are components of blood that play a critical role in stopping bleeding by initiating blood coagulation. They achieve this by containing and releasing thromboplastin."""
        self.response = {
            'concept': 'Platelets and Blood Coagulation',
            'explanation': """Platelets are components of blood that play a critical role in stopping bleeding by initiating blood coagulation. They achieve this by containing and releasing thromboplastin.""",
            'topic': 'Biology',
            'subtopic': 'Blood Components',
            'examples': ["When a blood vessel is injured, platelets aggregate at the site.", "A reduction in platelet count can lead to excessive bleeding.", "Platelets are essential for the formation of a blood clot."]
        }
        self.halt()

    @Rule(Fact(query_topic='thromboplastin_function'))
    def rule_thromboplastin_function(self):
        """Thromboplastin is a substance found within platelets that is instrumental in the process of blood coagulation, acting as an enzyme to trigger the clotting cascade."""
        self.response = {
            'concept': 'Thromboplastin Function',
            'explanation': """Thromboplastin is a substance found within platelets that is instrumental in the process of blood coagulation, acting as an enzyme to trigger the clotting cascade.""",
            'topic': 'Biology',
            'subtopic': 'Blood Coagulation',
            'examples': ["Thromboplastin is released from damaged platelets to initiate clotting.", "The activation of thromboplastin is a key step in forming a fibrin clot.", "Deficiency in thromboplastin can result in impaired blood clotting."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__water_content'))
    def rule_blood_plasma_composition__water_content(self):
        """Blood plasma is primarily composed of water, which makes up approximately 92% of its total volume. Water serves as a solvent and transport medium for various substances."""
        self.response = {
            'concept': 'Blood Plasma Composition: Water Content',
            'explanation': """Blood plasma is primarily composed of water, which makes up approximately 92% of its total volume. Water serves as a solvent and transport medium for various substances.""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Water in plasma helps maintain blood volume and pressure.", "Nutrients and waste products are dissolved in the water of plasma.", "Proper hydration is crucial for maintaining the water content of blood plasma."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__proteins'))
    def rule_blood_plasma_composition__proteins(self):
        """After water, proteins are the second most abundant compounds in blood plasma. Key plasma proteins include Albumen, Globulin, and Fibrinogen, each having distinct physiological roles."""
        self.response = {
            'concept': 'Blood Plasma Composition: Proteins',
            'explanation': """After water, proteins are the second most abundant compounds in blood plasma. Key plasma proteins include Albumen, Globulin, and Fibrinogen, each having distinct physiological roles.""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Albumen helps maintain the osmotic pressure of blood.", "Globulins include antibodies, which are vital for the immune system.", "Fibrinogen is a precursor to fibrin, essential for blood clotting."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__nutrients'))
    def rule_blood_plasma_composition__nutrients(self):
        """Blood plasma transports various nutrients required by cells throughout the body. These include monosaccharides (e.g., glucose), amino acids, fatty acids, glycerol, and vitamins."""
        self.response = {
            'concept': 'Blood Plasma Composition: Nutrients',
            'explanation': """Blood plasma transports various nutrients required by cells throughout the body. These include monosaccharides (e.g., glucose), amino acids, fatty acids, glycerol, and vitamins.""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Glucose is carried to cells for cellular respiration.", "Amino acids are transported to tissues for protein synthesis.", "Vitamins absorbed from the digestive system reach target cells via plasma."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__ions'))
    def rule_blood_plasma_composition__ions(self):
        """Blood plasma contains a variety of essential mineral ions, such as Na+, K+, Ca2+, Mg2+, Cl-, PO4^3-, SO4^2-, and HCO3^-. These ions are critical for maintaining electrolyte balance and various bodily functions."""
        self.response = {
            'concept': 'Blood Plasma Composition: Ions',
            'explanation': """Blood plasma contains a variety of essential mineral ions, such as Na+, K+, Ca2+, Mg2+, Cl-, PO4^3-, SO4^2-, and HCO3^-. These ions are critical for maintaining electrolyte balance and various bodily functions.""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Sodium (Na+) and potassium (K+) ions are crucial for nerve impulse transmission.", "Calcium (Ca2+) ions are vital for blood clotting and muscle contraction.", "Bicarbonate (HCO3-) ions act as a buffer to regulate blood pH."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__nitrogenous_waste'))
    def rule_blood_plasma_composition__nitrogenous_waste(self):
        """Blood plasma carries nitrogenous byproducts of metabolism, which are waste products that need to be excreted from the body. These include urea, uric acid, and creatinine."""
        self.response = {
            'concept': 'Blood Plasma Composition: Nitrogenous Waste',
            'explanation': """Blood plasma carries nitrogenous byproducts of metabolism, which are waste products that need to be excreted from the body. These include urea, uric acid, and creatinine.""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Urea is transported from the liver to the kidneys for elimination.", "Elevated levels of creatinine in plasma can indicate kidney dysfunction.", "Uric acid is a byproduct of nucleic acid metabolism carried in plasma."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__gases'))
    def rule_blood_plasma_composition__gases(self):
        """Blood plasma transports various dissolved gases throughout the body. These include respiratory gases like oxygen (O2) and carbon dioxide (CO2), as well as inert gases like nitrogen (N2)."""
        self.response = {
            'concept': 'Blood Plasma Composition: Gases',
            'explanation': """Blood plasma transports various dissolved gases throughout the body. These include respiratory gases like oxygen (O2) and carbon dioxide (CO2), as well as inert gases like nitrogen (N2).""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Oxygen is transported from the lungs to tissues for cellular respiration.", "Carbon dioxide is carried from tissues to the lungs for exhalation.", "Nitrogen gas is dissolved in plasma but not utilized metabolically."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma_composition__hormones__antibodies__antigens'))
    def rule_blood_plasma_composition__hormones__antibodies__antigens(self):
        """Beyond basic components, blood plasma also serves as a medium for transporting specialized biological molecules, including hormones (chemical messengers), antibodies (immune proteins), and antigens (molecules that trigger immune responses)."""
        self.response = {
            'concept': 'Blood Plasma Composition: Hormones, Antibodies, Antigens',
            'explanation': """Beyond basic components, blood plasma also serves as a medium for transporting specialized biological molecules, including hormones (chemical messengers), antibodies (immune proteins), and antigens (molecules that trigger immune responses).""",
            'topic': 'Biology',
            'subtopic': 'Blood Plasma Composition',
            'examples': ["Hormones like insulin or thyroid hormone travel through plasma to target organs.", "Antibodies in plasma provide immunity against pathogens.", "Antigens on cell surfaces are recognized by the immune system through plasma components."]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_blood__transportation_of_materials'))
    def rule_function_of_blood__transportation_of_materials(self):
        """One of the primary functions of blood is to transport essential materials throughout the body, including digested end products (nutrients), respiratory gases (O2, CO2), excretory byproducts, hormones, mineral ions, and proteins."""
        self.response = {
            'concept': 'Function of Blood: Transportation of Materials',
            'explanation': """One of the primary functions of blood is to transport essential materials throughout the body, including digested end products (nutrients), respiratory gases (O2, CO2), excretory byproducts, hormones, mineral ions, and proteins.""",
            'topic': 'Biology',
            'subtopic': 'Functions of Blood',
            'examples': ["Blood carries oxygen from the lungs to all body cells.", "Nutrients absorbed from the small intestine are distributed via blood.", "Metabolic waste products are transported by blood to excretory organs."]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_blood__protection_against_pathogens'))
    def rule_function_of_blood__protection_against_pathogens(self):
        """Blood provides crucial protection against pathogenic microbes. It achieves this through mechanisms like phagocytosis by white blood cells, which engulf invaders, and by producing antibodies to neutralize threats."""
        self.response = {
            'concept': 'Function of Blood: Protection Against Pathogens',
            'explanation': """Blood provides crucial protection against pathogenic microbes. It achieves this through mechanisms like phagocytosis by white blood cells, which engulf invaders, and by producing antibodies to neutralize threats.""",
            'topic': 'Biology',
            'subtopic': 'Functions of Blood',
            'examples': ["White blood cells in blood destroy bacteria and viruses.", "Antibodies circulating in plasma identify and mark pathogens for destruction.", "The immune components in blood defend the body from infection."]
        }
        self.halt()

    @Rule(Fact(query_topic='function_of_blood__maintenance_of_chemical_coordination_and_homeostasis'))
    def rule_function_of_blood__maintenance_of_chemical_coordination_and_homeostasis(self):
        """Blood is vital for maintaining chemical coordination among various tissues and organs by transporting hormones. It also plays a key role in preserving homeostasis by regulating factors like body temperature, pH, and fluid balance."""
        self.response = {
            'concept': 'Function of Blood: Maintenance of Chemical Coordination and Homeostasis',
            'explanation': """Blood is vital for maintaining chemical coordination among various tissues and organs by transporting hormones. It also plays a key role in preserving homeostasis by regulating factors like body temperature, pH, and fluid balance.""",
            'topic': 'Biology',
            'subtopic': 'Functions of Blood',
            'examples': ["Hormones transported by blood coordinate growth and metabolism.", "Blood acts as a buffer system to stabilize the body's pH.", "Blood flow is regulated to distribute heat and maintain core body temperature."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_circulation_mechanism'))
    def rule_blood_circulation_mechanism(self):
        """Blood is continuously circulated throughout the body by the force generated by the heart. This continuous flow ensures the distribution of vital substances to all tissues and organs."""
        self.response = {
            'concept': 'Blood Circulation Mechanism',
            'explanation': """Blood is continuously circulated throughout the body by the force generated by the heart. This continuous flow ensures the distribution of vital substances to all tissues and organs.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["The heart's pumping action propels blood into arteries.", "Blood flows through a network of vessels to reach every cell.", "Effective circulation is essential for oxygen and nutrient delivery."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_wall_thickness'))
    def rule_heart_wall_thickness(self):
        """The atrial walls of the human heart are thinner than the ventricular walls. Among all chambers, the left ventricle possesses the thickest wall."""
        self.response = {
            'concept': 'Heart Wall Thickness',
            'explanation': """The atrial walls of the human heart are thinner than the ventricular walls. Among all chambers, the left ventricle possesses the thickest wall.""",
            'topic': 'Biology',
            'subtopic': 'Heart Anatomy',
            'examples': ["The right atrial wall is comparatively thin.", "The left ventricular wall is significantly thicker to pump blood to the entire body.", "Ventricular walls are generally more muscular than atrial walls."]
        }
        self.halt()

    @Rule(Fact(query_topic='arterial_system_function'))
    def rule_arterial_system_function(self):
        """The arterial system encompasses all arteries within the blood circulatory system. Its primary role is to transport oxygenated blood from the heart to various parts of the body, with the notable exception of the pulmonary artery, which carries deoxygenated blood to the lungs."""
        self.response = {
            'concept': 'Arterial System Function',
            'explanation': """The arterial system encompasses all arteries within the blood circulatory system. Its primary role is to transport oxygenated blood from the heart to various parts of the body, with the notable exception of the pulmonary artery, which carries deoxygenated blood to the lungs.""",
            'topic': 'Biology',
            'subtopic': 'Blood Circulatory System',
            'examples': ["The Aorta distributes oxygenated blood from the left ventricle to systemic arteries.", "The Hepatic artery delivers oxygenated blood to the liver.", "The Pulmonary artery transports deoxygenated blood from the right ventricle to the lungs."]
        }
        self.halt()

    @Rule(Fact(query_topic='venous_system_function'))
    def rule_venous_system_function(self):
        """The venous system comprises all veins in the blood circulatory system, typically responsible for transporting deoxygenated blood back to the heart. An exception to this rule is the pulmonary veins, which carry oxygenated blood from the lungs to the left atrium."""
        self.response = {
            'concept': 'Venous System Function',
            'explanation': """The venous system comprises all veins in the blood circulatory system, typically responsible for transporting deoxygenated blood back to the heart. An exception to this rule is the pulmonary veins, which carry oxygenated blood from the lungs to the left atrium.""",
            'topic': 'Biology',
            'subtopic': 'Blood Circulatory System',
            'examples': ["The Superior vena cava returns deoxygenated blood from the upper body to the right atrium.", "The Renal vein carries deoxygenated blood away from the kidneys.", "The Pulmonary veins deliver oxygenated blood from the lungs to the left atrium."]
        }
        self.halt()

    @Rule(Fact(query_topic='pulmonary_circulation'))
    def rule_pulmonary_circulation(self):
        """Pulmonary circulation is a component of double blood circulation where blood exclusively flows through the lungs for gas exchange. The right ventricle of the heart functions as the pump for this specific circulatory pathway."""
        self.response = {
            'concept': 'Pulmonary Circulation',
            'explanation': """Pulmonary circulation is a component of double blood circulation where blood exclusively flows through the lungs for gas exchange. The right ventricle of the heart functions as the pump for this specific circulatory pathway.""",
            'topic': 'Biology',
            'subtopic': 'Blood Circulation',
            'examples': ["Deoxygenated blood leaves the right ventricle, travels to the lungs via the pulmonary artery.", "Oxygenated blood returns from the lungs to the left atrium through the pulmonary veins.", "Its primary purpose is to oxygenate blood and remove carbon dioxide."]
        }
        self.halt()

    @Rule(Fact(query_topic='systemic_circulation'))
    def rule_systemic_circulation(self):
        """Systemic circulation is the part of double blood circulation where blood is distributed to and collected from all organs and tissues of the body, excluding the lungs. The left ventricle of the heart serves as the pump for this extensive circulatory route."""
        self.response = {
            'concept': 'Systemic Circulation',
            'explanation': """Systemic circulation is the part of double blood circulation where blood is distributed to and collected from all organs and tissues of the body, excluding the lungs. The left ventricle of the heart serves as the pump for this extensive circulatory route.""",
            'topic': 'Biology',
            'subtopic': 'Blood Circulation',
            'examples': ["Oxygenated blood is pumped from the left ventricle to the head and hands.", "Blood flows through arteries to supply organs like the liver, intestines, and kidneys.", "Deoxygenated blood from the body tissues returns to the right atrium via the vena cava."]
        }
        self.halt()

    @Rule(Fact(query_topic='double_circulation'))
    def rule_double_circulation(self):
        """The process in which blood flows twice through the heart before entering into the systemic artery. In humans, this means that when blood circulates once through the body, it flows twice through the heart."""
        self.response = {
            'concept': 'Double Circulation',
            'explanation': """The process in which blood flows twice through the heart before entering into the systemic artery. In humans, this means that when blood circulates once through the body, it flows twice through the heart.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["Blood flows twice through heart before entering into systemic artery.", "In human, when the blood circulates once through the body it flows twice through the heart."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_beat'))
    def rule_heart_beat(self):
        """The rhythmic contractions and dilations of the heart muscle, specifically the atria and ventricles, which are responsible for pumping blood out of the heart."""
        self.response = {
            'concept': 'Heart Beat',
            'explanation': """The rhythmic contractions and dilations of the heart muscle, specifically the atria and ventricles, which are responsible for pumping blood out of the heart.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["Atria and Ventricles of heart contract to pump blood out of the heart.", "These contractions and dilations of heart muscle are known as heart beat."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_beat_rate'))
    def rule_heart_beat_rate(self):
        """The number of heart beats per minute. For a healthy person at rest, this rate is typically 72 beats per minute, which is similar to the pulse rate."""
        self.response = {
            'concept': 'Heart Beat Rate',
            'explanation': """The number of heart beats per minute. For a healthy person at rest, this rate is typically 72 beats per minute, which is similar to the pulse rate.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["The heart beat rate of a healthy person at rest, is 72 beats per minute.", "Pulse rate is also similar to heart beat rate."]
        }
        self.halt()

    @Rule(Fact(query_topic='cardiac_cycle'))
    def rule_cardiac_cycle(self):
        """A complete sequence of events for one heart beat, beginning from its generation to the start of the next beat, involving specific stages of contraction and relaxation of the atria and ventricles."""
        self.response = {
            'concept': 'Cardiac Cycle',
            'explanation': """A complete sequence of events for one heart beat, beginning from its generation to the start of the next beat, involving specific stages of contraction and relaxation of the atria and ventricles.""",
            'topic': 'Biology',
            'subtopic': 'Cardiac Cycle',
            'examples': ["In one heart beat atria contract when ventricles dilate. Next ventricles contract, atria dilate.", "Cardiac cycle refers to a complete heart beat from its generation to the beginning of the next beat."]
        }
        self.halt()

    @Rule(Fact(query_topic='diastole__cardiac_cycle_stage_'))
    def rule_diastole__cardiac_cycle_stage_(self):
        """The stage of the cardiac cycle characterized by atrial contraction, lasting approximately 0.1 seconds."""
        self.response = {
            'concept': 'Diastole (Cardiac Cycle Stage)',
            'explanation': """The stage of the cardiac cycle characterized by atrial contraction, lasting approximately 0.1 seconds.""",
            'topic': 'Biology',
            'subtopic': 'Cardiac Cycle Stages',
            'examples': ["Contraction of atria is known as diastole (0.1 seconds).", "Diastole - Atrial contraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='systole__cardiac_cycle_stage_'))
    def rule_systole__cardiac_cycle_stage_(self):
        """The stage of the cardiac cycle characterized by ventricular contraction, lasting approximately 0.3 seconds."""
        self.response = {
            'concept': 'Systole (Cardiac Cycle Stage)',
            'explanation': """The stage of the cardiac cycle characterized by ventricular contraction, lasting approximately 0.3 seconds.""",
            'topic': 'Biology',
            'subtopic': 'Cardiac Cycle Stages',
            'examples': ["Contraction of ventricles is known as systole (0.3 seconds).", "Systole - Ventricular contraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='intervening__cardiac_cycle_stage_'))
    def rule_intervening__cardiac_cycle_stage_(self):
        """The stage of the cardiac cycle where both atria and ventricles are in a relaxed mode, lasting approximately 0.4 seconds. It is also known as complete cardiac diastole."""
        self.response = {
            'concept': 'Intervening (Cardiac Cycle Stage)',
            'explanation': """The stage of the cardiac cycle where both atria and ventricles are in a relaxed mode, lasting approximately 0.4 seconds. It is also known as complete cardiac diastole.""",
            'topic': 'Biology',
            'subtopic': 'Cardiac Cycle Stages',
            'examples': ["After that atria and ventricles are in relax mode and it is known as intervening (0.4 seconds).", "Intervening - Atrial and Ventricular relaxation (complete cardiac diastole)."]
        }
        self.halt()

    @Rule(Fact(query_topic='electrocardiogram__ecg_'))
    def rule_electrocardiogram__ecg_(self):
        """A diagnostic tool used to obtain information about heart function by tracing the potential changes that occur in cardiac muscle cells during heart activity. It can identify the three stages of the cardiac cycle."""
        self.response = {
            'concept': 'Electrocardiogram (ECG)',
            'explanation': """A diagnostic tool used to obtain information about heart function by tracing the potential changes that occur in cardiac muscle cells during heart activity. It can identify the three stages of the cardiac cycle.""",
            'topic': 'Biology',
            'subtopic': 'Cardiac Diagnostics',
            'examples': ["Electro cardio gram (E.C.G) is used to get information about heart function.", "This tracing denote the potential changes take place in cardiac muscle cells during heart function.", "Three stages of cardiac cycle can be identified in ECG."]
        }
        self.halt()

    @Rule(Fact(query_topic='ecg_wave_patterns'))
    def rule_ecg_wave_patterns(self):
        """Specific deflections on an ECG tracing that represent different phases of the cardiac cycle: the P wave indicates atrial contraction, the QRS complex indicates ventricular contraction, and the T wave indicates the intervening relaxation period. Deviations from normal patterns suggest heart dysfunction."""
        self.response = {
            'concept': 'ECG Wave Patterns',
            'explanation': """Specific deflections on an ECG tracing that represent different phases of the cardiac cycle: the P wave indicates atrial contraction, the QRS complex indicates ventricular contraction, and the T wave indicates the intervening relaxation period. Deviations from normal patterns suggest heart dysfunction.""",
            'topic': 'Biology',
            'subtopic': 'ECG Interpretation',
            'examples': ["P - Atrial contraction", "QRS - Ventricular contraction", "T - Intervening", "ECG wave patterns deviate from normal patterns due to dysfunction of heart."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_sounds__lub_dup_'))
    def rule_heart_sounds__lub_dup_(self):
        """The characteristic sounds produced by the heart during a beat. The longer 'Lub' sound occurs when the bicuspid and tricuspid valves close during atrial contraction. The shorter 'Dup' sound follows, produced by the closing of the semi-lunar valves."""
        self.response = {
            'concept': 'Heart Sounds (Lub-Dup)',
            'explanation': """The characteristic sounds produced by the heart during a beat. The longer 'Lub' sound occurs when the bicuspid and tricuspid valves close during atrial contraction. The shorter 'Dup' sound follows, produced by the closing of the semi-lunar valves.""",
            'topic': 'Biology',
            'subtopic': 'Heart Function',
            'examples': ["Lub - Dup sound in heart beat can be heard by keeping ear or stethoscope on chest.", "Lub sound is produced when bicuspid and tricuspid valves close in atrial contraction.", "This Dup sound is resulted when semi lunar valves close."]
        }
        self.halt()

    @Rule(Fact(query_topic='systolic_blood_pressure'))
    def rule_systolic_blood_pressure(self):
        """The force created on the arteries when the heart pumps blood through them to the rest of the body. A normal systolic blood pressure is 110-120 mmHg."""
        self.response = {
            'concept': 'Systolic Blood Pressure',
            'explanation': """The force created on the arteries when the heart pumps blood through them to the rest of the body. A normal systolic blood pressure is 110-120 mmHg.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System',
            'examples': ["In a blood pressure reading of 120/80 mmHg, '120' represents the systolic pressure.", "A patient's systolic blood pressure of 115 mmHg falls within the normal range.", "High systolic pressure can indicate increased strain on arteries during heart contractions."]
        }
        self.halt()

    @Rule(Fact(query_topic='diastolic_blood_pressure'))
    def rule_diastolic_blood_pressure(self):
        """The pressure in the arteries when the heart rests between beats. A normal diastolic blood pressure is between 70-80 mmHg."""
        self.response = {
            'concept': 'Diastolic Blood Pressure',
            'explanation': """The pressure in the arteries when the heart rests between beats. A normal diastolic blood pressure is between 70-80 mmHg.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System',
            'examples': ["In a blood pressure reading of 120/80 mmHg, '80' represents the diastolic pressure.", "A diastolic pressure of 72 mmHg is considered normal.", "Diastolic pressure reflects the minimum arterial pressure during cardiac relaxation."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_pressure_measurement_unit'))
    def rule_blood_pressure_measurement_unit(self):
        """Blood pressure is measured in millimeters of mercury."""
        self.response = {
            'concept': 'Blood Pressure Measurement Unit',
            'explanation': """Blood pressure is measured in millimeters of mercury.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System',
            'examples': ["The 'mmHg' in 120/80 mmHg stands for millimeters of mercury.", "Healthcare professionals use mmHg to quantify blood pressure readings.", "Units like kPa are also used, but mmHg is standard in clinical settings."]
        }
        self.halt()

    @Rule(Fact(query_topic='normal_resting_blood_pressure'))
    def rule_normal_resting_blood_pressure(self):
        """A standard representation for normal resting blood pressure, indicated as 120/80 mmHg."""
        self.response = {
            'concept': 'Normal Resting Blood Pressure',
            'explanation': """A standard representation for normal resting blood pressure, indicated as 120/80 mmHg.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System',
            'examples': ["An individual with a consistent blood pressure of 120/80 mmHg has normal resting blood pressure.", "The target for healthy blood pressure is often cited as 120/80 mmHg.", "Deviations from 120/80 mmHg may indicate hypertension or hypotension."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_increasing_blood_pressure'))
    def rule_factors_increasing_blood_pressure(self):
        """Several factors can cause an increase in blood pressure."""
        self.response = {
            'concept': 'Factors Increasing Blood Pressure',
            'explanation': """Several factors can cause an increase in blood pressure.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System',
            'examples': ["Ageing is a common factor that can lead to increased blood pressure.", "Stressful mentality can cause a temporary or chronic elevation in blood pressure.", "Certain diseases can contribute to higher blood pressure readings."]
        }
        self.halt()

    @Rule(Fact(query_topic='lymphatic_system'))
    def rule_lymphatic_system(self):
        """A transportation system in the human body that is closely linked with the blood circulatory system."""
        self.response = {
            'concept': 'Lymphatic System',
            'explanation': """A transportation system in the human body that is closely linked with the blood circulatory system.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["The lymphatic system plays a crucial role in fluid balance and immune function.", "Unlike the cardiovascular system, the lymphatic system is a one-way drainage system.", "Edema can occur if the lymphatic system is not functioning properly."]
        }
        self.halt()

    @Rule(Fact(query_topic='tissue_fluid'))
    def rule_tissue_fluid(self):
        """Fluid formed when WBCs and blood plasma move through the thin walls of blood capillaries into the tissues. RBCs and some plasma proteins cannot pass through the capillary wall. Materials are exchanged between somatic cells and blood through this fluid."""
        self.response = {
            'concept': 'Tissue Fluid',
            'explanation': """Fluid formed when WBCs and blood plasma move through the thin walls of blood capillaries into the tissues. RBCs and some plasma proteins cannot pass through the capillary wall. Materials are exchanged between somatic cells and blood through this fluid.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Tissue fluid surrounds cells, delivering nutrients and removing waste.", "The composition of tissue fluid is similar to blood plasma but without large proteins and red blood cells.", "Part of the tissue fluid is reabsorbed back into the capillaries."]
        }
        self.halt()

    @Rule(Fact(query_topic='lymph'))
    def rule_lymph(self):
        """The tissue fluid that flows within the lymphatic vessels."""
        self.response = {
            'concept': 'Lymph',
            'explanation': """The tissue fluid that flows within the lymphatic vessels.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Once tissue fluid enters a lymphatic capillary, it is called lymph.", "Lymph transports immune cells throughout the body.", "Lymph is typically clear and watery, similar to plasma."]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_lymphatic_system'))
    def rule_components_of_lymphatic_system(self):
        """The lymphatic system consists of lacteals, lymph capillaries, and lymph nodes."""
        self.response = {
            'concept': 'Components of Lymphatic System',
            'explanation': """The lymphatic system consists of lacteals, lymph capillaries, and lymph nodes.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System Structure',
            'examples': ["Lacteals are specialized lymph capillaries in the small intestine.", "Lymph nodes filter lymph and house immune cells.", "Lymph capillaries are tiny vessels that collect tissue fluid."]
        }
        self.halt()

    @Rule(Fact(query_topic='lymph_flow_mechanism'))
    def rule_lymph_flow_mechanism(self):
        """Lymph flows due to the pressure caused by muscles around the lymph vessels."""
        self.response = {
            'concept': 'Lymph Flow Mechanism',
            'explanation': """Lymph flows due to the pressure caused by muscles around the lymph vessels.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System Function',
            'examples': ["Skeletal muscle contractions help to pump lymph through the lymphatic vessels.", "Movement and exercise are important for effective lymph circulation.", "Unlike blood, lymph does not have a central pump like the heart."]
        }
        self.halt()

    @Rule(Fact(query_topic='main_lymph_vessels'))
    def rule_main_lymph_vessels(self):
        """All the lymph vessels in the body form two main vessels: the Thoracic duct and the Right lymphatic duct."""
        self.response = {
            'concept': 'Main Lymph Vessels',
            'explanation': """All the lymph vessels in the body form two main vessels: the Thoracic duct and the Right lymphatic duct.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System Structure',
            'examples': ["The thoracic duct collects lymph from most of the body.", "The right lymphatic duct drains lymph from the upper right quadrant of the body.", "These main ducts return lymph to the subclavian veins."]
        }
        self.halt()

    @Rule(Fact(query_topic='thoracic_duct_drainage'))
    def rule_thoracic_duct_drainage(self):
        """The Thoracic duct empties lymph into the left subclavian vein."""
        self.response = {
            'concept': 'Thoracic Duct Drainage',
            'explanation': """The Thoracic duct empties lymph into the left subclavian vein.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System Function',
            'examples': ["Lymph collected from the lower body eventually drains into the left subclavian vein via the thoracic duct.", "The thoracic duct is the largest lymphatic vessel in the body.", "Return of lymph to the subclavian vein reintroduces filtered fluid back into the blood circulation."]
        }
        self.halt()

    @Rule(Fact(query_topic='right_lymphatic_duct_function'))
    def rule_right_lymphatic_duct_function(self):
        """The right lymphatic duct is responsible for collecting lymph and emptying it into the right subclavian vein, from where it subsequently enters the general venous circulation."""
        self.response = {
            'concept': 'Right Lymphatic Duct Function',
            'explanation': """The right lymphatic duct is responsible for collecting lymph and emptying it into the right subclavian vein, from where it subsequently enters the general venous circulation.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Lymph drainage into the right subclavian vein", "Return of lymph to venous circulation", "Lymph collected from the upper right quadrant of the body"]
        }
        self.halt()

    @Rule(Fact(query_topic='main_function_of_lymphatic_system'))
    def rule_main_function_of_lymphatic_system(self):
        """The primary role of the lymphatic system is the destruction of infectious organisms, such as bacteria, thereby playing a crucial part in the body's immune defense."""
        self.response = {
            'concept': 'Main Function of Lymphatic System',
            'explanation': """The primary role of the lymphatic system is the destruction of infectious organisms, such as bacteria, thereby playing a crucial part in the body's immune defense.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Eliminating bacteria from the body", "Immune response against pathogens", "Filtering out infectious agents"]
        }
        self.halt()

    @Rule(Fact(query_topic='lymph_node_destruction_mechanism'))
    def rule_lymph_node_destruction_mechanism(self):
        """Within lymph nodes, White Blood Cells (WBCs) destroy infectious organisms through a process called phagocytosis. During active destruction, these lymph nodes become more active and can appear swollen (Kuddeti)."""
        self.response = {
            'concept': 'Lymph Node Destruction Mechanism',
            'explanation': """Within lymph nodes, White Blood Cells (WBCs) destroy infectious organisms through a process called phagocytosis. During active destruction, these lymph nodes become more active and can appear swollen (Kuddeti).""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System / Immune System',
            'examples': ["WBCs engulfing bacteria in lymph nodes", "Phagocytic activity in response to infection", "Swollen lymph nodes indicating immune activity"]
        }
        self.halt()

    @Rule(Fact(query_topic='lymph_node_locations'))
    def rule_lymph_node_locations(self):
        """Lymph nodes are found in various strategic locations throughout the body, often in clusters, to effectively filter lymph."""
        self.response = {
            'concept': 'Lymph Node Locations',
            'explanation': """Lymph nodes are found in various strategic locations throughout the body, often in clusters, to effectively filter lymph.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Around the liver", "In the armpits", "Around the throat"]
        }
        self.halt()

    @Rule(Fact(query_topic='cholesterol'))
    def rule_cholesterol(self):
        """Cholesterol is an essential lipid compound naturally produced by the liver. Due to its insolubility in water, it must be transported in the bloodstream by combining with proteins, forming lipoproteins."""
        self.response = {
            'concept': 'Cholesterol',
            'explanation': """Cholesterol is an essential lipid compound naturally produced by the liver. Due to its insolubility in water, it must be transported in the bloodstream by combining with proteins, forming lipoproteins.""",
            'topic': 'Biology',
            'subtopic': 'Lipids / Human Physiology',
            'examples': ["An essential lipid compound", "Produced by the liver", "Insoluble in water"]
        }
        self.halt()

    @Rule(Fact(query_topic='lipoproteins'))
    def rule_lipoproteins(self):
        """Lipoproteins are complexes formed by cholesterol and proteins, enabling the transport of cholesterol through the body's aqueous circulatory system. They are classified into two main types: Low Density Lipoproteins (LDL) and High Density Lipoproteins (HDL)."""
        self.response = {
            'concept': 'Lipoproteins',
            'explanation': """Lipoproteins are complexes formed by cholesterol and proteins, enabling the transport of cholesterol through the body's aqueous circulatory system. They are classified into two main types: Low Density Lipoproteins (LDL) and High Density Lipoproteins (HDL).""",
            'topic': 'Biology',
            'subtopic': 'Lipids / Blood Transport',
            'examples': ["LDL (Low Density Lipoproteins)", "HDL (High Density Lipoproteins)", "Transporting cholesterol in blood"]
        }
        self.halt()

    @Rule(Fact(query_topic='low_density_lipoproteins__ldl_'))
    def rule_low_density_lipoproteins__ldl_(self):
        """Low Density Lipoproteins (LDL) are a type of lipoprotein that, when present in excessive amounts, can deposit in coronary and other arteries, contributing to arterial narrowing and disease."""
        self.response = {
            'concept': 'Low Density Lipoproteins (LDL)',
            'explanation': """Low Density Lipoproteins (LDL) are a type of lipoprotein that, when present in excessive amounts, can deposit in coronary and other arteries, contributing to arterial narrowing and disease.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System / Lipids',
            'examples': ["Excessive amounts deposit in arteries", "Contributes to arterial blockages", "Often referred to as 'bad cholesterol'"]
        }
        self.halt()

    @Rule(Fact(query_topic='atheroma'))
    def rule_atheroma(self):
        """Atheroma refers to the lipid deposits that accumulate on the inner walls of arteries, typically resulting from excessive levels of low-density lipoproteins (LDL) in the bloodstream."""
        self.response = {
            'concept': 'Atheroma',
            'explanation': """Atheroma refers to the lipid deposits that accumulate on the inner walls of arteries, typically resulting from excessive levels of low-density lipoproteins (LDL) in the bloodstream.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System / Diseases',
            'examples': ["Lipid deposits in arteries", "Plaque-like buildup", "Narrowing the arterial lumen"]
        }
        self.halt()

    @Rule(Fact(query_topic='artherosclerosis'))
    def rule_artherosclerosis(self):
        """Artherosclerosis is a condition characterized by the formation of atheroma (lipid deposits) in coronary and other arteries, which reduces the size of the arterial lumen and impairs blood flow."""
        self.response = {
            'concept': 'Artherosclerosis',
            'explanation': """Artherosclerosis is a condition characterized by the formation of atheroma (lipid deposits) in coronary and other arteries, which reduces the size of the arterial lumen and impairs blood flow.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System / Diseases',
            'examples': ["Reduction of lumen size in arteries", "Blocked coronary arteries", "Condition caused by lipid deposits"]
        }
        self.halt()

    @Rule(Fact(query_topic='angina_pectoris__chest_pain_'))
    def rule_angina_pectoris__chest_pain_(self):
        """Angina, or chest pain, is a symptom caused by insufficient blood supply to the heart muscle, typically due to the blocking of coronary arteries. This can lead to parts of the cardiac muscle failing to function properly."""
        self.response = {
            'concept': 'Angina Pectoris (Chest Pain)',
            'explanation': """Angina, or chest pain, is a symptom caused by insufficient blood supply to the heart muscle, typically due to the blocking of coronary arteries. This can lead to parts of the cardiac muscle failing to function properly.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System / Diseases',
            'examples': ["Chest pain as a symptom", "Caused by blocked coronary arteries", "Indication of affected blood supply to heart"]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_failure'))
    def rule_heart_failure(self):
        """Heart failure occurs when a region of the cardiac muscle does not receive adequate blood supply due to blockages in the coronary arteries, leading to that specific region of the heart muscle failing to function."""
        self.response = {
            'concept': 'Heart Failure',
            'explanation': """Heart failure occurs when a region of the cardiac muscle does not receive adequate blood supply due to blockages in the coronary arteries, leading to that specific region of the heart muscle failing to function.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular System / Diseases',
            'examples': ["Region of cardiac muscle not receiving blood", "Cardiac muscle failing to function", "Result of blocked coronary arteries"]
        }
        self.halt()

    @Rule(Fact(query_topic='causes_of_increased_ldl_levels'))
    def rule_causes_of_increased_ldl_levels(self):
        """Elevated levels of Low Density Lipoproteins (LDL) are primarily attributed to the consumption of foods that contain a high amount of saturated fatty acids."""
        self.response = {
            'concept': 'Causes of Increased LDL Levels',
            'explanation': """Elevated levels of Low Density Lipoproteins (LDL) are primarily attributed to the consumption of foods that contain a high amount of saturated fatty acids.""",
            'topic': 'Biology',
            'subtopic': 'Nutrition / Cardiovascular Health',
            'examples': ["Consumption of beef and pork", "Intake of full cream milk", "Eating egg yolk and prawns"]
        }
        self.halt()

    @Rule(Fact(query_topic='artherosclerosis_control_and_prevention'))
    def rule_artherosclerosis_control_and_prevention(self):
        """Artherosclerosis can be controlled and prevented through lifestyle modifications, specifically by managing the intake of foods high in saturated fatty acids and engaging in regular physical exercise."""
        self.response = {
            'concept': 'Artherosclerosis Control and Prevention',
            'explanation': """Artherosclerosis can be controlled and prevented through lifestyle modifications, specifically by managing the intake of foods high in saturated fatty acids and engaging in regular physical exercise.""",
            'topic': 'Biology',
            'subtopic': 'Cardiovascular Health / Lifestyle',
            'examples': ["Controlling food types with saturated fatty acids", "Regular exercises", "Reducing consumption of full cream milk and liver"]
        }
        self.halt()

    @Rule(Fact(query_topic='hypertension'))
    def rule_hypertension(self):
        """Hypertension, also known as high blood pressure, occurs when the lumen size of arteries reduces (e.g., due to cholesterol), lowering blood supply to organs. To compensate, the heart exerts more pressure, leading to a higher pressure exerted onto the arterial wall."""
        self.response = {
            'concept': 'Hypertension',
            'explanation': """Hypertension, also known as high blood pressure, occurs when the lumen size of arteries reduces (e.g., due to cholesterol), lowering blood supply to organs. To compensate, the heart exerts more pressure, leading to a higher pressure exerted onto the arterial wall.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["Reducing consumption of saturated fatty acid helps control hypertension.", "Avoiding smoking is a measure to control high blood pressure.", "Managing mental stress can help control hypertension."]
        }
        self.halt()

    @Rule(Fact(query_topic='hypotension'))
    def rule_hypotension(self):
        """Hypotension is the condition of low blood pressure, where blood pressure becomes less than the normal level. It occurs mostly due to nutrient deficiencies or a reduction in the elasticity of the artery or arteriole wall. Individuals experiencing this condition require treatments to quickly normalize their blood pressure."""
        self.response = {
            'concept': 'Hypotension',
            'explanation': """Hypotension is the condition of low blood pressure, where blood pressure becomes less than the normal level. It occurs mostly due to nutrient deficiencies or a reduction in the elasticity of the artery or arteriole wall. Individuals experiencing this condition require treatments to quickly normalize their blood pressure.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["Low blood pressure occurring in an individual due to a lack of essential nutrients.", "A patient needing immediate medical intervention to raise their blood pressure to a normal range.", "Reduced elasticity in arterial walls contributing to a person's lower than normal blood pressure."]
        }
        self.halt()

    @Rule(Fact(query_topic='thrombosis'))
    def rule_thrombosis(self):
        """Thrombosis is a condition where the blood supply to a certain organ is adversely affected due to the formation of a blood clot within a blood vessel."""
        self.response = {
            'concept': 'Thrombosis',
            'explanation': """Thrombosis is a condition where the blood supply to a certain organ is adversely affected due to the formation of a blood clot within a blood vessel.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["A blood clot forming in a leg vein, obstructing blood flow to the limb.", "Avoiding alcohol and smoking to reduce the risk of blood clot formation.", "Consuming food with more fibre as a preventative measure against thrombosis."]
        }
        self.halt()

    @Rule(Fact(query_topic='paralysis'))
    def rule_paralysis(self):
        """Paralysis is a condition that occurs when the blood supply to a specific part of the brain is compromised due to a blood clot, causing the organs controlled by that affected brain region to fail."""
        self.response = {
            'concept': 'Paralysis',
            'explanation': """Paralysis is a condition that occurs when the blood supply to a specific part of the brain is compromised due to a blood clot, causing the organs controlled by that affected brain region to fail.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["Loss of movement in an arm or leg following a blood clot in the brain.", "Speech difficulties experienced after a part of the brain is deprived of blood due to a clot.", "Failure of sensory functions in a body part due to thrombosis affecting a corresponding brain area."]
        }
        self.halt()

    @Rule(Fact(query_topic='coronary_thrombosis'))
    def rule_coronary_thrombosis(self):
        """Coronary thrombosis is a specific type of thrombosis where a blood clot forms in a coronary artery, thereby affecting the normal function of the heart."""
        self.response = {
            'concept': 'Coronary Thrombosis',
            'explanation': """Coronary thrombosis is a specific type of thrombosis where a blood clot forms in a coronary artery, thereby affecting the normal function of the heart.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["A blood clot blocking a major artery responsible for supplying blood to the heart muscle.", "Impaired pumping ability of the heart due to a clot forming in a coronary vessel.", "A person diagnosed with thrombosis specifically located in the arteries that surround the heart."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_attack'))
    def rule_heart_attack(self):
        """A heart attack is a severe medical event that may occur as a direct consequence of coronary thrombosis, where the heart's function is critically affected due to a blood clot in a coronary artery."""
        self.response = {
            'concept': 'Heart Attack',
            'explanation': """A heart attack is a severe medical event that may occur as a direct consequence of coronary thrombosis, where the heart's function is critically affected due to a blood clot in a coronary artery.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["A sudden onset of severe chest pain and breathlessness due to a blockage in a coronary artery.", "Damage to heart muscle tissue resulting from a prolonged lack of blood supply caused by a clot.", "An emergency situation where immediate medical attention is required to restore blood flow to the heart."]
        }
        self.halt()

    @Rule(Fact(query_topic='coordination'))
    def rule_coordination(self):
        """The adaptation of the body according to changes in both external and internal environments to carry out body functions smoothly."""
        self.response = {
            'concept': 'Coordination',
            'explanation': """The adaptation of the body according to changes in both external and internal environments to carry out body functions smoothly.""",
            'topic': 'Biology',
            'subtopic': 'Regulation & Control',
            'examples': ["Identification of changes in the environment and responding accordingly", "The body maintaining a stable internal temperature", "Regulating blood glucose levels"]
        }
        self.halt()

    @Rule(Fact(query_topic='stimulus'))
    def rule_stimulus(self):
        """A change that takes place in the external or internal environment which is detectable by sensory organs."""
        self.response = {
            'concept': 'Stimulus',
            'explanation': """A change that takes place in the external or internal environment which is detectable by sensory organs.""",
            'topic': 'Biology',
            'subtopic': 'Sensory Perception',
            'examples': ["Light energy detected by the eye", "Touch due to a thorn prick on the leg", "The smell of tasty food"]
        }
        self.halt()

    @Rule(Fact(query_topic='sensory_organs___receptors'))
    def rule_sensory_organs___receptors(self):
        """Organs that can detect (sense) stimuli."""
        self.response = {
            'concept': 'Sensory Organs / Receptors',
            'explanation': """Organs that can detect (sense) stimuli.""",
            'topic': 'Biology',
            'subtopic': 'Sensory Systems',
            'examples': ["Eye (detects light energy)", "Nose (detects smell)", "Skin (detects touch)"]
        }
        self.halt()

    @Rule(Fact(query_topic='response'))
    def rule_response(self):
        """The reaction of the body for a stimulus."""
        self.response = {
            'concept': 'Response',
            'explanation': """The reaction of the body for a stimulus.""",
            'topic': 'Biology',
            'subtopic': 'Physiological Reactions',
            'examples': ["Taking the foot away from a thorn prick", "Saliva secreted into the mouth upon smelling tasty food", "Blinking when exposed to sudden bright light"]
        }
        self.halt()

    @Rule(Fact(query_topic='effectors'))
    def rule_effectors(self):
        """Organs or tissues that carry out the response to a stimulus."""
        self.response = {
            'concept': 'Effectors',
            'explanation': """Organs or tissues that carry out the response to a stimulus.""",
            'topic': 'Biology',
            'subtopic': 'Body Systems',
            'examples': ["Muscles (e.g., muscles of the foot)", "Glands (e.g., salivary glands)", "Skeletal muscles contracting"]
        }
        self.halt()

    @Rule(Fact(query_topic='nervous_system___nervous_coordination'))
    def rule_nervous_system___nervous_coordination(self):
        """A system in the human body responsible for coordination where impulses transmit through nerves and aim at a specific effector."""
        self.response = {
            'concept': 'Nervous System / Nervous Coordination',
            'explanation': """A system in the human body responsible for coordination where impulses transmit through nerves and aim at a specific effector.""",
            'topic': 'Biology',
            'subtopic': 'Coordination Systems',
            'examples': ["A reflex action like pulling your hand away from heat", "Muscle contractions for voluntary movement", "Transmission of pain signals"]
        }
        self.halt()

    @Rule(Fact(query_topic='endocrine_system___chemical_coordination'))
    def rule_endocrine_system___chemical_coordination(self):
        """A system in the human body responsible for coordination where hormones secrete to blood."""
        self.response = {
            'concept': 'Endocrine System / Chemical Coordination',
            'explanation': """A system in the human body responsible for coordination where hormones secrete to blood.""",
            'topic': 'Biology',
            'subtopic': 'Coordination Systems',
            'examples': ["Hormones secreted into the bloodstream", "Regulation of growth by growth hormone", "Insulin controlling blood sugar levels"]
        }
        self.halt()

    @Rule(Fact(query_topic='hormone_concentration_and_effector_response'))
    def rule_hormone_concentration_and_effector_response(self):
        """The response of a particular effector is determined by the concentration of the hormone it encounters."""
        self.response = {
            'concept': 'Hormone Concentration and Effector Response',
            'explanation': """The response of a particular effector is determined by the concentration of the hormone it encounters.""",
            'topic': 'Biology',
            'subtopic': 'Human body processes',
            'examples': ["concentration of hormone", "particular effector respond to it"]
        }
        self.halt()

    @Rule(Fact(query_topic='impulse_transmission_in_nerves'))
    def rule_impulse_transmission_in_nerves(self):
        """Impulses are transmitted through nerves as a result of an electrochemical change occurring within them."""
        self.response = {
            'concept': 'Impulse Transmission in Nerves',
            'explanation': """Impulses are transmitted through nerves as a result of an electrochemical change occurring within them.""",
            'topic': 'Biology',
            'subtopic': 'Nervous coordination',
            'examples': ["electro chemical change in the nerves", "impulses are transmitted through nerves"]
        }
        self.halt()

    @Rule(Fact(query_topic='coordination_in_nervous_system'))
    def rule_coordination_in_nervous_system(self):
        """A proper coordination is maintained between the receptor, which detects stimuli, and the effector, which carries out the response."""
        self.response = {
            'concept': 'Coordination in Nervous System',
            'explanation': """A proper coordination is maintained between the receptor, which detects stimuli, and the effector, which carries out the response.""",
            'topic': 'Biology',
            'subtopic': 'Nervous coordination',
            'examples': ["receptor", "effector", "proper coordination is maintained"]
        }
        self.halt()

    @Rule(Fact(query_topic='structural_unit_of_the_nervous_system'))
    def rule_structural_unit_of_the_nervous_system(self):
        """The fundamental structural unit responsible for nervous system function is the neuron."""
        self.response = {
            'concept': 'Structural Unit of the Nervous System',
            'explanation': """The fundamental structural unit responsible for nervous system function is the neuron.""",
            'topic': 'Biology',
            'subtopic': 'Nervous system',
            'examples': ["structural unit of the nervous system is the neuron", "neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_neurons'))
    def rule_types_of_neurons(self):
        """There are three distinct types of neurons that make up the nervous system, each with specialized functions."""
        self.response = {
            'concept': 'Types of Neurons',
            'explanation': """There are three distinct types of neurons that make up the nervous system, each with specialized functions.""",
            'topic': 'Biology',
            'subtopic': 'Nervous system / Neurons',
            'examples': ["Sensory neuron", "Motor neuron", "Inter neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_the_nervous_system'))
    def rule_components_of_the_nervous_system(self):
        """The nervous system is primarily composed of two main components: the central nervous system and the peripheral nervous system."""
        self.response = {
            'concept': 'Components of the Nervous System',
            'explanation': """The nervous system is primarily composed of two main components: the central nervous system and the peripheral nervous system.""",
            'topic': 'Biology',
            'subtopic': 'Nervous system',
            'examples': ["central nervous system", "peripheral nervous system"]
        }
        self.halt()

    @Rule(Fact(query_topic='central_nervous_system__cns__composition'))
    def rule_central_nervous_system__cns__composition(self):
        """The Central Nervous System (CNS) is comprised of the brain and the spinal cord."""
        self.response = {
            'concept': 'Central Nervous System (CNS) Composition',
            'explanation': """The Central Nervous System (CNS) is comprised of the brain and the spinal cord.""",
            'topic': 'Biology',
            'subtopic': 'Central Nervous System',
            'examples': ["Brain", "Spinal cord", "Central nervous system"]
        }
        self.halt()

    @Rule(Fact(query_topic='peripheral_nervous_system__pns__composition'))
    def rule_peripheral_nervous_system__pns__composition(self):
        """The Peripheral Nervous System (PNS) consists of cranial nerves and spinal nerves."""
        self.response = {
            'concept': 'Peripheral Nervous System (PNS) Composition',
            'explanation': """The Peripheral Nervous System (PNS) consists of cranial nerves and spinal nerves.""",
            'topic': 'Biology',
            'subtopic': 'Peripheral Nervous System',
            'examples': ["Cranial nerves (12 pairs)", "Spinal nerves (31 pairs)", "Peripheral nervous system"]
        }
        self.halt()

    @Rule(Fact(query_topic='importance_and_protection_of_the_central_nervous_system'))
    def rule_importance_and_protection_of_the_central_nervous_system(self):
        """The Central Nervous System (CNS) is crucial for controlling bodily activities and coordination. The brain is protected by the skull, and the spinal cord is protected by the vertebral column."""
        self.response = {
            'concept': 'Importance and Protection of the Central Nervous System',
            'explanation': """The Central Nervous System (CNS) is crucial for controlling bodily activities and coordination. The brain is protected by the skull, and the spinal cord is protected by the vertebral column.""",
            'topic': 'Biology',
            'subtopic': 'Central Nervous System',
            'examples': ["controlling of activities and coordination", "Skull provides protection to the brain", "Vertebral column provides protection to the spinal cord"]
        }
        self.halt()

    @Rule(Fact(query_topic='meninges_and_cerebrospinal_fluid_location'))
    def rule_meninges_and_cerebrospinal_fluid_location(self):
        """The brain and spinal cord are enveloped by protective layers called meninges. A special fluid, known as cerebrospinal fluid, is found within the brain's cavities and between the meninges."""
        self.response = {
            'concept': 'Meninges and Cerebrospinal Fluid Location',
            'explanation': """The brain and spinal cord are enveloped by protective layers called meninges. A special fluid, known as cerebrospinal fluid, is found within the brain's cavities and between the meninges.""",
            'topic': 'Biology',
            'subtopic': 'Central Nervous System',
            'examples': ["Brain and spinal cord are covered by meninges", "fluid found within the cavities of brain", "fluid found between meninges"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_cerebrospinal_fluid__csf_'))
    def rule_functions_of_cerebrospinal_fluid__csf_(self):
        """Cerebrospinal fluid provides buoyant support, absorbs shocks and jerks, protects against microbial infections and desiccation, and guards against temperature fluctuations."""
        self.response = {
            'concept': 'Functions of Cerebrospinal Fluid (CSF)',
            'explanation': """Cerebrospinal fluid provides buoyant support, absorbs shocks and jerks, protects against microbial infections and desiccation, and guards against temperature fluctuations.""",
            'topic': 'Biology',
            'subtopic': 'Cerebrospinal Fluid',
            'examples': ["Support bouncy to brain and spinal cord", "Absorption of shocks and jerks", "Protection against microbial infections and desiccation"]
        }
        self.halt()

    @Rule(Fact(query_topic='brain_protection_and_composition'))
    def rule_brain_protection_and_composition(self):
        """The brain is protected by the cranium and three meningeal linings. It contains billions of neurons and neuroglia, and is structurally divided into the Cerebrum, Cerebellum, and Medulla oblongata."""
        self.response = {
            'concept': 'Brain Protection and Composition',
            'explanation': """The brain is protected by the cranium and three meningeal linings. It contains billions of neurons and neuroglia, and is structurally divided into the Cerebrum, Cerebellum, and Medulla oblongata.""",
            'topic': 'Biology',
            'subtopic': 'Brain',
            'examples': ["Brain is protected by the cranium", "surrounded by three linings called meninges", "composed of three main parts, as Cerebrum, Cerebellum and Medulla oblongata"]
        }
        self.halt()

    @Rule(Fact(query_topic='brain_peripheral_region_composition'))
    def rule_brain_peripheral_region_composition(self):
        """The peripheral region of the brain is composed of grey matter, which consists of cell bodies, and an interior of white matter, which is made up of myelin sheaths covering nerve fibres."""
        self.response = {
            'concept': 'Brain Peripheral Region Composition',
            'explanation': """The peripheral region of the brain is composed of grey matter, which consists of cell bodies, and an interior of white matter, which is made up of myelin sheaths covering nerve fibres.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Structure',
            'examples': ["Grey matter is made up of cell bodies.", "White matter is due to myelin sheath.", "Myelin sheath is made up of nerve fibres."]
        }
        self.halt()

    @Rule(Fact(query_topic='cerebrum_structure'))
    def rule_cerebrum_structure(self):
        """The cerebrum is the largest and most highly developed part of the brain. It is divided into left and right hemispheres, and its cortex is highly convoluted to increase surface area."""
        self.response = {
            'concept': 'Cerebrum Structure',
            'explanation': """The cerebrum is the largest and most highly developed part of the brain. It is divided into left and right hemispheres, and its cortex is highly convoluted to increase surface area.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Structure',
            'examples': ["Largest and most highly developed part of the brain.", "Divided into left and right hemispheres.", "Cortex is highly convoluted to increase surface area."]
        }
        self.halt()

    @Rule(Fact(query_topic='cerebrum_hemispheric_control'))
    def rule_cerebrum_hemispheric_control(self):
        """The left cerebral hemisphere controls the right half of the body, while the right cerebral hemisphere controls the left part of the body."""
        self.response = {
            'concept': 'Cerebrum Hemispheric Control',
            'explanation': """The left cerebral hemisphere controls the right half of the body, while the right cerebral hemisphere controls the left part of the body.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Function',
            'examples': ["Left cerebral hemisphere controls the right half of the body.", "Right cerebral hemisphere controls the left part of the body."]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_cerebrum'))
    def rule_functions_of_cerebrum(self):
        """The cerebrum is responsible for the perception and storage of sensory information, processing senses like vision, taste, smell, hearing, pain, and temperature, performing high mental activities, and controlling voluntary muscle contraction."""
        self.response = {
            'concept': 'Functions of Cerebrum',
            'explanation': """The cerebrum is responsible for the perception and storage of sensory information, processing senses like vision, taste, smell, hearing, pain, and temperature, performing high mental activities, and controlling voluntary muscle contraction.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Function',
            'examples': ["Perception of impulses from receptors.", "Perform high mental activities such as learning and thinking.", "Controlling of voluntary muscle contraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='cerebellum_structure'))
    def rule_cerebellum_structure(self):
        """The cerebellum is located just below the latter part of the cerebrum. It consists of two hemispheres, with grey matter forming the outer layer and white matter forming the interior layer."""
        self.response = {
            'concept': 'Cerebellum Structure',
            'explanation': """The cerebellum is located just below the latter part of the cerebrum. It consists of two hemispheres, with grey matter forming the outer layer and white matter forming the interior layer.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Structure',
            'examples': ["Located just below the latter part of the cerebrum.", "Consists of two hemispheres.", "Grey matter in the outer layer and white matter in the interior layer."]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_cerebellum'))
    def rule_functions_of_cerebellum(self):
        """The cerebellum plays a crucial role in the maintenance of body balance, control of voluntary muscle activity, and overall maintenance of body movement."""
        self.response = {
            'concept': 'Functions of Cerebellum',
            'explanation': """The cerebellum plays a crucial role in the maintenance of body balance, control of voluntary muscle activity, and overall maintenance of body movement.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Function',
            'examples': ["Maintenance of body balance.", "Control of voluntary muscle activity.", "Involve in maintenance of body movement."]
        }
        self.halt()

    @Rule(Fact(query_topic='medulla_oblongata_structure'))
    def rule_medulla_oblongata_structure(self):
        """The medulla oblongata is located anteriorly interior to the cerebellum and serves as an important center for controlling many vital life processes."""
        self.response = {
            'concept': 'Medulla Oblongata Structure',
            'explanation': """The medulla oblongata is located anteriorly interior to the cerebellum and serves as an important center for controlling many vital life processes.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Structure',
            'examples': ["Located anteriorly interior to cerebellum.", "An important centre in controlling many life processes."]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_medulla_oblongata'))
    def rule_functions_of_medulla_oblongata(self):
        """The medulla oblongata controls essential involuntary actions, such as heart rate and respiration rate, and also regulates various reflex actions, including vomiting, coughing, and swallowing."""
        self.response = {
            'concept': 'Functions of Medulla Oblongata',
            'explanation': """The medulla oblongata controls essential involuntary actions, such as heart rate and respiration rate, and also regulates various reflex actions, including vomiting, coughing, and swallowing.""",
            'topic': 'Biology',
            'subtopic': 'Human Brain Function',
            'examples': ["Control involuntary actions such as rate of heart beat.", "Control reflex actions such as vomiting.", "Control reflex actions such as swallowing."]
        }
        self.halt()

    @Rule(Fact(query_topic='spinal_cord_structure'))
    def rule_spinal_cord_structure(self):
        """The spinal cord is a tubular structure that begins from the medulla oblongata and extends inferiorly."""
        self.response = {
            'concept': 'Spinal Cord Structure',
            'explanation': """The spinal cord is a tubular structure that begins from the medulla oblongata and extends inferiorly.""",
            'topic': 'Biology',
            'subtopic': 'Human Nervous System Structure',
            'examples': ["It is a tubular structure.", "Starts from medulla oblongata inferiorly."]
        }
        self.halt()

    @Rule(Fact(query_topic='spinal_cord_structure'))
    def rule_spinal_cord_structure(self):
        """The spinal cord, which runs through the vertebral column, is characterized by white matter located peripherally and grey matter located interiorly, containing a central canal. Spinal nerves originate symmetrically from its sides."""
        self.response = {
            'concept': 'Spinal Cord Structure',
            'explanation': """The spinal cord, which runs through the vertebral column, is characterized by white matter located peripherally and grey matter located interiorly, containing a central canal. Spinal nerves originate symmetrically from its sides.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Grey matter", "White matter", "Spinal nerves"]
        }
        self.halt()

    @Rule(Fact(query_topic='reflex_arc'))
    def rule_reflex_arc(self):
        """The functional unit of the nervous system that ensures proper coordination between receptors and effectors. It involves impulses being sent from receptors to the central nervous system and subsequently to the effectors."""
        self.response = {
            'concept': 'Reflex Arc',
            'explanation': """The functional unit of the nervous system that ensures proper coordination between receptors and effectors. It involves impulses being sent from receptors to the central nervous system and subsequently to the effectors.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Stimulation of pain receptors in the skin", "Impulse transmission through a sensory neuron", "Effector response by muscles of the leg"]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_a_reflex_arc'))
    def rule_components_of_a_reflex_arc(self):
        """A reflex arc involves three types of nerve cells that work together to facilitate reflex actions."""
        self.response = {
            'concept': 'Components of a Reflex Arc',
            'explanation': """A reflex arc involves three types of nerve cells that work together to facilitate reflex actions.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Sensory neuron", "Inter neuron", "Motor neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='reflex_actions'))
    def rule_reflex_actions(self):
        """A sudden, involuntary response to a specific stimulus, which occurs without the conscious involvement of the brain."""
        self.response = {
            'concept': 'Reflex Actions',
            'explanation': """A sudden, involuntary response to a specific stimulus, which occurs without the conscious involvement of the brain.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Moving the hand away from a hot surface", "Lifting the leg when stepping on a thorn", "Sneezing"]
        }
        self.halt()

    @Rule(Fact(query_topic='spinal_reflexes'))
    def rule_spinal_reflexes(self):
        """A type of reflex action where the reflex arc primarily involves the spinal cord, enabling responses without brain consciousness."""
        self.response = {
            'concept': 'Spinal Reflexes',
            'explanation': """A type of reflex action where the reflex arc primarily involves the spinal cord, enabling responses without brain consciousness.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Moving the hand away when it contacts with a hot surface", "Lifting the leg when you step on a thorn"]
        }
        self.halt()

    @Rule(Fact(query_topic='cranial_reflexes'))
    def rule_cranial_reflexes(self):
        """A type of reflex action that involves cranial nerves or brain centers, leading to responses without conscious thought."""
        self.response = {
            'concept': 'Cranial Reflexes',
            'explanation': """A type of reflex action that involves cranial nerves or brain centers, leading to responses without conscious thought.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Sneezing", "Salivation", "Blinking eyelids"]
        }
        self.halt()

    @Rule(Fact(query_topic='autonomic_nervous_system'))
    def rule_autonomic_nervous_system(self):
        """This nervous system supplies nerves to the internal organs of the body, coordinating involuntary activities. Its coordinating centers include the hypothalamus and medulla oblongata."""
        self.response = {
            'concept': 'Autonomic Nervous System',
            'explanation': """This nervous system supplies nerves to the internal organs of the body, coordinating involuntary activities. Its coordinating centers include the hypothalamus and medulla oblongata.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Regulation of heart rate", "Control of digestion", "Maintenance of breathing rhythm"]
        }
        self.halt()

    @Rule(Fact(query_topic='autonomic_nervous_system'))
    def rule_autonomic_nervous_system(self):
        """The autonomic nervous system is composed of two main parts: the sympathetic nervous system and the parasympathetic nervous system. These two parts generally cause opposite effects in the body, helping to regulate involuntary functions."""
        self.response = {
            'concept': 'Autonomic Nervous System',
            'explanation': """The autonomic nervous system is composed of two main parts: the sympathetic nervous system and the parasympathetic nervous system. These two parts generally cause opposite effects in the body, helping to regulate involuntary functions.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Composed of sympathetic and parasympathetic nervous systems", "Regulates involuntary body functions", "Its parts cause opposite effects"]
        }
        self.halt()

    @Rule(Fact(query_topic='sympathetic_nervous_system'))
    def rule_sympathetic_nervous_system(self):
        """A part of the autonomic nervous system that activates during emergency situations, leading to the 'fight or flight' effects. Its physiological changes are later neutralized by the parasympathetic system."""
        self.response = {
            'concept': 'Sympathetic Nervous System',
            'explanation': """A part of the autonomic nervous system that activates during emergency situations, leading to the 'fight or flight' effects. Its physiological changes are later neutralized by the parasympathetic system.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Activates during emergency (fight or flight)", "Reduces size of pupil", "Increases heart beat rate"]
        }
        self.halt()

    @Rule(Fact(query_topic='parasympathetic_nervous_system'))
    def rule_parasympathetic_nervous_system(self):
        """A part of the autonomic nervous system that counteracts the changes caused by the sympathetic system. It helps to bring the body back to a resting state after an emergency, neutralizing 'fight or flight' effects."""
        self.response = {
            'concept': 'Parasympathetic Nervous System',
            'explanation': """A part of the autonomic nervous system that counteracts the changes caused by the sympathetic system. It helps to bring the body back to a resting state after an emergency, neutralizing 'fight or flight' effects.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Neutralizes sympathetic system effects", "Increases size of pupil", "Reduces heart beat rate"]
        }
        self.halt()

    @Rule(Fact(query_topic='chemical_co_ordination'))
    def rule_chemical_co_ordination(self):
        """An essential process for the survival of an organism, comparable to nervous co-ordination. It involves hormones secreted by endocrine glands to regulate various body functions."""
        self.response = {
            'concept': 'Chemical Co-ordination',
            'explanation': """An essential process for the survival of an organism, comparable to nervous co-ordination. It involves hormones secreted by endocrine glands to regulate various body functions.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Involves hormones for regulation", "Uses endocrine glands", "Important for organism survival"]
        }
        self.halt()

    @Rule(Fact(query_topic='hormones'))
    def rule_hormones(self):
        """Organic compounds secreted by endocrine glands directly into the bloodstream. They are transported through blood, produced at one site, and act on specific target organs or cells at another site, requiring only small concentrations to be effective."""
        self.response = {
            'concept': 'Hormones',
            'explanation': """Organic compounds secreted by endocrine glands directly into the bloodstream. They are transported through blood, produced at one site, and act on specific target organs or cells at another site, requiring only small concentrations to be effective.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Are organic compounds", "Transported through blood", "Stimulate target organs or cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='endocrine_glands__ductless_glands_'))
    def rule_endocrine_glands__ductless_glands_(self):
        """Glands that secrete hormones directly into the bloodstream, rather than through ducts. These glands are crucial for chemical co-ordination within the human body."""
        self.response = {
            'concept': 'Endocrine Glands (Ductless Glands)',
            'explanation': """Glands that secrete hormones directly into the bloodstream, rather than through ducts. These glands are crucial for chemical co-ordination within the human body.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Pituitary gland", "Thyroid gland", "Pancreas"]
        }
        self.halt()

    @Rule(Fact(query_topic='pituitary_gland'))
    def rule_pituitary_gland(self):
        """The pituitary gland is located below the hypothalamus in the cerebrum. It secretes Growth Hormone, which increases protein synthesis and promotes the growth of ordinary body tissues and long bones."""
        self.response = {
            'concept': 'Pituitary Gland',
            'explanation': """The pituitary gland is located below the hypothalamus in the cerebrum. It secretes Growth Hormone, which increases protein synthesis and promotes the growth of ordinary body tissues and long bones.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Growth Hormone from the pituitary gland helps increase muscle mass.", "The growth of long bones during childhood is regulated by Growth Hormone.", "Deficiency in Growth Hormone can lead to stunted physical development."]
        }
        self.halt()

    @Rule(Fact(query_topic='thyroid_gland'))
    def rule_thyroid_gland(self):
        """The thyroid gland is located posterior to the trachea and in the dorsal part of the neck. It secretes two main hormones: Calcitonin, which reduces calcium levels in the blood, and Thyroxin, which controls the metabolic rate of the body."""
        self.response = {
            'concept': 'Thyroid Gland',
            'explanation': """The thyroid gland is located posterior to the trachea and in the dorsal part of the neck. It secretes two main hormones: Calcitonin, which reduces calcium levels in the blood, and Thyroxin, which controls the metabolic rate of the body.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Calcitonin helps prevent hypercalcemia by lowering blood calcium.", "Thyroxin regulates how quickly the body uses energy.", "An underactive thyroid gland can lead to a slower metabolic rate."]
        }
        self.halt()

    @Rule(Fact(query_topic='pancreas_gland'))
    def rule_pancreas_gland(self):
        """The pancreas is situated in the bend of the duodenum between the stomach and large intestine. It produces Insulin, which converts glucose into glycogen to lower blood sugar, and Glucagon, which converts glycogen into glucose to raise blood sugar."""
        self.response = {
            'concept': 'Pancreas Gland',
            'explanation': """The pancreas is situated in the bend of the duodenum between the stomach and large intestine. It produces Insulin, which converts glucose into glycogen to lower blood sugar, and Glucagon, which converts glycogen into glucose to raise blood sugar.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["After a meal, insulin is secreted to reduce blood glucose.", "When blood sugar is low, glucagon is released to increase glucose availability.", "The pancreas maintains blood glucose homeostasis through insulin and glucagon."]
        }
        self.halt()

    @Rule(Fact(query_topic='adrenal_glands'))
    def rule_adrenal_glands(self):
        """Adrenal glands are located on the surface of the kidneys. They secrete Adrenaline, a hormone that prepares the body to activate and respond in emergency situations."""
        self.response = {
            'concept': 'Adrenal Glands',
            'explanation': """Adrenal glands are located on the surface of the kidneys. They secrete Adrenaline, a hormone that prepares the body to activate and respond in emergency situations.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Adrenaline causes an increase in heart rate during a fright.", "The 'fight or flight' response is primarily mediated by adrenaline.", "Adrenaline diverts blood to muscles, preparing the body for physical exertion."]
        }
        self.halt()

    @Rule(Fact(query_topic='testes'))
    def rule_testes(self):
        """The testes are located outside the abdominal region. They secrete Testosterone, a hormone responsible for the development of secondary sexual characteristics in boys and for inducing spermatogenesis (sperm production)."""
        self.response = {
            'concept': 'Testes',
            'explanation': """The testes are located outside the abdominal region. They secrete Testosterone, a hormone responsible for the development of secondary sexual characteristics in boys and for inducing spermatogenesis (sperm production).""",
            'topic': 'Biology',
            'subtopic': 'Reproductive System / Endocrine System',
            'examples': ["Testosterone promotes the growth of facial hair in males.", "The deepening of a boy's voice during puberty is due to testosterone.", "Spermatogenesis, the formation of sperm, is regulated by testosterone."]
        }
        self.halt()

    @Rule(Fact(query_topic='ovaries'))
    def rule_ovaries(self):
        """The ovaries are located below the kidneys. They secrete Oestrogen, which is involved in the development of secondary sexual characteristics in girls, and Progesterone, which is crucial for the maintenance of pregnancy and the regulation of the menstrual cycle."""
        self.response = {
            'concept': 'Ovaries',
            'explanation': """The ovaries are located below the kidneys. They secrete Oestrogen, which is involved in the development of secondary sexual characteristics in girls, and Progesterone, which is crucial for the maintenance of pregnancy and the regulation of the menstrual cycle.""",
            'topic': 'Biology',
            'subtopic': 'Reproductive System / Endocrine System',
            'examples': ["Oestrogen stimulates breast development in females.", "Progesterone helps prepare the uterus for implantation of a fertilized egg.", "The cyclical changes in the uterus during the menstrual cycle are controlled by oestrogen and progesterone."]
        }
        self.halt()

    @Rule(Fact(query_topic='homeostasis'))
    def rule_homeostasis(self):
        """Homeostasis is the process of maintaining a constant internal environment within an organism. This constant internal environment is critical because even small changes can significantly affect cellular activities."""
        self.response = {
            'concept': 'Homeostasis',
            'explanation': """Homeostasis is the process of maintaining a constant internal environment within an organism. This constant internal environment is critical because even small changes can significantly affect cellular activities.""",
            'topic': 'Biology',
            'subtopic': 'Physiology',
            'examples': ["Regulating body temperature at a stable 37°C is an example of homeostasis.", "Maintaining blood pH within a narrow range is crucial for homeostasis.", "The body's ability to maintain constant blood pressure demonstrates homeostasis."]
        }
        self.halt()

    @Rule(Fact(query_topic='internal_environment'))
    def rule_internal_environment(self):
        """The internal environment refers to the immediate surroundings of the body's cells, providing the necessary medium for their survival. It includes tissue fluid around cells, plasma around blood cells, and lymph. Maintaining its stability ensures constant conditions within cells."""
        self.response = {
            'concept': 'Internal Environment',
            'explanation': """The internal environment refers to the immediate surroundings of the body's cells, providing the necessary medium for their survival. It includes tissue fluid around cells, plasma around blood cells, and lymph. Maintaining its stability ensures constant conditions within cells.""",
            'topic': 'Biology',
            'subtopic': 'Physiology',
            'examples': ["Tissue fluid directly surrounds body cells, forming part of the internal environment.", "Blood plasma transports nutrients and waste products within the internal environment.", "Lymph is a component of the internal environment, involved in fluid balance and immunity."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_regulated_in_internal_environment'))
    def rule_factors_regulated_in_internal_environment(self):
        """Several critical factors within the internal environment must be precisely regulated to ensure proper cellular function and overall body homeostasis. These factors are maintained within a narrow, tolerated range."""
        self.response = {
            'concept': 'Factors Regulated in Internal Environment',
            'explanation': """Several critical factors within the internal environment must be precisely regulated to ensure proper cellular function and overall body homeostasis. These factors are maintained within a narrow, tolerated range.""",
            'topic': 'Biology',
            'subtopic': 'Homeostasis',
            'examples': ["Blood glucose level is a vital factor regulated by the body.", "Body temperature is constantly monitored and adjusted to maintain constancy.", "Water balance within the body is tightly controlled to prevent dehydration or overhydration."]
        }
        self.halt()

    @Rule(Fact(query_topic='regulation_of_blood_glucose_level'))
    def rule_regulation_of_blood_glucose_level(self):
        """In a healthy adult, the blood glucose level is maintained between 80-120 mg/100 ml of blood. When this level rises above normal, beta cells in the islets of Langerhans within the pancreas secrete more insulin, which then converts glucose into glycogen to lower the blood sugar."""
        self.response = {
            'concept': 'Regulation of Blood Glucose Level',
            'explanation': """In a healthy adult, the blood glucose level is maintained between 80-120 mg/100 ml of blood. When this level rises above normal, beta cells in the islets of Langerhans within the pancreas secrete more insulin, which then converts glucose into glycogen to lower the blood sugar.""",
            'topic': 'Biology',
            'subtopic': 'Homeostasis / Endocrine System',
            'examples': ["After eating a high-carbohydrate meal, insulin secretion increases to lower blood glucose.", "If blood glucose drops too low, counter-regulatory hormones activate to raise it.", "Diabetes mellitus is characterized by the body's inability to properly regulate blood glucose levels."]
        }
        self.halt()

    @Rule(Fact(query_topic='excess_glucose_storage'))
    def rule_excess_glucose_storage(self):
        """Excess glucose is first converted to glycogen and stored in the liver. Any further excess glucose is then converted to fat and stored in adipose tissue."""
        self.response = {
            'concept': 'Excess Glucose Storage',
            'explanation': """Excess glucose is first converted to glycogen and stored in the liver. Any further excess glucose is then converted to fat and stored in adipose tissue.""",
            'topic': 'Biology',
            'subtopic': 'Blood Glucose Regulation',
            'examples': ["After a large meal, the liver stores glucose as glycogen.", "Consuming high amounts of carbohydrates over time leads to fat accumulation in adipose tissue.", "The body efficiently manages energy by converting surplus glucose into storable forms."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_glucose_increase_via_glucagon'))
    def rule_blood_glucose_increase_via_glucagon(self):
        """When blood glucose levels fall below normal (e.g., during starvation), alpha cells in the islets of Langerhans in the pancreas are stimulated to secrete glucagon. Glucagon acts on stored glycogen in the liver, converting it back into glucose which is then released into the blood to raise the blood glucose level to normal."""
        self.response = {
            'concept': 'Blood Glucose Increase via Glucagon',
            'explanation': """When blood glucose levels fall below normal (e.g., during starvation), alpha cells in the islets of Langerhans in the pancreas are stimulated to secrete glucagon. Glucagon acts on stored glycogen in the liver, converting it back into glucose which is then released into the blood to raise the blood glucose level to normal.""",
            'topic': 'Biology',
            'subtopic': 'Blood Glucose Regulation',
            'examples': ["During an overnight fast, glucagon helps maintain stable blood sugar levels.", "A person on a low-carbohydrate diet relies on glucagon to mobilize liver glycogen.", "The hormone glucagon prevents hypoglycemia by stimulating glucose production from stored reserves."]
        }
        self.halt()

    @Rule(Fact(query_topic='causes_of_diabetes'))
    def rule_causes_of_diabetes(self):
        """Diabetes is caused by the absence of beta cells in the pancreas or insufficient secretion of insulin, both of which impair blood glucose regulation."""
        self.response = {
            'concept': 'Causes of Diabetes',
            'explanation': """Diabetes is caused by the absence of beta cells in the pancreas or insufficient secretion of insulin, both of which impair blood glucose regulation.""",
            'topic': 'Biology',
            'subtopic': 'Blood Glucose Regulation',
            'examples': ["Type 1 diabetes results from the autoimmune destruction of insulin-producing beta cells.", "Pancreatic damage can lead to a lack of insulin secretion, causing diabetes.", "Insufficient insulin production prevents cells from taking up glucose from the blood."]
        }
        self.halt()

    @Rule(Fact(query_topic='homoithermic_organisms'))
    def rule_homoithermic_organisms(self):
        """A homoithermic organism is capable of maintaining a constant body temperature, irrespective of fluctuations in the environmental temperature. Humans are an example of a homoithermic organism."""
        self.response = {
            'concept': 'Homoithermic Organisms',
            'explanation': """A homoithermic organism is capable of maintaining a constant body temperature, irrespective of fluctuations in the environmental temperature. Humans are an example of a homoithermic organism.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["Humans maintain an internal temperature of around 37°C whether it's hot or cold outside.", "Birds are also homoithermic, keeping a stable body temperature.", "Homoithermy allows organisms to function efficiently across a range of external temperatures."]
        }
        self.halt()

    @Rule(Fact(query_topic='normal_human_body_temperature_range'))
    def rule_normal_human_body_temperature_range(self):
        """The normal body temperature for humans is 37°C, but it can naturally vary within a range of 36°C to 37.5°C."""
        self.response = {
            'concept': 'Normal Human Body Temperature Range',
            'explanation': """The normal body temperature for humans is 37°C, but it can naturally vary within a range of 36°C to 37.5°C.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["A healthy adult usually has a body temperature close to 37°C.", "A temperature of 36.5°C is still considered within the normal range.", "Slight variations, such as 37.2°C, are common throughout the day."]
        }
        self.halt()

    @Rule(Fact(query_topic='thermoregulatory_centre_location'))
    def rule_thermoregulatory_centre_location(self):
        """The thermoregulatory centre in humans, responsible for controlling body temperature, is located in the hypothalamus of the brain."""
        self.response = {
            'concept': 'Thermoregulatory Centre Location',
            'explanation': """The thermoregulatory centre in humans, responsible for controlling body temperature, is located in the hypothalamus of the brain.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["Damage to the hypothalamus can severely impair a person's ability to regulate their body temperature.", "The hypothalamus continuously monitors internal temperature and initiates appropriate responses.", "Signals from temperature receptors in the skin and blood are processed by the hypothalamus."]
        }
        self.halt()

    @Rule(Fact(query_topic='body_response_to_cold_environment'))
    def rule_body_response_to_cold_environment(self):
        """When environmental temperature drops, the hypothalamus initiates several activities to prevent a decrease in body temperature: reducing blood supply to the skin (vasoconstriction), decreasing sweat production, causing hairs to erect to trap an insulating air layer, and generating heat through shivering if heat loss is substantial."""
        self.response = {
            'concept': 'Body Response to Cold Environment',
            'explanation': """When environmental temperature drops, the hypothalamus initiates several activities to prevent a decrease in body temperature: reducing blood supply to the skin (vasoconstriction), decreasing sweat production, causing hairs to erect to trap an insulating air layer, and generating heat through shivering if heat loss is substantial.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["Shivering to generate heat when exposed to cold.", "Goosebumps forming due to piloerection in chilly conditions.", "Skin appearing pale as blood flow to the surface is reduced to conserve heat."]
        }
        self.halt()

    @Rule(Fact(query_topic='body_response_to_hot_environment'))
    def rule_body_response_to_hot_environment(self):
        """When the internal environmental temperature increases, the hypothalamus stimulates processes to prevent an increase in body temperature: dilating blood vessels in the skin to increase blood supply and heat loss, and increasing sweat production by sweat glands, where the evaporation of sweat absorbs heat from the body, thereby decreasing body temperature."""
        self.response = {
            'concept': 'Body Response to Hot Environment',
            'explanation': """When the internal environmental temperature increases, the hypothalamus stimulates processes to prevent an increase in body temperature: dilating blood vessels in the skin to increase blood supply and heat loss, and increasing sweat production by sweat glands, where the evaporation of sweat absorbs heat from the body, thereby decreasing body temperature.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["Sweating profusely during strenuous exercise to cool down.", "Skin flushing red due to increased blood flow near the surface in hot weather.", "Feeling a cooling sensation as sweat evaporates from the skin after a run."]
        }
        self.halt()

    @Rule(Fact(query_topic='overall_regulation_of_body_temperature'))
    def rule_overall_regulation_of_body_temperature(self):
        """The hypothalamus is the primary organ responsible for the overall regulation of body temperature, orchestrating all the mechanisms to maintain homeostasis."""
        self.response = {
            'concept': 'Overall Regulation of Body Temperature',
            'explanation': """The hypothalamus is the primary organ responsible for the overall regulation of body temperature, orchestrating all the mechanisms to maintain homeostasis.""",
            'topic': 'Biology',
            'subtopic': 'Thermoregulation',
            'examples': ["Whether it's too hot or too cold, the hypothalamus constantly works to keep the body's core temperature stable.", "The ability to regulate body temperature is crucial for human survival.", "Without the hypothalamus, the body would struggle to adapt to temperature changes."]
        }
        self.halt()

    @Rule(Fact(query_topic='initiation_of_water_balance_regulation'))
    def rule_initiation_of_water_balance_regulation(self):
        """When the water level of blood drops, the pituitary gland is stimulated to secrete ADH (Antidiuretic Hormone) to begin the process of regulating water balance."""
        self.response = {
            'concept': 'Initiation of Water Balance Regulation',
            'explanation': """When the water level of blood drops, the pituitary gland is stimulated to secrete ADH (Antidiuretic Hormone) to begin the process of regulating water balance.""",
            'topic': 'Biology',
            'subtopic': 'Water Balance Regulation',
            'examples': ["Feeling thirsty is often accompanied by ADH secretion to conserve body water.", "Dehydration triggers the pituitary to release ADH.", "ADH acts on the kidneys to reabsorb more water back into the blood."]
        }
        self.halt()

    @Rule(Fact(query_topic='antidiuresis_hormone__adh_'))
    def rule_antidiuresis_hormone__adh_(self):
        """ADH acts on the kidney to increase reabsorption of water, thereby reducing the amount of water released with urine. It regulates water balance in the body. When water level in blood is high, the reabsorption of water decreases, and the amount of water released with urine increases."""
        self.response = {
            'concept': 'Antidiuresis Hormone (ADH)',
            'explanation': """ADH acts on the kidney to increase reabsorption of water, thereby reducing the amount of water released with urine. It regulates water balance in the body. When water level in blood is high, the reabsorption of water decreases, and the amount of water released with urine increases.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System / Excretory System',
            'examples': ["ADH is released when the body is dehydrated to conserve water.", "High blood water levels inhibit ADH release, leading to more dilute urine.", "A deficiency in ADH can cause excessive urination."]
        }
        self.halt()

    @Rule(Fact(query_topic='human_body_biological_processes'))
    def rule_human_body_biological_processes(self):
        """Digestion, respiration, blood circulation, excretion, and coordination are several fundamental biological processes that take place in the human body."""
        self.response = {
            'concept': 'Human Body Biological Processes',
            'explanation': """Digestion, respiration, blood circulation, excretion, and coordination are several fundamental biological processes that take place in the human body.""",
            'topic': 'Biology',
            'subtopic': 'Human Physiology Overview',
            'examples': ["Digestion breaks down food into usable nutrients.", "Respiration provides energy for cellular activities.", "Blood circulation transports substances throughout the body."]
        }
        self.halt()

    @Rule(Fact(query_topic='food_digestion'))
    def rule_food_digestion(self):
        """Food digestion is the process by which complex organic compounds are converted into simple organic products which get absorbed into the human body."""
        self.response = {
            'concept': 'Food Digestion',
            'explanation': """Food digestion is the process by which complex organic compounds are converted into simple organic products which get absorbed into the human body.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System',
            'examples': ["Carbohydrates are digested into glucose.", "Proteins are broken down into amino acids.", "Lipids are digested into fatty acids and glycerol."]
        }
        self.halt()

    @Rule(Fact(query_topic='role_of_enzymes_in_digestion'))
    def rule_role_of_enzymes_in_digestion(self):
        """Enzymes are important in food digestion, facilitating the breakdown of complex organic compounds into simpler forms."""
        self.response = {
            'concept': 'Role of Enzymes in Digestion',
            'explanation': """Enzymes are important in food digestion, facilitating the breakdown of complex organic compounds into simpler forms.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System / Enzymes',
            'examples': ["Amylase enzymes break down starch.", "Protease enzymes break down proteins.", "Lipase enzymes break down fats."]
        }
        self.halt()

    @Rule(Fact(query_topic='end_products_of_food_digestion'))
    def rule_end_products_of_food_digestion(self):
        """The end products of food digestion are glucose from carbohydrates, fatty acids and glycerol from lipids, and amino acids from protein."""
        self.response = {
            'concept': 'End Products of Food Digestion',
            'explanation': """The end products of food digestion are glucose from carbohydrates, fatty acids and glycerol from lipids, and amino acids from protein.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System',
            'examples': ["Glucose is absorbed into the bloodstream after carbohydrate digestion.", "Fatty acids and glycerol are absorbed after lipid digestion.", "Amino acids are absorbed to build new proteins."]
        }
        self.halt()

    @Rule(Fact(query_topic='role_of_bile_in_lipid_digestion'))
    def rule_role_of_bile_in_lipid_digestion(self):
        """Bile helps to emulsify lipids in lipid digestion, breaking down large fat globules into smaller ones for easier enzymatic action."""
        self.response = {
            'concept': 'Role of Bile in Lipid Digestion',
            'explanation': """Bile helps to emulsify lipids in lipid digestion, breaking down large fat globules into smaller ones for easier enzymatic action.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System',
            'examples': ["Bile prepares fats for digestion by lipase enzymes.", "Without bile, lipid digestion would be inefficient.", "Bile is produced by the liver and stored in the gallbladder."]
        }
        self.halt()

    @Rule(Fact(query_topic='direct_absorption_of_materials'))
    def rule_direct_absorption_of_materials(self):
        """Several materials, including medicine, vitamins, alcohol, and glucose, are absorbed directly into the blood without requiring digestion."""
        self.response = {
            'concept': 'Direct Absorption of Materials',
            'explanation': """Several materials, including medicine, vitamins, alcohol, and glucose, are absorbed directly into the blood without requiring digestion.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System / Absorption',
            'examples': ["Alcohol can be absorbed directly from the stomach.", "Many vitamins are absorbed intact.", "Simple sugars like glucose can be absorbed directly."]
        }
        self.halt()

    @Rule(Fact(query_topic='respiration__cellular_'))
    def rule_respiration__cellular_(self):
        """Respiration is the process of oxidation of simple foods within living cells to release energy."""
        self.response = {
            'concept': 'Respiration (Cellular)',
            'explanation': """Respiration is the process of oxidation of simple foods within living cells to release energy.""",
            'topic': 'Biology',
            'subtopic': 'Cellular Respiration',
            'examples': ["Aerobic respiration uses oxygen to produce energy.", "Anaerobic respiration occurs without oxygen.", "Glucose is a common 'simple food' oxidized during respiration."]
        }
        self.halt()

    @Rule(Fact(query_topic='respiratory_system_function'))
    def rule_respiratory_system_function(self):
        """The respiratory system is involved in taking oxygen into the lungs and releasing gaseous waste products, such as carbon dioxide, out of the lungs."""
        self.response = {
            'concept': 'Respiratory System Function',
            'explanation': """The respiratory system is involved in taking oxygen into the lungs and releasing gaseous waste products, such as carbon dioxide, out of the lungs.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System',
            'examples': ["Inhalation brings oxygen into the body.", "Exhalation expels carbon dioxide.", "Gas exchange occurs in the alveoli of the lungs."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_production_and_storage_in_respiration'))
    def rule_energy_production_and_storage_in_respiration(self):
        """Part of the energy produced during anaerobic and aerobic respiration is lost as heat, while the rest is deposited in ATP (adenosine triphosphate) as chemical energy for cellular use."""
        self.response = {
            'concept': 'Energy Production and Storage in Respiration',
            'explanation': """Part of the energy produced during anaerobic and aerobic respiration is lost as heat, while the rest is deposited in ATP (adenosine triphosphate) as chemical energy for cellular use.""",
            'topic': 'Biology',
            'subtopic': 'Energy Metabolism',
            'examples': ["ATP is the primary energy currency of the cell.", "Heat generated during respiration helps maintain body temperature.", "Muscle contraction is powered by ATP."]
        }
        self.halt()

    @Rule(Fact(query_topic='excretion'))
    def rule_excretion(self):
        """Excretion is the removal of excretory products, which are waste substances produced during metabolism, from the body."""
        self.response = {
            'concept': 'Excretion',
            'explanation': """Excretion is the removal of excretory products, which are waste substances produced during metabolism, from the body.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System',
            'examples': ["Removal of urea in urine.", "Exhaling carbon dioxide and water vapor.", "Sweating to remove excess salts and water."]
        }
        self.halt()

    @Rule(Fact(query_topic='organs_of_excretion'))
    def rule_organs_of_excretion(self):
        """Kidneys, skin, and lungs are the primary organs which carry out excretion in humans."""
        self.response = {
            'concept': 'Organs of Excretion',
            'explanation': """Kidneys, skin, and lungs are the primary organs which carry out excretion in humans.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System',
            'examples': ["Kidneys filter blood to produce urine.", "Skin releases sweat containing salts and metabolic wastes.", "Lungs remove carbon dioxide, a metabolic waste product."]
        }
        self.halt()

    @Rule(Fact(query_topic='nephron'))
    def rule_nephron(self):
        """The nephron is the functional and structural unit of the kidney. The excretory materials produced within nephrons are collectively referred to as urine."""
        self.response = {
            'concept': 'Nephron',
            'explanation': """The nephron is the functional and structural unit of the kidney. The excretory materials produced within nephrons are collectively referred to as urine.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System / Kidney Structure',
            'examples': ["Each kidney contains millions of nephrons.", "Filtration, reabsorption, and secretion processes occur in the nephron.", "Urine formation begins in the glomerulus of the nephron."]
        }
        self.halt()

    @Rule(Fact(query_topic='urinary_system'))
    def rule_urinary_system(self):
        """The urinary system is the anatomical system involved in the production and removal of urine from the body."""
        self.response = {
            'concept': 'Urinary System',
            'explanation': """The urinary system is the anatomical system involved in the production and removal of urine from the body.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System',
            'examples': ["The kidneys, ureters, bladder, and urethra comprise the urinary system.", "It maintains water and electrolyte balance.", "The bladder stores urine before elimination."]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_blood_circulatory_system'))
    def rule_functions_of_blood_circulatory_system(self):
        """The blood circulatory system has two main functions: circulating substances (like nutrients, oxygen, hormones, and waste products) throughout the body and protecting the body from microorganisms."""
        self.response = {
            'concept': 'Functions of Blood Circulatory System',
            'explanation': """The blood circulatory system has two main functions: circulating substances (like nutrients, oxygen, hormones, and waste products) throughout the body and protecting the body from microorganisms.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["It transports oxygen from lungs to tissues.", "It carries antibodies to fight infections.", "It transports nutrients from the digestive system to cells."]
        }
        self.halt()

    @Rule(Fact(query_topic='composition_of_blood'))
    def rule_composition_of_blood(self):
        """Blood is composed of two main components: blood cells (red blood cells, white blood cells, platelets) and plasma, the liquid matrix."""
        self.response = {
            'concept': 'Composition of Blood',
            'explanation': """Blood is composed of two main components: blood cells (red blood cells, white blood cells, platelets) and plasma, the liquid matrix.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System / Blood',
            'examples': ["Red blood cells are responsible for oxygen transport.", "Plasma carries nutrients and waste products.", "White blood cells are crucial for immune defense."]
        }
        self.halt()

    @Rule(Fact(query_topic='heart_function'))
    def rule_heart_function(self):
        """The heart functions as a pumping machine for the blood circulatory system, propelling blood throughout the body."""
        self.response = {
            'concept': 'Heart Function',
            'explanation': """The heart functions as a pumping machine for the blood circulatory system, propelling blood throughout the body.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System / Heart',
            'examples': ["The heart pumps deoxygenated blood to the lungs.", "It pumps oxygenated blood to the rest of the body.", "The rhythmic contractions of the heart maintain blood flow."]
        }
        self.halt()

    @Rule(Fact(query_topic='double_circulation'))
    def rule_double_circulation(self):
        """A type of circulatory system where blood passes through the heart twice in one complete circuit, consisting of systemic and pulmonary circulation."""
        self.response = {
            'concept': 'Double Circulation',
            'explanation': """A type of circulatory system where blood passes through the heart twice in one complete circuit, consisting of systemic and pulmonary circulation.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["Systemic circulation", "Pulmonary circulation", "Blood flow in mammals"]
        }
        self.halt()

    @Rule(Fact(query_topic='cardiac_cycle_stages'))
    def rule_cardiac_cycle_stages(self):
        """The major stages of a cardiac cycle, which describes the complete sequence of events in the heart, are diastole, systole, and an intervening phase."""
        self.response = {
            'concept': 'Cardiac Cycle Stages',
            'explanation': """The major stages of a cardiac cycle, which describes the complete sequence of events in the heart, are diastole, systole, and an intervening phase.""",
            'topic': 'Biology',
            'subtopic': 'Heart Physiology',
            'examples': ["Diastole (heart relaxation)", "Systole (heart contraction)", "Ventricular filling"]
        }
        self.halt()

    @Rule(Fact(query_topic='lymph_nodes'))
    def rule_lymph_nodes(self):
        """Places in the lymphatic system where lymphatic vessels aggregate, serving to filter lymph and destroy germs that enter the body."""
        self.response = {
            'concept': 'Lymph Nodes',
            'explanation': """Places in the lymphatic system where lymphatic vessels aggregate, serving to filter lymph and destroy germs that enter the body.""",
            'topic': 'Biology',
            'subtopic': 'Lymphatic System',
            'examples': ["Filtering pathogens from lymph", "Destroying bacteria", "Activation of immune cells"]
        }
        self.halt()

    @Rule(Fact(query_topic='coordination__biological_'))
    def rule_coordination__biological_(self):
        """The process of maintaining a proper balance between stimulus and response within an organism."""
        self.response = {
            'concept': 'Coordination (Biological)',
            'explanation': """The process of maintaining a proper balance between stimulus and response within an organism.""",
            'topic': 'Biology',
            'subtopic': 'Regulation',
            'examples': ["Responding to a hot object", "Adjusting pupil size to light changes", "Maintaining body posture"]
        }
        self.halt()

    @Rule(Fact(query_topic='systems_involved_in_coordination'))
    def rule_systems_involved_in_coordination(self):
        """The nervous system and the endocrine system are the two main systems involved in maintaining coordination within the body."""
        self.response = {
            'concept': 'Systems Involved in Coordination',
            'explanation': """The nervous system and the endocrine system are the two main systems involved in maintaining coordination within the body.""",
            'topic': 'Biology',
            'subtopic': 'Regulation / Nervous System / Endocrine System',
            'examples': ["Nerve impulses for rapid responses", "Hormonal regulation for long-term changes", "Reflex actions"]
        }
        self.halt()

    @Rule(Fact(query_topic='units_of_the_nervous_system'))
    def rule_units_of_the_nervous_system(self):
        """The structural unit of the nervous system is the neuron, whereas the functional unit is the reflex arc."""
        self.response = {
            'concept': 'Units of the Nervous System',
            'explanation': """The structural unit of the nervous system is the neuron, whereas the functional unit is the reflex arc.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Neuron (nerve cell)", "Reflex arc", "Sensory neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='central_nervous_system__cns__components'))
    def rule_central_nervous_system__cns__components(self):
        """The central nervous system (CNS) consists of the brain and the spinal cord."""
        self.response = {
            'concept': 'Central Nervous System (CNS) Components',
            'explanation': """The central nervous system (CNS) consists of the brain and the spinal cord.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Brain", "Spinal cord", "Cerebrum"]
        }
        self.halt()

    @Rule(Fact(query_topic='components_of_a_reflex_arc'))
    def rule_components_of_a_reflex_arc(self):
        """A reflex arc is composed of a motor neuron, a sensory neuron, and an interneuron, allowing for rapid, involuntary responses."""
        self.response = {
            'concept': 'Components of a Reflex Arc',
            'explanation': """A reflex arc is composed of a motor neuron, a sensory neuron, and an interneuron, allowing for rapid, involuntary responses.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Sensory neuron", "Interneuron", "Motor neuron"]
        }
        self.halt()

    @Rule(Fact(query_topic='autonomic_nervous_system__ans__function'))
    def rule_autonomic_nervous_system__ans__function(self):
        """The autonomic nervous system is important for controlling involuntary body functions."""
        self.response = {
            'concept': 'Autonomic Nervous System (ANS) Function',
            'explanation': """The autonomic nervous system is important for controlling involuntary body functions.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Heartbeat regulation", "Digestive processes", "Breathing rate control"]
        }
        self.halt()

    @Rule(Fact(query_topic='divisions_of_autonomic_nervous_system'))
    def rule_divisions_of_autonomic_nervous_system(self):
        """The autonomic nervous system is organized to control opposite actions via its two divisions: the sympathetic and parasympathetic nervous systems."""
        self.response = {
            'concept': 'Divisions of Autonomic Nervous System',
            'explanation': """The autonomic nervous system is organized to control opposite actions via its two divisions: the sympathetic and parasympathetic nervous systems.""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': ["Sympathetic nervous system (e.g., increasing heart rate)", "Parasympathetic nervous system (e.g., decreasing heart rate)", "Pupil dilation vs. constriction"]
        }
        self.halt()

    @Rule(Fact(query_topic='hormones_and_chemical_coordination'))
    def rule_hormones_and_chemical_coordination(self):
        """Hormones, secreted into the blood from glands, regulate the chemical coordination of the body."""
        self.response = {
            'concept': 'Hormones and Chemical Coordination',
            'explanation': """Hormones, secreted into the blood from glands, regulate the chemical coordination of the body.""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': ["Insulin regulating blood glucose", "Adrenaline triggering 'fight or flight'", "Thyroxine controlling metabolism"]
        }
        self.halt()

    @Rule(Fact(query_topic='homeostasis'))
    def rule_homeostasis(self):
        """The maintenance of a constant internal environment within the body, free from the changes in the external environment."""
        self.response = {
            'concept': 'Homeostasis',
            'explanation': """The maintenance of a constant internal environment within the body, free from the changes in the external environment.""",
            'topic': 'Biology',
            'subtopic': 'Regulation / Physiology',
            'examples': ["Regulating blood glucose levels", "Maintaining body temperature", "Balancing water levels"]
        }
        self.halt()

    @Rule(Fact(query_topic='causes_of_gastritis'))
    def rule_causes_of_gastritis(self):
        """Gastritis is an inflammation of the lining of the stomach. It can be caused by various factors that irritate or damage the gastric mucosa."""
        self.response = {
            'concept': 'Causes of Gastritis',
            'explanation': """Gastritis is an inflammation of the lining of the stomach. It can be caused by various factors that irritate or damage the gastric mucosa.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System Diseases',
            'examples': ["Helicobacter pylori (H. pylori) bacterial infection", "Excessive alcohol consumption", "Prolonged use of Nonsteroidal Anti-inflammatory Drugs (NSAIDs) like ibuprofen or aspirin"]
        }
        self.halt()

    @Rule(Fact(query_topic='protection_against_protein_digestive_enzymes'))
    def rule_protection_against_protein_digestive_enzymes(self):
        """The digestive system employs several mechanisms to prevent its own walls from being digested by potent protein-digesting enzymes it produces, such as pepsin and trypsin."""
        self.response = {
            'concept': 'Protection Against Protein Digestive Enzymes',
            'explanation': """The digestive system employs several mechanisms to prevent its own walls from being digested by potent protein-digesting enzymes it produces, such as pepsin and trypsin.""",
            'topic': 'Biology',
            'subtopic': 'Digestive System Physiology',
            'examples': ["Secretion of enzymes in inactive zymogen forms (e.g., pepsinogen, trypsinogen) that are activated only in the lumen.", "The presence of a thick, alkaline mucus layer protecting the stomach and intestinal lining.", "Rapid regeneration and replacement of epithelial cells lining the digestive tract."]
        }
        self.halt()

    @Rule(Fact(query_topic='anatomy_of_respiratory_organs'))
    def rule_anatomy_of_respiratory_organs(self):
        """Identification and naming of specific structures within an organ responsible for respiration, such as the lungs or airways."""
        self.response = {
            'concept': 'Anatomy of Respiratory Organs',
            'explanation': """Identification and naming of specific structures within an organ responsible for respiration, such as the lungs or airways.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Anatomy',
            'examples': ["Trachea (windpipe)", "Bronchi (air passages to lungs)", "Alveoli (air sacs in lungs)"]
        }
        self.halt()

    @Rule(Fact(query_topic='respiratory_surface'))
    def rule_respiratory_surface(self):
        """The specific anatomical location within a respiratory system where the exchange of gases (oxygen and carbon dioxide) between the organism and its environment occurs."""
        self.response = {
            'concept': 'Respiratory Surface',
            'explanation': """The specific anatomical location within a respiratory system where the exchange of gases (oxygen and carbon dioxide) between the organism and its environment occurs.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Physiology',
            'examples': ["Alveoli in human lungs", "Gills in fish", "Moist skin of amphibians"]
        }
        self.halt()

    @Rule(Fact(query_topic='adaptations_for_efficient_gas_exchange'))
    def rule_adaptations_for_efficient_gas_exchange(self):
        """Structural and functional features of a respiratory surface that are optimized to maximize the rate of diffusion of respiratory gases (oxygen and carbon dioxide)."""
        self.response = {
            'concept': 'Adaptations for Efficient Gas Exchange',
            'explanation': """Structural and functional features of a respiratory surface that are optimized to maximize the rate of diffusion of respiratory gases (oxygen and carbon dioxide).""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Physiology',
            'examples': ["Large surface area to volume ratio (e.g., millions of alveoli).", "Thin walls (often one-cell thick) to minimize diffusion distance.", "Rich blood supply (dense capillary network) to maintain a steep concentration gradient."]
        }
        self.halt()

    @Rule(Fact(query_topic='differences_in_blood_composition_in_respiratory_vessels'))
    def rule_differences_in_blood_composition_in_respiratory_vessels(self):
        """The comparison of the concentration of gases and other substances in blood before and after it passes through a respiratory surface, illustrating the effect of gas exchange."""
        self.response = {
            'concept': 'Differences in Blood Composition in Respiratory Vessels',
            'explanation': """The comparison of the concentration of gases and other substances in blood before and after it passes through a respiratory surface, illustrating the effect of gas exchange.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory and Circulatory Systems Physiology',
            'examples': ["Blood in the pulmonary artery (entering lungs) has high CO2 and low O2.", "Blood in the pulmonary vein (leaving lungs) has low CO2 and high O2.", "Systemic arterial blood has higher oxygen content than systemic venous blood."]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_flow_to_heart_chambers'))
    def rule_blood_flow_to_heart_chambers(self):
        """Tracing the path of blood from major vessels into the various chambers of the heart, detailing the direction and destination of blood."""
        self.response = {
            'concept': 'Blood Flow to Heart Chambers',
            'explanation': """Tracing the path of blood from major vessels into the various chambers of the heart, detailing the direction and destination of blood.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System Anatomy',
            'examples': ["Pulmonary veins carry oxygenated blood to the left atrium.", "Superior vena cava carries deoxygenated blood to the right atrium.", "Inferior vena cava carries deoxygenated blood to the right atrium."]
        }
        self.halt()

    @Rule(Fact(query_topic='respiratory_infections_causing_swelling'))
    def rule_respiratory_infections_causing_swelling(self):
        """Illnesses affecting the respiratory system, typically caused by bacterial or viral pathogens, which lead to inflammation and swelling of specific respiratory structures."""
        self.response = {
            'concept': 'Respiratory Infections Causing Swelling',
            'explanation': """Illnesses affecting the respiratory system, typically caused by bacterial or viral pathogens, which lead to inflammation and swelling of specific respiratory structures.""",
            'topic': 'Biology',
            'subtopic': 'Respiratory System Diseases',
            'examples': ["Bronchitis (inflammation of the bronchi)", "Pneumonia (inflammation of the alveoli and lung tissue)", "Laryngitis (inflammation of the larynx or voice box)"]
        }
        self.halt()

    @Rule(Fact(query_topic='products_of_anaerobic_respiration_in_animals'))
    def rule_products_of_anaerobic_respiration_in_animals(self):
        """The substances produced when animal cells respire without sufficient oxygen, leading to an alternative metabolic pathway to generate a small amount of ATP."""
        self.response = {
            'concept': 'Products of Anaerobic Respiration in Animals',
            'explanation': """The substances produced when animal cells respire without sufficient oxygen, leading to an alternative metabolic pathway to generate a small amount of ATP.""",
            'topic': 'Biology',
            'subtopic': 'Cellular Respiration',
            'examples': ["Lactic acid (in muscle cells during strenuous exercise)", "Small amounts of ATP (energy currency)", "Heat"]
        }
        self.halt()

    @Rule(Fact(query_topic='substances_not_produced_by_anaerobic_respiration'))
    def rule_substances_not_produced_by_anaerobic_respiration(self):
        """Identifying compounds or processes that are not direct outcomes or characteristics of anaerobic respiration (fermentation), contrasting them with products of aerobic respiration or specific fermentation types."""
        self.response = {
            'concept': 'Substances Not Produced by Anaerobic Respiration',
            'explanation': """Identifying compounds or processes that are not direct outcomes or characteristics of anaerobic respiration (fermentation), contrasting them with products of aerobic respiration or specific fermentation types.""",
            'topic': 'Biology',
            'subtopic': 'Cellular Respiration',
            'examples': ["Large quantities of ATP (aerobic respiration yields much more)", "Water (a product of aerobic respiration's electron transport chain)", "Sustained high energy output (anaerobic is for short bursts)"]
        }
        self.halt()

    @Rule(Fact(query_topic='structural_and_functional_unit_of_the_kidney'))
    def rule_structural_and_functional_unit_of_the_kidney(self):
        """The fundamental microscopic unit within the kidney responsible for filtering blood, reabsorbing essential substances, secreting wastes, and ultimately forming urine."""
        self.response = {
            'concept': 'Structural and Functional Unit of the Kidney',
            'explanation': """The fundamental microscopic unit within the kidney responsible for filtering blood, reabsorbing essential substances, secreting wastes, and ultimately forming urine.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System Anatomy',
            'examples': ["Nephron"]
        }
        self.halt()

    @Rule(Fact(query_topic='anatomy_of_the_nephron'))
    def rule_anatomy_of_the_nephron(self):
        """Identification and naming of the distinct components that collectively form a nephron, the functional unit of the kidney."""
        self.response = {
            'concept': 'Anatomy of the Nephron',
            'explanation': """Identification and naming of the distinct components that collectively form a nephron, the functional unit of the kidney.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System Anatomy',
            'examples': ["Glomerulus", "Bowman's capsule", "Loop of Henle"]
        }
        self.halt()

    @Rule(Fact(query_topic='functions_of_nephron_parts'))
    def rule_functions_of_nephron_parts(self):
        """Describing the specific physiological processes (e.g., filtration, reabsorption, secretion) that occur in different segments of the nephron to regulate blood composition and form urine."""
        self.response = {
            'concept': 'Functions of Nephron Parts',
            'explanation': """Describing the specific physiological processes (e.g., filtration, reabsorption, secretion) that occur in different segments of the nephron to regulate blood composition and form urine.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System Physiology',
            'examples': ["Glomerular filtration (in the glomerulus and Bowman's capsule)", "Selective reabsorption of nutrients (e.g., glucose, amino acids) in the proximal convoluted tubule.", "Tubular secretion of waste products (e.g., urea, creatinine) in the distal convoluted tubule."]
        }
        self.halt()

    @Rule(Fact(query_topic='substances_reabsorbed_in_the_kidney'))
    def rule_substances_reabsorbed_in_the_kidney(self):
        """Essential substances that are selectively transported back from the filtrate in the renal tubules into the bloodstream (peritubular capillaries) to be retained by the body."""
        self.response = {
            'concept': 'Substances Reabsorbed in the Kidney',
            'explanation': """Essential substances that are selectively transported back from the filtrate in the renal tubules into the bloodstream (peritubular capillaries) to be retained by the body.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System Physiology',
            'examples': ["Glucose", "Amino acids", "Water"]
        }
        self.halt()

    @Rule(Fact(query_topic='glucosuria__glucose_in_urine__and_its_causes'))
    def rule_glucosuria__glucose_in_urine__and_its_causes(self):
        """The condition where glucose is present in the urine, which typically indicates a problem with blood glucose regulation or kidney function, most commonly diabetes mellitus."""
        self.response = {
            'concept': 'Glucosuria (Glucose in Urine) and its Causes',
            'explanation': """The condition where glucose is present in the urine, which typically indicates a problem with blood glucose regulation or kidney function, most commonly diabetes mellitus.""",
            'topic': 'Biology',
            'subtopic': 'Excretory System Diseases',
            'examples': ["Diabetes Mellitus Type 1 (insufficient insulin production)", "Diabetes Mellitus Type 2 (insulin resistance or insufficient insulin)", "Gestational Diabetes (glucose intolerance during pregnancy)"]
        }
        self.halt()

    @Rule(Fact(query_topic='chambers_of_the_human_heart'))
    def rule_chambers_of_the_human_heart(self):
        """The four distinct compartments within the human heart that receive and pump blood, maintaining the circulatory flow."""
        self.response = {
            'concept': 'Chambers of the Human Heart',
            'explanation': """The four distinct compartments within the human heart that receive and pump blood, maintaining the circulatory flow.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System Anatomy',
            'examples': ["Right Atrium", "Left Atrium", "Right Ventricle"]
        }
        self.halt()

    @Rule(Fact(query_topic='major_blood_vessels_of_the_human_circulatory_system'))
    def rule_major_blood_vessels_of_the_human_circulatory_system(self):
        """Identification of the principal arteries and veins responsible for transporting blood to and from the heart and various body organs."""
        self.response = {
            'concept': 'Major Blood Vessels of the Human Circulatory System',
            'explanation': """Identification of the principal arteries and veins responsible for transporting blood to and from the heart and various body organs.""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System Anatomy',
            'examples': ["Aorta (largest artery)", "Vena Cava (superior and inferior, largest veins)", "Pulmonary Artery (carries deoxygenated blood to lungs)"]
        }
        self.halt()

    @Rule(Fact(query_topic='glucose_storage_in_the_liver'))
    def rule_glucose_storage_in_the_liver(self):
        """The form in which excess glucose is converted and stored primarily in the liver (and muscles) to serve as a readily available energy reserve."""
        self.response = {
            'concept': 'Glucose Storage in the Liver',
            'explanation': """The form in which excess glucose is converted and stored primarily in the liver (and muscles) to serve as a readily available energy reserve.""",
            'topic': 'Biology',
            'subtopic': 'Metabolism / Endocrine System',
            'examples': ["Glycogen", "Stored also in muscle cells", "Regulated by insulin and glucagon"]
        }
        self.halt()

    @Rule(Fact(query_topic='collecting_duct'))
    def rule_collecting_duct(self):
        """ix.%dyl kd,sldj ÷\P›US® SÇõ´"""
        self.response = {
            'concept': 'Collecting duct',
            'explanation': """ix.%dyl kd,sldj ÷\P›US® SÇõ´""",
            'topic': 'Biology',
            'subtopic': 'Human Anatomy',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='blood_circulation'))
    def rule_blood_circulation(self):
        """reêr ixirKh _¸v _Ø÷Óõõmh®"""
        self.response = {
            'concept': 'Blood circulation',
            'explanation': """reêr ixirKh _¸v _Ø÷Óõõmh®""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='blood_corpuscles'))
    def rule_blood_corpuscles(self):
        """foaydKqq S¸vU P»[PÒ"""
        self.response = {
            'concept': 'Blood corpuscles',
            'explanation': """foaydKqq S¸vU P»[PÒ""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': ["Red blood corpuscle", "Granulocytes", "Non-granulocytes"]
        }
        self.halt()

    @Rule(Fact(query_topic='blood_plasma'))
    def rule_blood_plasma(self):
        """reêr ma,diauh S¸v vµÁÂøÇ¯®"""
        self.response = {
            'concept': 'Blood plasma',
            'explanation': """reêr ma,diauh S¸v vµÁÂøÇ¯®""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='red_blood_corpuscle'))
    def rule_red_blood_corpuscle(self):
        """r;= reêrdKq ö\[S¸vU P»® lKslduh ]Ö©o öPõsh"""
        self.response = {
            'concept': 'Red blood corpuscle',
            'explanation': """r;= reêrdKq ö\[S¸vU P»® lKslduh ]Ö©o öPõsh""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='granulocytes'))
    def rule_granulocytes(self):
        """iqÿ reêrdKqq öÁsSÈ¯®"""
        self.response = {
            'concept': 'Granulocytes',
            'explanation': """iqÿ reêrdKqq öÁsSÈ¯®""",
            'topic': 'Biology',
            'subtopic': 'Blood Components',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='non_granulocytes'))
    def rule_non_granulocytes(self):
        """lKslduh fkdjk iqÿ ]Ö©o¯ØÓ öÁs reêrdKqq SÈ¯®"""
        self.response = {
            'concept': 'Non-granulocytes',
            'explanation': """lKslduh fkdjk iqÿ ]Ö©o¯ØÓ öÁs reêrdKqq SÈ¯®""",
            'topic': 'Biology',
            'subtopic': 'Blood Components',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='atrium'))
    def rule_atrium(self):
        """l¾Ksldj Cu¯ÁøÓ"""
        self.response = {
            'concept': 'Atrium',
            'explanation': """l¾Ksldj Cu¯ÁøÓ""",
            'topic': 'Biology',
            'subtopic': 'Heart Anatomy',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='ventricle'))
    def rule_ventricle(self):
        """fldaIsldj ÷\õøn¯øÓ"""
        self.response = {
            'concept': 'Ventricle',
            'explanation': """fldaIsldj ÷\õøn¯øÓ""",
            'topic': 'Biology',
            'subtopic': 'Heart Anatomy',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='bicuspid_valve'))
    def rule_bicuspid_valve(self):
        """oaú;=Kav lmdgh C¸Tº ÁõÀÄ"""
        self.response = {
            'concept': 'Bicuspid valve',
            'explanation': """oaú;=Kav lmdgh C¸Tº ÁõÀÄ""",
            'topic': 'Biology',
            'subtopic': 'Heart Anatomy',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='pulmonary_vein'))
    def rule_pulmonary_vein(self):
        """mqmaMqYSh Ysrdj ~øµ±µÀ |õÍ®"""
        self.response = {
            'concept': 'Pulmonary vein',
            'explanation': """mqmaMqYSh Ysrdj ~øµ±µÀ |õÍ®""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='pulmonary_circulation'))
    def rule_pulmonary_circulation(self):
        """mqmamqYSh ixirKh ~øµ±µÀ _Ø÷Óõmh®"""
        self.response = {
            'concept': 'Pulmonary circulation',
            'explanation': """mqmamqYSh ixirKh ~øµ±µÀ _Ø÷Óõmh®""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='lymphatic_system'))
    def rule_lymphatic_system(self):
        """jid moaO;sh {n}ºz öuõSv"""
        self.response = {
            'concept': 'Lymphatic system',
            'explanation': """jid moaO;sh {n}ºz öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Immune System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='systemic_circulation'))
    def rule_systemic_circulation(self):
        """ixia:dksl ixirKh öuõSv _Ø÷Óõmh®"""
        self.response = {
            'concept': 'Systemic circulation',
            'explanation': """ixia:dksl ixirKh öuõSv _Ø÷Óõmh®""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='blood_capillaries'))
    def rule_blood_capillaries(self):
        """reêr flaYkd,sld S¸v ©°ºxøÍU SÇõ´"""
        self.response = {
            'concept': 'Blood capillaries',
            'explanation': """reêr flaYkd,sld S¸v ©°ºxøÍU SÇõ´""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='systemic_artery'))
    def rule_systemic_artery(self):
        """ixia:dksl Ouksh öuõSv¨ ö£¸|õi"""
        self.response = {
            'concept': 'Systemic artery',
            'explanation': """ixia:dksl Ouksh öuõSv¨ ö£¸|õi""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='arterial_system'))
    def rule_arterial_system(self):
        """Ouks moaO;sh |õiz öuõSv"""
        self.response = {
            'concept': 'Arterial system',
            'explanation': """Ouks moaO;sh |õiz öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='venous_system'))
    def rule_venous_system(self):
        """Ysrd moaO;sh |õÍzöuõSv"""
        self.response = {
            'concept': 'Venous system',
            'explanation': """Ysrd moaO;sh |õÍzöuõSv""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='coronary_thrombosis'))
    def rule_coronary_thrombosis(self):
        """lsÍgl f;%dïfndaish •i²¸ xöµõ®÷£õ]ì"""
        self.response = {
            'concept': 'Coronary thrombosis',
            'explanation': """lsÍgl f;%dïfndaish •i²¸ xöµõ®÷£õ]ì""",
            'topic': 'Biology',
            'subtopic': 'Circulatory System Disorders',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='co_ordination'))
    def rule_co_ordination(self):
        """iudfhdackh Cø¯£õUP®"""
        self.response = {
            'concept': 'Co-ordination',
            'explanation': """iudfhdackh Cø¯£õUP®""",
            'topic': 'Biology',
            'subtopic': 'General Biology',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='homeostasis'))
    def rule_homeostasis(self):
        """iuiaÓ;sh J¸^ºzvh{ø»"""
        self.response = {
            'concept': 'Homeostasis',
            'explanation': """iuiaÓ;sh J¸^ºzvh{ø»""",
            'topic': 'Biology',
            'subtopic': 'General Biology',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='reflex_arc'))
    def rule_reflex_arc(self):
        """m%;Sl pdmh öuÔ¨¦ ÂÀ"""
        self.response = {
            'concept': 'Reflex arc',
            'explanation': """m%;Sl pdmh öuÔ¨¦ ÂÀ""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='reflex_actions'))
    def rule_reflex_actions(self):
        """m%;Sl l%shd öuÔÂøÚ"""
        self.response = {
            'concept': 'Reflex actions',
            'explanation': """m%;Sl l%shd öuÔÂøÚ""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='central_nervous_system'))
    def rule_central_nervous_system(self):
        """uOH iakdhq moaO;sh ø©¯ |µ®¦z öuõSv"""
        self.response = {
            'concept': 'Central nervous system',
            'explanation': """uOH iakdhq moaO;sh ø©¯ |µ®¦z öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='autonomic_nervous_system'))
    def rule_autonomic_nervous_system(self):
        """iajhx idOl ußÚõm] |µ®¦z iakdhq moaO;sh öuõSv m%;Hdkqfõ.S"""
        self.response = {
            'concept': 'Autonomic nervous system',
            'explanation': """iajhx idOl ußÚõm] |µ®¦z iakdhq moaO;sh öuõSv m%;Hdkqfõ.S""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='parasympathetic_system'))
    def rule_parasympathetic_system(self):
        """£µõ£›Ä |µ®¦z iakdhq moaO;sh öuõSv"""
        self.response = {
            'concept': 'Parasympathetic system',
            'explanation': """£µõ£›Ä |µ®¦z iakdhq moaO;sh öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='sympathetic_system'))
    def rule_sympathetic_system(self):
        """wkqfõ.S iakdhq moaO;sh £›Ä |µ®¦z öuõSv"""
        self.response = {
            'concept': 'Sympathetic system',
            'explanation': """wkqfõ.S iakdhq moaO;sh £›Ä |µ®¦z öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Nervous System',
            'examples': []
        }
        self.halt()

    @Rule(Fact(query_topic='endocrine_system'))
    def rule_endocrine_system(self):
        """wka;rdi¾. moaO;sh APg_µUS¢ öuõSv"""
        self.response = {
            'concept': 'Endocrine system',
            'explanation': """wka;rdi¾. moaO;sh APg_µUS¢ öuõSv""",
            'topic': 'Biology',
            'subtopic': 'Endocrine System',
            'examples': []
        }
        self.halt()

