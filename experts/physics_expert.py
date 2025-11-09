"""
Physics Expert System
--------------------
Traditional Experta rule-based expert system for O/L Physics topics.
Comprehensive knowledge base integrated from textbook.
"""

from experta import *


class PhysicsExpert(KnowledgeEngine):
    """
    Expert system for Physics questions using traditional @Rule format.
    
    Topics covered (comprehensive):
    - Waves and Sound
    - Light and Optics
    - Forces and Motion
    - Energy
    - Electricity
    - And many more O/L Physics topics from the complete textbook knowledge base
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
    
    @Rule(Fact(query_topic='forces'))
    def rule_forces(self):
        """Forces cause objects to accelerate."""

    # ==================== COMPREHENSIVE KNOWLEDGE BASE RULES ====================
    # Integrated from textbook knowledge base

    @Rule(Fact(query_topic='formation_of_ripples'))
    def rule_formation_of_ripples(self):
        """Ripples are disturbances that form and spread across a surface, typically originating from a point of impact or perturbation. These disturbances propagate outwards, often in a circular pattern from the source."""
        self.response = {
            'concept': 'Formation of Ripples',
            'explanation': """Ripples are disturbances that form and spread across a surface, typically originating from a point of impact or perturbation. These disturbances propagate outwards, often in a circular pattern from the source.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Ripples formed when a pebble is dropped onto a still water surface.", "Ripples forming in a horizontally held rope when shaken up and down."]
        }
        self.halt()

    @Rule(Fact(query_topic='wave__definition_'))
    def rule_wave__definition_(self):
        """A wave is a disturbance that propagates through a medium or space. It is characterized by the transmission of energy without the permanent displacement of the medium's substance."""
        self.response = {
            'concept': 'Wave (Definition)',
            'explanation': """A wave is a disturbance that propagates through a medium or space. It is characterized by the transmission of energy without the permanent displacement of the medium's substance.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["The disturbance spreading over a water surface after a pebble drop.", "The disturbance traveling along a rope when shaken.", "Water waves carrying energy to a plastic ball on the water surface."]
        }
        self.halt()

    @Rule(Fact(query_topic='energy_transmission_by_waves'))
    def rule_energy_transmission_by_waves(self):
        """A fundamental property of waves is their ability to carry and transmit energy from one point to another. Crucially, this energy transmission occurs without the physical substance of the medium being transmitted between the points; instead, the particles of the medium typically oscillate around their fixed positions."""
        self.response = {
            'concept': 'Energy Transmission by Waves',
            'explanation': """A fundamental property of waves is their ability to carry and transmit energy from one point to another. Crucially, this energy transmission occurs without the physical substance of the medium being transmitted between the points; instead, the particles of the medium typically oscillate around their fixed positions.""",
            'topic': 'Physics',
            'subtopic': 'Properties of Waves',
            'examples': ["A plastic ball moving up and down on a water surface due to passing waves, indicating energy transfer to the ball.", "Water particles at each point moving up and down as a water wave travels, but not moving horizontally with the wave itself."]
        }
        self.halt()

    @Rule(Fact(query_topic='wave_motion'))
    def rule_wave_motion(self):
        """The process by which energy is transmitted through a medium or space in the form of waves, where the particles of the medium oscillate but do not travel along with the wave itself."""
        self.response = {
            'concept': 'Wave Motion',
            'explanation': """The process by which energy is transmitted through a medium or space in the form of waves, where the particles of the medium oscillate but do not travel along with the wave itself.""",
            'topic': 'Physics',
            'subtopic': 'Fundamentals of Waves',
            'examples': ["Water waves moving across the surface of water", "Waves propagating along a stretched rope", "Sound waves traveling through air"]
        }
        self.halt()

    @Rule(Fact(query_topic='medium_for_wave_propagation'))
    def rule_medium_for_wave_propagation(self):
        """The substance or material through which waves propagate, allowing for the transmission of energy. The particles of this medium transmit energy even though they do not travel along with the wave."""
        self.response = {
            'concept': 'Medium for Wave Propagation',
            'explanation': """The substance or material through which waves propagate, allowing for the transmission of energy. The particles of this medium transmit energy even though they do not travel along with the wave.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["Water is the medium for water waves", "The material of a rope is the medium for waves along it", "Air is the medium for sound waves"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_waves'))
    def rule_mechanical_waves(self):
        """Waves that require a material medium (such as solids, liquids, or gases) for their propagation. Energy is transmitted through the vibration and interaction of the medium's particles."""
        self.response = {
            'concept': 'Mechanical Waves',
            'explanation': """Waves that require a material medium (such as solids, liquids, or gases) for their propagation. Energy is transmitted through the vibration and interaction of the medium's particles.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["Water waves", "Waves propagating along a slinky", "Sound waves through air, liquids, or solids"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_waves'))
    def rule_electromagnetic_waves(self):
        """Waves that do not require a material medium for their propagation and can travel through empty space or a vacuum. They are responsible for transmitting energy over vast distances."""
        self.response = {
            'concept': 'Electromagnetic Waves',
            'explanation': """Waves that do not require a material medium for their propagation and can travel through empty space or a vacuum. They are responsible for transmitting energy over vast distances.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["Light from the sun", "Heat from the sun", "Radio waves"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_waves'))
    def rule_mechanical_waves(self):
        """Mechanical waves are waves that require a material medium for their propagation. The movement and participation of the particles within that medium are essential for the wave to travel."""
        self.response = {
            'concept': 'Mechanical Waves',
            'explanation': """Mechanical waves are waves that require a material medium for their propagation. The movement and participation of the particles within that medium are essential for the wave to travel.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Waves formed on water surfaces", "Sound waves that travel in air", "Waves formed on a guitar string when it is plucked"]
        }
        self.halt()

    @Rule(Fact(query_topic='categories_of_mechanical_waves'))
    def rule_categories_of_mechanical_waves(self):
        """Mechanical waves are categorized into two main types based on the relationship between the direction of motion of the medium's particles and the direction of the wave's propagation."""
        self.response = {
            'concept': 'Categories of Mechanical Waves',
            'explanation': """Mechanical waves are categorized into two main types based on the relationship between the direction of motion of the medium's particles and the direction of the wave's propagation.""",
            'topic': 'Physics',
            'subtopic': 'Mechanical Waves',
            'examples': ["Transverse waves", "Longitudinal waves"]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_waves'))
    def rule_transverse_waves(self):
        """Transverse waves are a type of mechanical wave where the propagation of the wave is in a direction perpendicular to the direction in which the particles of the medium move."""
        self.response = {
            'concept': 'Transverse Waves',
            'explanation': """Transverse waves are a type of mechanical wave where the propagation of the wave is in a direction perpendicular to the direction in which the particles of the medium move.""",
            'topic': 'Physics',
            'subtopic': 'Mechanical Waves',
            'examples': ["Waves formed on a slinky when shaken side-to-side, where the wave travels along the slinky but the ribbons move perpendicular to it", "Water waves generated by dropping an object into still water, where water particles move up and down while the wave travels horizontally"]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_waves'))
    def rule_transverse_waves(self):
        """Waves where the particles of the medium move in a direction perpendicular to the direction of the wave propagation. The water particles move up and down while the waves spread in a perpendicular direction."""
        self.response = {
            'concept': 'Transverse Waves',
            'explanation': """Waves where the particles of the medium move in a direction perpendicular to the direction of the wave propagation. The water particles move up and down while the waves spread in a perpendicular direction.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Waves that travel on the water surface", "Waves formed by shaking one end of a string up and down"]
        }
        self.halt()

    @Rule(Fact(query_topic='crest'))
    def rule_crest(self):
        """Points in a wave where the particles have traveled the maximum distance in the upward direction."""
        self.response = {
            'concept': 'Crest',
            'explanation': """Points in a wave where the particles have traveled the maximum distance in the upward direction.""",
            'topic': 'Physics',
            'subtopic': 'Transverse Waves',
            'examples': ["Points A and B in the cross section of a water wave (Figure 4.7)"]
        }
        self.halt()

    @Rule(Fact(query_topic='trough'))
    def rule_trough(self):
        """Points in a wave where the particles have traveled the maximum distance in the downward direction."""
        self.response = {
            'concept': 'Trough',
            'explanation': """Points in a wave where the particles have traveled the maximum distance in the downward direction.""",
            'topic': 'Physics',
            'subtopic': 'Transverse Waves',
            'examples': ["Points C and D in the cross section of a water wave (Figure 4.7)"]
        }
        self.halt()

    @Rule(Fact(query_topic='longitudinal_waves'))
    def rule_longitudinal_waves(self):
        """Waves demonstrated using a slinky, where moving one end forward causes coils to bunch up (compression) and pulling it back causes coils to stretch out (rarefaction). In these waves, the particles of the medium move in the same direction as the wave propagation (as shown in Figure 4.9)."""
        self.response = {
            'concept': 'Longitudinal Waves',
            'explanation': """Waves demonstrated using a slinky, where moving one end forward causes coils to bunch up (compression) and pulling it back causes coils to stretch out (rarefaction). In these waves, the particles of the medium move in the same direction as the wave propagation (as shown in Figure 4.9).""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Waves formed by moving a slinky forward and backward"]
        }
        self.halt()

    @Rule(Fact(query_topic='compression'))
    def rule_compression(self):
        """In a longitudinal wave, when the free end of a slinky is pushed forward, the coils near that end are bunched up."""
        self.response = {
            'concept': 'Compression',
            'explanation': """In a longitudinal wave, when the free end of a slinky is pushed forward, the coils near that end are bunched up.""",
            'topic': 'Physics',
            'subtopic': 'Longitudinal Waves',
            'examples': ["The bunched-up coils in a slinky when its free end is pushed forward"]
        }
        self.halt()

    @Rule(Fact(query_topic='rarefaction'))
    def rule_rarefaction(self):
        """In a longitudinal wave, when the free end of a slinky is pulled back, the coils will stretch-out."""
        self.response = {
            'concept': 'Rarefaction',
            'explanation': """In a longitudinal wave, when the free end of a slinky is pulled back, the coils will stretch-out.""",
            'topic': 'Physics',
            'subtopic': 'Longitudinal Waves',
            'examples': ["The stretched-out coils in a slinky when its free end is pulled back"]
        }
        self.halt()

    @Rule(Fact(query_topic='compressions'))
    def rule_compressions(self):
        """Regions formed in a medium (like a slinky) when it is pushed forward, causing particles to momentarily crowd together or experience higher density."""
        self.response = {
            'concept': 'Compressions',
            'explanation': """Regions formed in a medium (like a slinky) when it is pushed forward, causing particles to momentarily crowd together or experience higher density.""",
            'topic': 'Physics',
            'subtopic': 'Longitudinal Waves',
            'examples': ["Compressions formed in a slinky when pushed forward", "Regions of higher pressure in a sound wave", "Areas where particles are closest in a longitudinal wave"]
        }
        self.halt()

    @Rule(Fact(query_topic='rarefactions'))
    def rule_rarefactions(self):
        """Regions formed in a medium (like a slinky) when the free end is moved backward, causing particles to momentarily spread apart or experience lower density."""
        self.response = {
            'concept': 'Rarefactions',
            'explanation': """Regions formed in a medium (like a slinky) when the free end is moved backward, causing particles to momentarily spread apart or experience lower density.""",
            'topic': 'Physics',
            'subtopic': 'Longitudinal Waves',
            'examples': ["Rarefactions formed in a slinky when moved backward", "Regions of lower pressure in a sound wave", "Areas where particles are furthest apart in a longitudinal wave"]
        }
        self.halt()

    @Rule(Fact(query_topic='longitudinal_waves'))
    def rule_longitudinal_waves(self):
        """Waves in which the particles of the medium oscillate parallel to the direction of wave propagation. These waves can propagate through solids, liquids, and gases."""
        self.response = {
            'concept': 'Longitudinal Waves',
            'explanation': """Waves in which the particles of the medium oscillate parallel to the direction of wave propagation. These waves can propagate through solids, liquids, and gases.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["Waves formed in the slinky in the activity", "Sound waves generated in air", "Waves propagating through a stretched spring"]
        }
        self.halt()

    @Rule(Fact(query_topic='vibrations'))
    def rule_vibrations(self):
        """The back and forth motions of an object or a part of an object, which can generate waves."""
        self.response = {
            'concept': 'Vibrations',
            'explanation': """The back and forth motions of an object or a part of an object, which can generate waves.""",
            'topic': 'Physics',
            'subtopic': 'Wave Generation',
            'examples': ["The back and forth motions of a tuning fork's arms", "A plucked guitar string", "A buzzing phone"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_waves'))
    def rule_sound_waves(self):
        """Longitudinal waves that cause the sensation of hearing, typically generated by vibrations."""
        self.response = {
            'concept': 'Sound Waves',
            'explanation': """Longitudinal waves that cause the sensation of hearing, typically generated by vibrations.""",
            'topic': 'Physics',
            'subtopic': 'Acoustics',
            'examples': ["Waves generated by a tuning fork that we hear", "Human speech", "Music played through a speaker"]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_waves'))
    def rule_transverse_waves(self):
        """Waves in which the particles of the medium move perpendicular to the direction of wave propagation. They propagate along the surfaces of solids and liquids or along strings, wires, etc."""
        self.response = {
            'concept': 'Transverse Waves',
            'explanation': """Waves in which the particles of the medium move perpendicular to the direction of wave propagation. They propagate along the surfaces of solids and liquids or along strings, wires, etc.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["Water waves", "Waves on a stretched string", "Waves in a vibrating rope"]
        }
        self.halt()

    @Rule(Fact(query_topic='waves'))
    def rule_waves(self):
        """Disturbances that spread from one point to another, exhibiting variations that depend on both time and distance."""
        self.response = {
            'concept': 'Waves',
            'explanation': """Disturbances that spread from one point to another, exhibiting variations that depend on both time and distance.""",
            'topic': 'Physics',
            'subtopic': 'Fundamental Concepts',
            'examples': ["Ocean waves", "Sound propagating through a room", "Light traveling through space"]
        }
        self.halt()

    @Rule(Fact(query_topic='sinusoidal_waves'))
    def rule_sinusoidal_waves(self):
        """A very simple form of wave where the displacement of particles from their central position varies smoothly over time and distance, following a sine or cosine function."""
        self.response = {
            'concept': 'Sinusoidal Waves',
            'explanation': """A very simple form of wave where the displacement of particles from their central position varies smoothly over time and distance, following a sine or cosine function.""",
            'topic': 'Physics',
            'subtopic': 'Wave Forms',
            'examples': ["An idealized graph of wave displacement over time", "A pure tone sound wave", "A single-frequency light wave"]
        }
        self.halt()

    @Rule(Fact(query_topic='one_oscillation'))
    def rule_one_oscillation(self):
        """The complete motion of a particle from time t0 (where displacement is zero), increasing to a maximum positive value at t1, decreasing to zero at t2, increasing in the negative direction to a maximum negative value at t3, and finally becoming zero again at t4. This motion from t0 to t4 constitutes one complete cycle."""
        self.response = {
            'concept': 'One Oscillation',
            'explanation': """The complete motion of a particle from time t0 (where displacement is zero), increasing to a maximum positive value at t1, decreasing to zero at t2, increasing in the negative direction to a maximum negative value at t3, and finally becoming zero again at t4. This motion from t0 to t4 constitutes one complete cycle.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The motion of the particle from t0 to t4 as shown in Figure 4.10.", "A full swing of a pendulum from one side, across its equilibrium, to the other side, and back to the starting side.", "One complete up-and-down movement of a floating object on water."]
        }
        self.halt()

    @Rule(Fact(query_topic='oscillation__general_'))
    def rule_oscillation__general_(self):
        """A general term used to describe the repetitive motion of a particle or system about an equilibrium position. If this motion is slow, it is specifically called an oscillation."""
        self.response = {
            'concept': 'Oscillation (General)',
            'explanation': """A general term used to describe the repetitive motion of a particle or system about an equilibrium position. If this motion is slow, it is specifically called an oscillation.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["A slow pendulum swing.", "The rhythmic sway of a tall building in a gentle breeze.", "The slow movement of a particle in a wave with a long period."]
        }
        self.halt()

    @Rule(Fact(query_topic='vibration'))
    def rule_vibration(self):
        """A term also used to describe repetitive motions similar to oscillations. If this motion is fast, it is called a vibration."""
        self.response = {
            'concept': 'Vibration',
            'explanation': """A term also used to describe repetitive motions similar to oscillations. If this motion is fast, it is called a vibration.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["A rapidly vibrating guitar string.", "The fast movement of a loudspeaker cone to produce sound.", "A quickly shaking object due to high-frequency waves."]
        }
        self.halt()

    @Rule(Fact(query_topic='crest'))
    def rule_crest(self):
        """The point of maximum positive displacement from the central (equilibrium) position in a wave, where the particle takes a maximum positive value."""
        self.response = {
            'concept': 'Crest',
            'explanation': """The point of maximum positive displacement from the central (equilibrium) position in a wave, where the particle takes a maximum positive value.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The highest point of a water wave.", "The peak shown in Figure 4.10 at time t1.", "The highest point on the graph of displacement versus distance in Figure 4.11."]
        }
        self.halt()

    @Rule(Fact(query_topic='trough'))
    def rule_trough(self):
        """The point of maximum negative displacement from the central (equilibrium) position in a wave, where the particle takes a maximum negative value."""
        self.response = {
            'concept': 'Trough',
            'explanation': """The point of maximum negative displacement from the central (equilibrium) position in a wave, where the particle takes a maximum negative value.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The lowest point of a water wave.", "The lowest point shown in Figure 4.10 at time t3.", "The lowest point on the graph of displacement versus distance in Figure 4.11."]
        }
        self.halt()

    @Rule(Fact(query_topic='period__t_'))
    def rule_period__t_(self):
        """The time taken for one complete oscillation of a particle. It represents the duration for the particle's motion to complete one full cycle from t0 to t4."""
        self.response = {
            'concept': 'Period (T)',
            'explanation': """The time taken for one complete oscillation of a particle. It represents the duration for the particle's motion to complete one full cycle from t0 to t4.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The time T labeled in Figure 4.10.", "The time it takes for a wave crest to pass a fixed point and be followed by the next crest.", "The duration of a complete back-and-forth swing of a pendulum."]
        }
        self.halt()

    @Rule(Fact(query_topic='amplitude_of_a_wave'))
    def rule_amplitude_of_a_wave(self):
        """The maximum displacement of a particle from its central or equilibrium position. It is the magnitude of the maximum positive or negative displacement reached during an oscillation."""
        self.response = {
            'concept': 'Amplitude of a Wave',
            'explanation': """The maximum displacement of a particle from its central or equilibrium position. It is the magnitude of the maximum positive or negative displacement reached during an oscillation.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The maximum 'a' value indicated in Figure 4.10 and Figure 4.11.", "The height of a wave crest measured from the equilibrium line.", "The maximum extent of a particle's movement from its rest position."]
        }
        self.halt()

    @Rule(Fact(query_topic='wavelength__λ_'))
    def rule_wavelength__λ_(self):
        """The spatial distance over which a wave's shape repeats at a given moment. It is typically measured as the distance between two consecutive corresponding points on a wave, such as two successive crests or troughs."""
        self.response = {
            'concept': 'Wavelength (λ)',
            'explanation': """The spatial distance over which a wave's shape repeats at a given moment. It is typically measured as the distance between two consecutive corresponding points on a wave, such as two successive crests or troughs.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The distance 'λ' indicated in Figure 4.11.", "The distance between two adjacent crests in a transverse wave.", "The length of one complete wave cycle in space."]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_wave'))
    def rule_transverse_wave(self):
        """A type of wave where the displacement of the particles of the medium is perpendicular to the direction of wave propagation. The visible shape of such a wave corresponds to a graph of particle displacement with distance from the source."""
        self.response = {
            'concept': 'Transverse Wave',
            'explanation': """A type of wave where the displacement of the particles of the medium is perpendicular to the direction of wave propagation. The visible shape of such a wave corresponds to a graph of particle displacement with distance from the source.""",
            'topic': 'Physics',
            'subtopic': 'Types of Waves',
            'examples': ["Waves traveling along a string (as shown in Figure 4.8).", "Electromagnetic waves, such as light.", "Water waves on the surface of a pond."]
        }
        self.halt()

    @Rule(Fact(query_topic='longitudinal_wave'))
    def rule_longitudinal_wave(self):
        """A type of wave where the displacement of the particles of the medium occurs in the same direction as the direction of wave propagation. While its form cannot be directly seen like a transverse wave, its displacement variation with distance can be measured and plotted."""
        self.response = {
            'concept': 'Longitudinal Wave',
            'explanation': """A type of wave where the displacement of the particles of the medium occurs in the same direction as the direction of wave propagation. While its form cannot be directly seen like a transverse wave, its displacement variation with distance can be measured and plotted.""",
            'topic': 'Physics',
            'subtopic': 'Types of Waves',
            'examples': ["Sound waves traveling through air.", "Waves created by pushing and pulling a Slinky toy along its length.", "Pressure waves in a fluid."]
        }
        self.halt()

    @Rule(Fact(query_topic='amplitude'))
    def rule_amplitude(self):
        """The maximum displacement shown by the particles taking part in the wave motion is known as the amplitude of the wave."""
        self.response = {
            'concept': 'Amplitude',
            'explanation': """The maximum displacement shown by the particles taking part in the wave motion is known as the amplitude of the wave.""",
            'topic': 'Physics',
            'subtopic': 'Wave Properties',
            'examples': ["Maximum displacement from the equilibrium position", "Height of a crest from the equilibrium", "Depth of a trough from the equilibrium"]
        }
        self.halt()

    @Rule(Fact(query_topic='wavelength__λ_'))
    def rule_wavelength__λ_(self):
        """The distance between one particle and the closest next particle taking part in the wave motion having the same state of motion is known as the wavelength (λ) of the wave. This is equivalent to the distance between two consecutive troughs or crests."""
        self.response = {
            'concept': 'Wavelength (λ)',
            'explanation': """The distance between one particle and the closest next particle taking part in the wave motion having the same state of motion is known as the wavelength (λ) of the wave. This is equivalent to the distance between two consecutive troughs or crests.""",
            'topic': 'Physics',
            'subtopic': 'Wave Properties',
            'examples': ["Distance between two consecutive crests", "Distance between two consecutive troughs", "Distance between two adjacent particles in the same state of motion"]
        }
        self.halt()

    @Rule(Fact(query_topic='period__t_'))
    def rule_period__t_(self):
        """The time taken by a particle for a complete oscillation is known as the period (T). It is also the time taken by a wave to travel a distance equal to one wavelength."""
        self.response = {
            'concept': 'Period (T)',
            'explanation': """The time taken by a particle for a complete oscillation is known as the period (T). It is also the time taken by a wave to travel a distance equal to one wavelength.""",
            'topic': 'Physics',
            'subtopic': 'Wave Properties',
            'examples': ["Time for one complete oscillation of a particle", "Time for a wave to travel one wavelength", "Measured in seconds (s)"]
        }
        self.halt()

    @Rule(Fact(query_topic='frequency__f_'))
    def rule_frequency__f_(self):
        """The number of oscillations carried out by a particle in a unit time is known as the frequency (f). Frequency is equal to the reciprocal of the period (f = 1/T). The unit used to measure frequency is Hertz (Hz), where one Hertz is defined as one oscillation per second."""
        self.response = {
            'concept': 'Frequency (f)',
            'explanation': """The number of oscillations carried out by a particle in a unit time is known as the frequency (f). Frequency is equal to the reciprocal of the period (f = 1/T). The unit used to measure frequency is Hertz (Hz), where one Hertz is defined as one oscillation per second.""",
            'topic': 'Physics',
            'subtopic': 'Wave Properties',
            'examples': ["Number of oscillations per second", "Reciprocal of the period (1/T)", "Measured in Hertz (Hz)"]
        }
        self.halt()

    @Rule(Fact(query_topic='wave_speed__v_'))
    def rule_wave_speed__v_(self):
        """A wave travels a distance equal to the wavelength (λ) in a time interval equal to the period (T). Therefore, its speed is given by the formulas v = λ/T or v = fλ."""
        self.response = {
            'concept': 'Wave Speed (v)',
            'explanation': """A wave travels a distance equal to the wavelength (λ) in a time interval equal to the period (T). Therefore, its speed is given by the formulas v = λ/T or v = fλ.""",
            'topic': 'Physics',
            'subtopic': 'Wave Properties',
            'examples': ["v = λ / T", "v = f × λ", "Measured in meters per second (m s⁻¹)"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_waves'))
    def rule_electromagnetic_waves(self):
        """Electromagnetic waves do not require the participation of material particles of a medium for their propagation. They consist of oscillating electric fields and magnetic fields."""
        self.response = {
            'concept': 'Electromagnetic Waves',
            'explanation': """Electromagnetic waves do not require the participation of material particles of a medium for their propagation. They consist of oscillating electric fields and magnetic fields.""",
            'topic': 'Physics',
            'subtopic': 'Types of Waves',
            'examples': ["Radio waves", "Do not require a medium to propagate", "Composed of oscillating electric and magnetic fields"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_wave_propagation_direction'))
    def rule_electromagnetic_wave_propagation_direction(self):
        """Electromagnetic waves propagate in a direction perpendicular to the directions of both the electric and magnetic fields, which are themselves perpendicular to each other."""
        self.response = {
            'concept': 'Electromagnetic Wave Propagation Direction',
            'explanation': """Electromagnetic waves propagate in a direction perpendicular to the directions of both the electric and magnetic fields, which are themselves perpendicular to each other.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Waves',
            'examples': ["If the electric field oscillates along the y-axis and the magnetic field along the z-axis, the wave propagates along the x-axis.", "Figure 4.12 visually represents the perpendicular orientation of the fields and the wave's direction of travel.", "A vertically polarized radio wave traveling horizontally has its magnetic field oscillating horizontally perpendicular to the direction of propagation."]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_waves_as_transverse_waves'))
    def rule_electromagnetic_waves_as_transverse_waves(self):
        """Because the direction of propagation is perpendicular to the oscillations of the electric and magnetic fields, electromagnetic waves are classified as transverse waves."""
        self.response = {
            'concept': 'Electromagnetic Waves as Transverse Waves',
            'explanation': """Because the direction of propagation is perpendicular to the oscillations of the electric and magnetic fields, electromagnetic waves are classified as transverse waves.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["Light waves are a common example of transverse electromagnetic waves.", "Radio waves also exhibit transverse wave characteristics, with field oscillations perpendicular to their direction of travel.", "Unlike sound waves, which are longitudinal, EM waves do not require a medium to oscillate in the direction of propagation."]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_electromagnetic_waves_in_vacuum'))
    def rule_speed_of_electromagnetic_waves_in_vacuum(self):
        """All electromagnetic waves propagate at a constant speed of approximately 2.988 × 10^8 m/s in a vacuum. For practical calculations, this speed is often rounded to 3 × 10^8 m/s."""
        self.response = {
            'concept': 'Speed of Electromagnetic Waves in Vacuum',
            'explanation': """All electromagnetic waves propagate at a constant speed of approximately 2.988 × 10^8 m/s in a vacuum. For practical calculations, this speed is often rounded to 3 × 10^8 m/s.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Wave Properties',
            'examples': ["The speed of light in outer space is precisely 3 × 10^8 m/s.", "Gamma rays, despite their high energy, travel at the same speed as radio waves in a vacuum.", "This constant speed in vacuum is a fundamental property for all parts of the electromagnetic spectrum."]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_electromagnetic_waves_in_material_media'))
    def rule_speed_of_electromagnetic_waves_in_material_media(self):
        """The speed of electromagnetic waves decreases when they travel through material media compared to their speed in a vacuum. Consequently, their wavelength also changes when entering a medium."""
        self.response = {
            'concept': 'Speed of Electromagnetic Waves in Material Media',
            'explanation': """The speed of electromagnetic waves decreases when they travel through material media compared to their speed in a vacuum. Consequently, their wavelength also changes when entering a medium.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Wave Properties',
            'examples': ["Light slows down significantly when it enters water or glass from the air.", "Radio waves travel at a slightly reduced speed through the Earth's atmosphere.", "Fiber optic cables guide light, but the light travels slower within the glass fibers than it would in a vacuum."]
        }
        self.halt()

    @Rule(Fact(query_topic='relationship_between_speed__frequency__and_wavelength_for_electromagnetic_waves'))
    def rule_relationship_between_speed__frequency__and_wavelength_for_electromagnetic_waves(self):
        """The speed (c) of an electromagnetic wave is determined by the product of its frequency (f) and its wavelength (λ), given by the relationship: c = fλ."""
        self.response = {
            'concept': 'Relationship between Speed, Frequency, and Wavelength for Electromagnetic Waves',
            'explanation': """The speed (c) of an electromagnetic wave is determined by the product of its frequency (f) and its wavelength (λ), given by the relationship: c = fλ.""",
            'topic': 'Physics',
            'subtopic': 'Wave Equation',
            'examples': ["To find the wavelength of a 100 MHz radio wave, one can use the formula c = fλ with c = 3 × 10^8 m/s.", "Given the speed of light and its wavelength (e.g., for green light), its frequency can be calculated.", "This fundamental equation applies to all forms of electromagnetic radiation, from gamma rays to radio waves."]
        }
        self.halt()

    @Rule(Fact(query_topic='general_characteristics_of_electromagnetic_waves'))
    def rule_general_characteristics_of_electromagnetic_waves(self):
        """Electromagnetic waves possess several key characteristics: they are not affected by external electric or magnetic fields, they do not require a material medium for propagation, and they travel at a speed of 3 × 10^8 m/s in a vacuum."""
        self.response = {
            'concept': 'General Characteristics of Electromagnetic Waves',
            'explanation': """Electromagnetic waves possess several key characteristics: they are not affected by external electric or magnetic fields, they do not require a material medium for propagation, and they travel at a speed of 3 × 10^8 m/s in a vacuum.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Wave Properties',
            'examples': ["Light from distant stars travels through the vacuum of space to reach Earth without needing a medium.", "A powerful magnet will not deflect a beam of light or X-rays.", "Despite containing charged particles, the fields of an EM wave are self-propagating and not influenced by external static fields."]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_spectrum'))
    def rule_electromagnetic_spectrum(self):
        """The electromagnetic spectrum is the entire range of all types of electromagnetic radiation, categorized by distinct frequency ranges where the characteristics of the waves vary significantly."""
        self.response = {
            'concept': 'Electromagnetic Spectrum',
            'explanation': """The electromagnetic spectrum is the entire range of all types of electromagnetic radiation, categorized by distinct frequency ranges where the characteristics of the waves vary significantly.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["The electromagnetic spectrum encompasses visible light, infrared, ultraviolet, X-rays, gamma rays, microwaves, and radio waves.", "Different regions of the spectrum have unique applications due to their varying wavelengths and energies.", "From extremely long radio waves to incredibly short gamma rays, the spectrum covers a vast range of frequencies."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_electromagnetic_waves_and_their_frequency_ranges'))
    def rule_types_of_electromagnetic_waves_and_their_frequency_ranges(self):
        """The electromagnetic spectrum is divided into several main types of waves, each defined by a specific frequency range:"""
        self.response = {
            'concept': 'Types of Electromagnetic Waves and their Frequency Ranges',
            'explanation': """The electromagnetic spectrum is divided into several main types of waves, each defined by a specific frequency range:""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Radio waves have frequencies typically less than 3 × 10^9 Hz.", "Visible rays occupy a narrow band from 4.28 × 10^14 Hz to 7.69 × 10^14 Hz.", "Gamma rays are the highest frequency waves, with frequencies greater than 3 × 10^19 Hz."]
        }
        self.halt()

    @Rule(Fact(query_topic='visible_light'))
    def rule_visible_light(self):
        """Visible light is the narrow range of the electromagnetic spectrum to which human eyes are sensitive. Its frequencies span from 4.28 × 10^14 Hz to 7.69 × 10^14 Hz, corresponding to a wavelength range from 690 nm to 400 nm. The region with the lowest wavelength (highest frequency) appears violet, and as the wavelength increases (frequency decreases), the color gradually changes through indigo, blue, up to red, forming the seven colors of the rainbow."""
        self.response = {
            'concept': 'Visible Light',
            'explanation': """Visible light is the narrow range of the electromagnetic spectrum to which human eyes are sensitive. Its frequencies span from 4.28 × 10^14 Hz to 7.69 × 10^14 Hz, corresponding to a wavelength range from 690 nm to 400 nm. The region with the lowest wavelength (highest frequency) appears violet, and as the wavelength increases (frequency decreases), the color gradually changes through indigo, blue, up to red, forming the seven colors of the rainbow.""",
            'topic': 'Physics Waves and their Applications',
            'subtopic': 'Applications of Electromagnetic Waves',
            'examples': ["The colors observed in a rainbow.", "Human vision relies on visible light.", "The violet color corresponds to the highest frequency of visible light."]
        }
        self.halt()

    @Rule(Fact(query_topic='gamma_rays'))
    def rule_gamma_rays(self):
        """Gamma rays are a type of electromagnetic wave emitted by radioactive elements. They possess extremely high frequencies and energies, allowing them to penetrate thick sheets of steel and concrete slabs. Due to their ability to destroy living cells, they are utilized in medical applications and sterilization processes."""
        self.response = {
            'concept': 'Gamma rays',
            'explanation': """Gamma rays are a type of electromagnetic wave emitted by radioactive elements. They possess extremely high frequencies and energies, allowing them to penetrate thick sheets of steel and concrete slabs. Due to their ability to destroy living cells, they are utilized in medical applications and sterilization processes.""",
            'topic': 'Physics Waves and their Applications',
            'subtopic': 'Applications of Electromagnetic Waves',
            'examples': ["Destroying cancer cells in medical treatment.", "Sterilizing utensils used for food.", "Sterilizing surgical instruments."]
        }
        self.halt()

    @Rule(Fact(query_topic='x_rays'))
    def rule_x_rays(self):
        """X-rays are electromagnetic waves primarily used for imaging internal organs of the human body. They travel easily through soft tissues but their intensity decreases rapidly when passing through bones, allowing for image formation. Excessive exposure to X-rays can cause cancers. They are generated by bombarding metal targets with high-speed electrons, converting the electrons' kinetic energy into X-rays."""
        self.response = {
            'concept': 'X-rays',
            'explanation': """X-rays are electromagnetic waves primarily used for imaging internal organs of the human body. They travel easily through soft tissues but their intensity decreases rapidly when passing through bones, allowing for image formation. Excessive exposure to X-rays can cause cancers. They are generated by bombarding metal targets with high-speed electrons, converting the electrons' kinetic energy into X-rays.""",
            'topic': 'Physics Waves and their Applications',
            'subtopic': 'Applications of Electromagnetic Waves',
            'examples': ["Taking photographs of internal body organs (e.g., bones).", "Examining the baggage of airline passengers.", "Scanning cargo inside containers."]
        }
        self.halt()

    @Rule(Fact(query_topic='x_ray_generation'))
    def rule_x_ray_generation(self):
        """X-rays are produced when a fast beam of electrons is allowed to hit a metal target, converting a part of the electrons' kinetic energy into X-rays."""
        self.response = {
            'concept': 'X-ray Generation',
            'explanation': """X-rays are produced when a fast beam of electrons is allowed to hit a metal target, converting a part of the electrons' kinetic energy into X-rays.""",
            'topic': 'Physics',
            'subtopic': 'X-rays',
            'examples': ["An X-ray tube uses an electron beam striking a metal anode to generate X-rays.", "The kinetic energy of accelerated electrons is transformed into X-ray radiation upon impact.", "Medical imaging equipment generates X-rays by firing electrons at a target."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultraviolet_radiation_definition_and_characteristics'))
    def rule_ultraviolet_radiation_definition_and_characteristics(self):
        """Ultraviolet (UV) radiation means 'above violet' and refers to rays with a frequency range above that of violet, which is the highest frequency color in the visible spectrum. UV radiation is invisible to the human eye, though some insects like bees can detect it. Sunlight contains a small amount of UV rays, which are also produced in electric discharge and from mercury vapor lamps."""
        self.response = {
            'concept': 'Ultraviolet Radiation Definition and Characteristics',
            'explanation': """Ultraviolet (UV) radiation means 'above violet' and refers to rays with a frequency range above that of violet, which is the highest frequency color in the visible spectrum. UV radiation is invisible to the human eye, though some insects like bees can detect it. Sunlight contains a small amount of UV rays, which are also produced in electric discharge and from mercury vapor lamps.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Violet light has a higher frequency than red light, but UV is even higher.", "Bees use UV vision to see patterns on flowers that are invisible to humans.", "A mercury vapor lamp emits ultraviolet light as part of its spectrum."]
        }
        self.halt()

    @Rule(Fact(query_topic='biological_effects_of_ultraviolet_radiation'))
    def rule_biological_effects_of_ultraviolet_radiation(self):
        """Ultraviolet radiation is beneficial to some extent as it helps the human body produce vitamin D. However, overexposure to ultraviolet rays can be harmful, causing conditions such as cataracts in the eye and various cancers in the skin."""
        self.response = {
            'concept': 'Biological Effects of Ultraviolet Radiation',
            'explanation': """Ultraviolet radiation is beneficial to some extent as it helps the human body produce vitamin D. However, overexposure to ultraviolet rays can be harmful, causing conditions such as cataracts in the eye and various cancers in the skin.""",
            'topic': 'Physics',
            'subtopic': 'Health and Safety',
            'examples': ["Moderate exposure to sunlight helps in the synthesis of Vitamin D.", "Wearing sunglasses protects the eyes from UV radiation to prevent cataracts.", "Excessive sunbathing can lead to an increased risk of skin cancer."]
        }
        self.halt()

    @Rule(Fact(query_topic='applications_of_ultraviolet_radiation'))
    def rule_applications_of_ultraviolet_radiation(self):
        """Ultraviolet radiation is used in hospitals for sterilization to kill germs. Its ability to make certain chemical substances glitter (fluoresce) is utilized in banks to check for hidden symbols in currency notes and in some washing powders to make clothes appear brighter when exposed to sunlight."""
        self.response = {
            'concept': 'Applications of Ultraviolet Radiation',
            'explanation': """Ultraviolet radiation is used in hospitals for sterilization to kill germs. Its ability to make certain chemical substances glitter (fluoresce) is utilized in banks to check for hidden symbols in currency notes and in some washing powders to make clothes appear brighter when exposed to sunlight.""",
            'topic': 'Physics',
            'subtopic': 'Practical Uses',
            'examples': ["UV lamps are used to sterilize surgical instruments in hospitals.", "Banks use UV light to detect counterfeit currency by revealing security features.", "Clothes washed with certain detergents show enhanced brightness under sunlight due to UV-reactive chemicals."]
        }
        self.halt()

    @Rule(Fact(query_topic='infrared_radiation_definition_and_characteristics'))
    def rule_infrared_radiation_definition_and_characteristics(self):
        """Infrared (IR) radiation is the range of frequencies below the red color that is not visible to the human eye. It is emitted by all heated bodies and often referred to as 'heat rays' because it causes a warm sensation when it falls on the skin. The human body also emits infrared radiation."""
        self.response = {
            'concept': 'Infrared Radiation Definition and Characteristics',
            'explanation': """Infrared (IR) radiation is the range of frequencies below the red color that is not visible to the human eye. It is emitted by all heated bodies and often referred to as 'heat rays' because it causes a warm sensation when it falls on the skin. The human body also emits infrared radiation.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["The warmth felt from a radiator is due to infrared radiation.", "Infrared light has a longer wavelength than red visible light.", "All warm objects, including our bodies, continuously emit infrared radiation."]
        }
        self.halt()

    @Rule(Fact(query_topic='applications_of_infrared_radiation'))
    def rule_applications_of_infrared_radiation(self):
        """Infrared radiation is used to take 'heat photographs' (thermal images) by capturing the heat rays emitted by body organs. This application can be used to identify certain diseases."""
        self.response = {
            'concept': 'Applications of Infrared Radiation',
            'explanation': """Infrared radiation is used to take 'heat photographs' (thermal images) by capturing the heat rays emitted by body organs. This application can be used to identify certain diseases.""",
            'topic': 'Physics',
            'subtopic': 'Practical Uses',
            'examples': ["Thermal cameras use infrared radiation to create images showing temperature differences.", "Doctors can use infrared imaging to detect areas of inflammation or unusual heat in the body.", "Infrared sensors are used in night vision devices to detect heat signatures."]
        }
        self.halt()

    @Rule(Fact(query_topic='infrared_radiation'))
    def rule_infrared_radiation(self):
        """Infrared radiation is a form of electromagnetic radiation used for various applications. It is employed to send signals from remote controls to television sets. Most cameras found in mobile telephones and computers are designed to be sensitive to infrared radiation. Additionally, it is utilized for physiotherapy treatments, and heat photographs are identified using this radiation."""
        self.response = {
            'concept': 'Infrared Radiation',
            'explanation': """Infrared radiation is a form of electromagnetic radiation used for various applications. It is employed to send signals from remote controls to television sets. Most cameras found in mobile telephones and computers are designed to be sensitive to infrared radiation. Additionally, it is utilized for physiotherapy treatments, and heat photographs are identified using this radiation.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Sending signals from remote controls to television sets.", "Cameras in mobile telephones and computers sensitive to infrared.", "Physiotherapy treatments using infrared radiation."]
        }
        self.halt()

    @Rule(Fact(query_topic='microwaves'))
    def rule_microwaves(self):
        """Microwaves are a range of electromagnetic frequencies found below infrared frequencies. They are used in RADAR systems, mobile telephones, and microwave ovens. The principle behind microwave ovens is that water and fat in food absorb microwaves, converting the energy into vibrational kinetic energy (heat). High-power microwaves for ovens and radar are produced by an instrument called a magnetron. Microwaves can cause adverse effects on the body; therefore, microwave ovens are designed to prevent leakage, and it is advised not to stay too close during operation. Excessive use of mobile telephones is suspected to cause harm to the brain."""
        self.response = {
            'concept': 'Microwaves',
            'explanation': """Microwaves are a range of electromagnetic frequencies found below infrared frequencies. They are used in RADAR systems, mobile telephones, and microwave ovens. The principle behind microwave ovens is that water and fat in food absorb microwaves, converting the energy into vibrational kinetic energy (heat). High-power microwaves for ovens and radar are produced by an instrument called a magnetron. Microwaves can cause adverse effects on the body; therefore, microwave ovens are designed to prevent leakage, and it is advised not to stay too close during operation. Excessive use of mobile telephones is suspected to cause harm to the brain.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Usage in RADAR systems.", "Heating food in microwave ovens.", "Communication via mobile telephones."]
        }
        self.halt()

    @Rule(Fact(query_topic='radio_waves'))
    def rule_radio_waves(self):
        """Radio waves possess the longest wavelengths and the shortest frequencies within the electromagnetic spectrum. They are primarily used for long-distance communications and are produced using radio frequency oscillators. When radio waves encounter an aerial, the aerial receives the information carried by the wave. Antennas are vital for both transmitting and receiving radio waves, and information is transmitted by modifying either the amplitude or the frequency of the wave according to the data."""
        self.response = {
            'concept': 'Radio Waves',
            'explanation': """Radio waves possess the longest wavelengths and the shortest frequencies within the electromagnetic spectrum. They are primarily used for long-distance communications and are produced using radio frequency oscillators. When radio waves encounter an aerial, the aerial receives the information carried by the wave. Antennas are vital for both transmitting and receiving radio waves, and information is transmitted by modifying either the amplitude or the frequency of the wave according to the data.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Long-distance communications.", "Information transmission by modifying amplitude.", "Reception of information by an aerial."]
        }
        self.halt()

    @Rule(Fact(query_topic='acoustic_energy'))
    def rule_acoustic_energy(self):
        """Acoustic energy is the type of energy that produces the sensation of hearing in our ears."""
        self.response = {
            'concept': 'Acoustic Energy',
            'explanation': """Acoustic energy is the type of energy that produces the sensation of hearing in our ears.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["Listening to musical instruments.", "Hearing various sounds in your surroundings early in the morning.", "The energy produced by a Hyla tree frog's voice."]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_generation_principle'))
    def rule_sound_generation_principle(self):
        """All sounds are generated by vibrations of objects. Many animals produce sounds by vibrating an organ in their body."""
        self.response = {
            'concept': 'Sound Generation Principle',
            'explanation': """All sounds are generated by vibrations of objects. Many animals produce sounds by vibrating an organ in their body.""",
            'topic': 'Physics',
            'subtopic': 'Sound Production',
            'examples': ["A buzzing bee making sound waves by moving its wings to and fro very fast.", "Crickets making their sound by rubbing their wings together.", "Our vocal cords vibrating, causing the air around them to vibrate and produce sound."]
        }
        self.halt()

    @Rule(Fact(query_topic='hyla_tree_frog_sound_mechanism'))
    def rule_hyla_tree_frog_sound_mechanism(self):
        """Male Hyla tree frogs amplify their voice using an inflatable balloon-like body organ under their throat. Sound is generated when air dispelled by the balloon passes through two stretched membranes at the bottom of their mouths, giving rise to vibrations in the membranes."""
        self.response = {
            'concept': 'Hyla Tree Frog Sound Mechanism',
            'explanation': """Male Hyla tree frogs amplify their voice using an inflatable balloon-like body organ under their throat. Sound is generated when air dispelled by the balloon passes through two stretched membranes at the bottom of their mouths, giving rise to vibrations in the membranes.""",
            'topic': 'Physics',
            'subtopic': 'Animal Sound Production',
            'examples': ["The male Hyla frog inflating its throat balloon to amplify its voice.", "Air passing through stretched membranes in the frog's mouth to create vibrations.", "A Hyla frog's voice traveling about ten times further than other varieties of frogs."]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_wave_propagation_and_hearing'))
    def rule_sound_wave_propagation_and_hearing(self):
        """We hear sounds when the resulting sound waves propagate through air and reach our ears. The vibrations of objects cause the surrounding air to vibrate, producing these sound waves that then travel."""
        self.response = {
            'concept': 'Sound Wave Propagation and Hearing',
            'explanation': """We hear sounds when the resulting sound waves propagate through air and reach our ears. The vibrations of objects cause the surrounding air to vibrate, producing these sound waves that then travel.""",
            'topic': 'Physics',
            'subtopic': 'Sound Wave Characteristics',
            'examples': ["Sound waves from vibrating vocal cords propagating through air to our ears.", "Sound waves from a buzzing bee reaching our ears.", "Sound waves generated by a loud-speaker traveling through the air."]
        }
        self.halt()

    @Rule(Fact(query_topic='formation_of_compressions__sound_'))
    def rule_formation_of_compressions__sound_(self):
        """When a vibrating membrane moves in one direction (e.g., right), it pushes air molecules forward, creating a layer of compressed air. This compressed region then moves forward, transferring kinetic energy to the air molecules."""
        self.response = {
            'concept': 'Formation of Compressions (Sound)',
            'explanation': """When a vibrating membrane moves in one direction (e.g., right), it pushes air molecules forward, creating a layer of compressed air. This compressed region then moves forward, transferring kinetic energy to the air molecules.""",
            'topic': 'Physics',
            'subtopic': 'Sound Propagation',
            'examples': ["Membrane moving to the right pushing air molecules forward", "Formation of a layer of compressed air shown in Figure 4.23 (b)", "Compressed region moves forward with kinetic energy transferred to air molecules"]
        }
        self.halt()

    @Rule(Fact(query_topic='formation_of_rarefactions__sound_'))
    def rule_formation_of_rarefactions__sound_(self):
        """When a vibrating membrane moves in the opposite direction (e.g., left), it creates a region of lower pressure, known as a rarefaction, in the air layer adjacent to it."""
        self.response = {
            'concept': 'Formation of Rarefactions (Sound)',
            'explanation': """When a vibrating membrane moves in the opposite direction (e.g., left), it creates a region of lower pressure, known as a rarefaction, in the air layer adjacent to it.""",
            'topic': 'Physics',
            'subtopic': 'Sound Propagation',
            'examples': ["Membrane moving to the left", "A region of rarefactions is formed in the air layer adjacent to the membrane", "Region shown in Figure 4.23 (c)"]
        }
        self.halt()

    @Rule(Fact(query_topic='nature_of_sound_waves'))
    def rule_nature_of_sound_waves(self):
        """Sound waves are characterized by the alternative generation and propagation of compressions and rarefactions in a medium. These compressions and rarefactions travel forward at the same speed, and sound is classified as a longitudinal wave."""
        self.response = {
            'concept': 'Nature of Sound Waves',
            'explanation': """Sound waves are characterized by the alternative generation and propagation of compressions and rarefactions in a medium. These compressions and rarefactions travel forward at the same speed, and sound is classified as a longitudinal wave.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["The membrane alternatively generates compressions and rarefactions", "Compressions and rarefactions travel forward with the same speed", "Sound is longitudinal waves"]
        }
        self.halt()

    @Rule(Fact(query_topic='molecular_motion_in_sound_waves'))
    def rule_molecular_motion_in_sound_waves(self):
        """Despite the forward movement of compressions and rarefactions, the individual particles of the medium (e.g., air molecules) only vibrate back and forth around a mean position."""
        self.response = {
            'concept': 'Molecular Motion in Sound Waves',
            'explanation': """Despite the forward movement of compressions and rarefactions, the individual particles of the medium (e.g., air molecules) only vibrate back and forth around a mean position.""",
            'topic': 'Physics',
            'subtopic': 'Wave Characteristics',
            'examples': ["Each air molecule only vibrates back and forth", "Air molecules vibrate around a mean position", "Compressions and rarefactions move forward"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_propagation_through_different_media'))
    def rule_sound_propagation_through_different_media(self):
        """Sound is not limited to air; it can propagate through various media, including water and solids. Generally, sound propagates better and faster through denser or more rigid media."""
        self.response = {
            'concept': 'Sound Propagation Through Different Media',
            'explanation': """Sound is not limited to air; it can propagate through various media, including water and solids. Generally, sound propagates better and faster through denser or more rigid media.""",
            'topic': 'Physics',
            'subtopic': 'Speed of Sound',
            'examples': ["Sound propagates not only through air", "Sound propagates through water", "Sound propagation is even better through solids"]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_sound_in_specific_media'))
    def rule_speed_of_sound_in_specific_media(self):
        """The speed of sound varies significantly depending on the medium. For example, sound travels about 1400 ms-1 in water and approximately 5000 m s-1 in steel, both considerably faster than in air."""
        self.response = {
            'concept': 'Speed of Sound in Specific Media',
            'explanation': """The speed of sound varies significantly depending on the medium. For example, sound travels about 1400 ms-1 in water and approximately 5000 m s-1 in steel, both considerably faster than in air.""",
            'topic': 'Physics',
            'subtopic': 'Speed of Sound',
            'examples': ["Sound waves travel through water with a speed of about 1400 ms-1", "Speed of sound waves through steel is about 5000 m s-1", "Sound propagates through water even faster than through air"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_wave_nature_of_sound'))
    def rule_mechanical_wave_nature_of_sound(self):
        """Sound waves are mechanical waves, which means they require a material medium (unlike light) to propagate and spread. They cannot travel through a vacuum."""
        self.response = {
            'concept': 'Mechanical Wave Nature of Sound',
            'explanation': """Sound waves are mechanical waves, which means they require a material medium (unlike light) to propagate and spread. They cannot travel through a vacuum.""",
            'topic': 'Physics',
            'subtopic': 'Wave Classification',
            'examples': ["A medium is essential for sound to spread", "Sound waves are mechanical wave", "Unlike light, a medium is essential for sound"]
        }
        self.halt()

    @Rule(Fact(query_topic='detection_and_communication_using_sound_propagation'))
    def rule_detection_and_communication_using_sound_propagation(self):
        """The ability of sound to travel through various media is exploited for communication and detection in nature. Examples include whales communicating underwater and snakes detecting ground vibrations through their bones."""
        self.response = {
            'concept': 'Detection and Communication Using Sound Propagation',
            'explanation': """The ability of sound to travel through various media is exploited for communication and detection in nature. Examples include whales communicating underwater and snakes detecting ground vibrations through their bones.""",
            'topic': 'Physics',
            'subtopic': 'Applications of Sound',
            'examples': ["Whales use sound waves to communicate among themselves", "Snakes can detect vibrations in the ground through its lower jaw bone", "The sound of a train approaching can be clearly heard through steel rails"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_requires_a_medium_for_propagation'))
    def rule_sound_requires_a_medium_for_propagation(self):
        """Sound waves cannot propagate through a vacuum; they require a material medium (such as air) to travel. An experiment with an electric bell inside a bell jar connected to a vacuum pump demonstrates this: as air is removed from the jar, the sound of the bell gradually becomes fainter and eventually disappears when a vacuum is formed."""
        self.response = {
            'concept': 'Sound Requires a Medium for Propagation',
            'explanation': """Sound waves cannot propagate through a vacuum; they require a material medium (such as air) to travel. An experiment with an electric bell inside a bell jar connected to a vacuum pump demonstrates this: as air is removed from the jar, the sound of the bell gradually becomes fainter and eventually disappears when a vacuum is formed.""",
            'topic': 'Physics',
            'subtopic': 'Sound Propagation',
            'examples': ["The sound of an electric bell becomes fainter and finally inaudible when the bell jar surrounding it becomes a vacuum.", "Sound does not travel through a vacuum.", "A medium is essential for sound waves to travel through."]
        }
        self.halt()

    @Rule(Fact(query_topic='difference_in_speed_between_light_and_sound'))
    def rule_difference_in_speed_between_light_and_sound(self):
        """Light travels at a significantly higher speed (300,000 km s-1 or 3 × 10^8 m s-1) compared to sound. This difference causes a time gap between observing a visual event (like lightning) and hearing its associated sound (thunder) when the event occurs at a distant point."""
        self.response = {
            'concept': 'Difference in Speed Between Light and Sound',
            'explanation': """Light travels at a significantly higher speed (300,000 km s-1 or 3 × 10^8 m s-1) compared to sound. This difference causes a time gap between observing a visual event (like lightning) and hearing its associated sound (thunder) when the event occurs at a distant point.""",
            'topic': 'Physics',
            'subtopic': 'Wave Speed',
            'examples': ["We hear the sound of thunder a short while after we see the light from a lightning strike.", "Light from a lightning strike takes a very short time to reach our eyes.", "There is a short time gap between seeing the light and hearing the thunder because it takes longer for the sound wave to travel."]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_sound_in_dry_air'))
    def rule_speed_of_sound_in_dry_air(self):
        """The speed of sound in dry air is temperature-dependent. At 0 oC, the speed of sound is approximately 330 m s-1. As the temperature increases, the speed of sound also increases; for instance, at 30 oC, it is about 350 m s-1."""
        self.response = {
            'concept': 'Speed of Sound in Dry Air',
            'explanation': """The speed of sound in dry air is temperature-dependent. At 0 oC, the speed of sound is approximately 330 m s-1. As the temperature increases, the speed of sound also increases; for instance, at 30 oC, it is about 350 m s-1.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves / Speed of Sound',
            'examples': ["Sound travels at 330 m/s in dry air when the temperature is 0 oC.", "At a warmer temperature of 30 oC, the speed of sound in dry air increases to 350 m/s.", "A change in air temperature affects how fast sound propagates."]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_sound_in_different_media'))
    def rule_speed_of_sound_in_different_media(self):
        """The speed of sound varies significantly across different mediums. In water, the speed of sound is about 1400 m s-1, which is approximately four times faster than in air. Through a steel rod, the speed of sound is about 5000 m s-1."""
        self.response = {
            'concept': 'Speed of Sound in Different Media',
            'explanation': """The speed of sound varies significantly across different mediums. In water, the speed of sound is about 1400 m s-1, which is approximately four times faster than in air. Through a steel rod, the speed of sound is about 5000 m s-1.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves / Speed of Sound',
            'examples': ["Underwater communication uses sound waves traveling at about 1400 m/s.", "A vibration in a steel beam can propagate at speeds up to 5000 m/s.", "Sound travels much faster in dense materials like steel and water compared to air."]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_characteristics__definition_'))
    def rule_sound_characteristics__definition_(self):
        """Sound characteristics are the properties of sound that allow listeners to distinguish different sounds. These are sensations produced in the ear that help differentiate one sound from another."""
        self.response = {
            'concept': 'Sound Characteristics (Definition)',
            'explanation': """Sound characteristics are the properties of sound that allow listeners to distinguish different sounds. These are sensations produced in the ear that help differentiate one sound from another.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves / Characteristics of Sound',
            'examples': ["The ability to tell the difference between a loud thunderclap and a soft whisper is due to sound characteristics.", "Sound characteristics enable us to distinguish the sound of a violin from a flute.", "Pitch, loudness, and quality of sound are types of sound characteristics."]
        }
        self.halt()

    @Rule(Fact(query_topic='main_characteristics_of_sound'))
    def rule_main_characteristics_of_sound(self):
        """There are three primary characteristics used to describe and distinguish sounds: Pitch, Loudness, and Quality of sound."""
        self.response = {
            'concept': 'Main Characteristics of Sound',
            'explanation': """There are three primary characteristics used to describe and distinguish sounds: Pitch, Loudness, and Quality of sound.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves / Characteristics of Sound',
            'examples': ["Pitch helps us classify a sound as high or low.", "Loudness describes how intense or soft a sound is perceived.", "The quality of sound allows us to recognize the source of a sound, like a specific musical instrument."]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch__relationship_with_frequency_'))
    def rule_pitch__relationship_with_frequency_(self):
        """Pitch is a quality of sound that is directly dependent on its frequency. An increase in the frequency of vibrations results in a higher pitch (a sharper sound), while a decrease in frequency leads to a lower pitch (a less sharp sound)."""
        self.response = {
            'concept': 'Pitch (Relationship with Frequency)',
            'explanation': """Pitch is a quality of sound that is directly dependent on its frequency. An increase in the frequency of vibrations results in a higher pitch (a sharper sound), while a decrease in frequency leads to a lower pitch (a less sharp sound).""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves / Pitch',
            'examples': ["When a hacksaw blade vibrates rapidly (high frequency), it produces a high-pitched sound.", "Increasing the length of a vibrating object reduces its frequency, thereby decreasing the pitch of the sound.", "A high-pitched sound, like a whistle, corresponds to a high vibration frequency."]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch_and_frequency_relationship'))
    def rule_pitch_and_frequency_relationship(self):
        """The pitch of a sound is directly related to its frequency. A higher frequency corresponds to a higher pitch, while a lower frequency corresponds to a lower pitch."""
        self.response = {
            'concept': 'Pitch and Frequency Relationship',
            'explanation': """The pitch of a sound is directly related to its frequency. A higher frequency corresponds to a higher pitch, while a lower frequency corresponds to a lower pitch.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["The frequency of the note middle C is 256 Hz.", "The frequency of the note higher C is 512 Hz.", "The pitch of the higher C is twice as high as the pitch of the middle C because its frequency is doubled."]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_wave_waveform'))
    def rule_sound_wave_waveform(self):
        """The oscillation of air molecules around their central position, caused by a sound wave, can be observed and displayed as a graph against time using a cathode ray oscilloscope (CRO). The shape of this displayed graph on the CRO screen is known as the waveform of the sound wave."""
        self.response = {
            'concept': 'Sound Wave Waveform',
            'explanation': """The oscillation of air molecules around their central position, caused by a sound wave, can be observed and displayed as a graph against time using a cathode ray oscilloscope (CRO). The shape of this displayed graph on the CRO screen is known as the waveform of the sound wave.""",
            'topic': 'Physics',
            'subtopic': 'Sound Wave Visualization',
            'examples': ["When a microphone is connected to an oscilloscope and a sound is generated, the oscilloscope screen displays the sound wave's graph.", "Figure 4.29 illustrates the shape of a sound wave displayed on a cathode ray oscilloscope.", "Figure 4.30 shows waveforms of two sound waves, one with a high pitch (high frequency) and another with a lower pitch (lower frequency)."]
        }
        self.halt()

    @Rule(Fact(query_topic='loudness'))
    def rule_loudness(self):
        """Loudness is the sensation perceived in the ear that depends on the amount of energy carried by the sound wave. A sound wave carrying a larger amount of energy will result in a louder sound."""
        self.response = {
            'concept': 'Loudness',
            'explanation': """Loudness is the sensation perceived in the ear that depends on the amount of energy carried by the sound wave. A sound wave carrying a larger amount of energy will result in a louder sound.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Tapping a drum with a larger force produces a louder sound because more energy is imparted.", "Plucking a stretched string harder displaces it further, requiring more work, and generates a louder sound wave with greater energy.", "Tapping a drum softly produces a lower sound level, indicating less energy carried by the sound wave."]
        }
        self.halt()

    @Rule(Fact(query_topic='loudness_of_sound'))
    def rule_loudness_of_sound(self):
        """Loudness is a characteristic of sound that varies according to the amplitude of a sound wave. It increases with increasing amplitude and decreases when the amplitude decreases. A higher amplitude corresponds to a higher level of loudness, while a lower amplitude corresponds to a lower level of loudness."""
        self.response = {
            'concept': 'Loudness of Sound',
            'explanation': """Loudness is a characteristic of sound that varies according to the amplitude of a sound wave. It increases with increasing amplitude and decreases when the amplitude decreases. A higher amplitude corresponds to a higher level of loudness, while a lower amplitude corresponds to a lower level of loudness.""",
            'topic': 'Physics',
            'subtopic': 'Characteristics of Sound',
            'examples': ["When a string is displaced further, the amplitude of vibration and the loudness of the sound wave both become larger.", "Waveforms of sound waves viewed on a cathode ray oscilloscope show higher amplitude for a high level of loudness and lower amplitude for a low level of loudness.", "A guitar string plucked gently will produce a quieter sound (lower amplitude) than one plucked forcefully (higher amplitude)."]
        }
        self.halt()

    @Rule(Fact(query_topic='quality_of_sound__timbre_'))
    def rule_quality_of_sound__timbre_(self):
        """The quality of sound is the characteristic that enables the ear to distinguish between sounds produced by different sources or instruments, even when they play notes with the same pitch and loudness. This distinction is possible due to differences in their waveforms, as different instruments produce unique wave patterns for the same note."""
        self.response = {
            'concept': 'Quality of Sound (Timbre)',
            'explanation': """The quality of sound is the characteristic that enables the ear to distinguish between sounds produced by different sources or instruments, even when they play notes with the same pitch and loudness. This distinction is possible due to differences in their waveforms, as different instruments produce unique wave patterns for the same note.""",
            'topic': 'Physics',
            'subtopic': 'Characteristics of Sound',
            'examples': ["Identifying the sound of a piano from that of a violin, even when both play a note with the same pitch and loudness.", "Waveforms of the same musical note played by a tuning fork, a violin, and a piano show distinct patterns when viewed on a cathode ray oscilloscope.", "The unique sound of a trumpet compared to a flute playing the same note is due to their different sound qualities."]
        }
        self.halt()

    @Rule(Fact(query_topic='human_hearing_range'))
    def rule_human_hearing_range(self):
        """The frequency range that can typically be heard by the human ear is from 20 Hz to 20,000 Hz. However, the upper limit of this audible range gradually decreases with age."""
        self.response = {
            'concept': 'Human Hearing Range',
            'explanation': """The frequency range that can typically be heard by the human ear is from 20 Hz to 20,000 Hz. However, the upper limit of this audible range gradually decreases with age.""",
            'topic': 'Physics',
            'subtopic': 'Sound Perception',
            'examples': ["A young adult can typically hear sounds between 20 Hz and 20,000 Hz.", "An older individual might find it difficult to hear frequencies near 20,000 Hz."]
        }
        self.halt()

    @Rule(Fact(query_topic='infra_sound'))
    def rule_infra_sound(self):
        """Infra-sound refers to sound waves with frequencies below 20 Hz, which are inaudible to the human ear."""
        self.response = {
            'concept': 'Infra-sound',
            'explanation': """Infra-sound refers to sound waves with frequencies below 20 Hz, which are inaudible to the human ear.""",
            'topic': 'Physics',
            'subtopic': 'Sound Frequencies',
            'examples': ["Sounds with a frequency lower than 20 Hz are classified as infra-sound.", "Elephants are capable of hearing infra-sound frequencies."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound'))
    def rule_ultrasound(self):
        """Ultrasound refers to sound waves with frequencies above 20,000 Hz, which are beyond the normal hearing range of humans."""
        self.response = {
            'concept': 'Ultrasound',
            'explanation': """Ultrasound refers to sound waves with frequencies above 20,000 Hz, which are beyond the normal hearing range of humans.""",
            'topic': 'Physics',
            'subtopic': 'Sound Frequencies',
            'examples': ["Sounds above 20,000 Hz are known as ultrasound.", "Bats and dolphins can perceive ultrasound frequencies."]
        }
        self.halt()

    @Rule(Fact(query_topic='sonar_for_sea_depth_measurement'))
    def rule_sonar_for_sea_depth_measurement(self):
        """SONAR (Sound Navigation and Ranging) is an instrument, typically affixed to the bottom of a ship, that emits ultrasound pulses to measure the depth of the sea. The depth is calculated by determining the time taken for these pulses to return after reflecting off the seabed."""
        self.response = {
            'concept': 'SONAR for Sea Depth Measurement',
            'explanation': """SONAR (Sound Navigation and Ranging) is an instrument, typically affixed to the bottom of a ship, that emits ultrasound pulses to measure the depth of the sea. The depth is calculated by determining the time taken for these pulses to return after reflecting off the seabed.""",
            'topic': 'Physics',
            'subtopic': 'Applications of Ultrasound / Oceanography',
            'examples': ["A ship employs SONAR to map the ocean floor.", "The time interval between emitting and receiving an ultrasound pulse indicates the sea depth.", "SONAR systems are crucial for marine navigation and research."]
        }
        self.halt()

    @Rule(Fact(query_topic='measuring_depth_of_the_sea__sonar_'))
    def rule_measuring_depth_of_the_sea__sonar_(self):
        """Ultrasound pulses are transmitted by a ship, travel through the water, reflect off the bottom of the sea, and are detected back at the ship. The depth of the sea can be calculated by using the known speed of sound in water and the total time taken for the ultrasound wave to travel to the bottom and return (Distance = (Speed × Time) / 2)."""
        self.response = {
            'concept': 'Measuring Depth of the Sea (Sonar)',
            'explanation': """Ultrasound pulses are transmitted by a ship, travel through the water, reflect off the bottom of the sea, and are detected back at the ship. The depth of the sea can be calculated by using the known speed of sound in water and the total time taken for the ultrasound wave to travel to the bottom and return (Distance = (Speed × Time) / 2).""",
            'topic': 'Physics',
            'subtopic': 'Applications of Ultrasound Waves',
            'examples': ["Finding the depth of the sea using ultrasound waves.", "If the time taken by ultrasound waves transmitted by a ship to reach the detector again after reflection from the sea bottom is 4 s, find the distance between the ship and the bottom of the sea (given speed of sound is 1500 m s-1).", "Distance between the ship and the bottom of the sea = (1500 m/s × 4 s) / 2 = 3000 m."]
        }
        self.halt()

    @Rule(Fact(query_topic='underwater_detection_and_investigation'))
    def rule_underwater_detection_and_investigation(self):
        """Ultrasound waves are used for detecting and investigating objects or groups of organisms underwater, leveraging the principles of reflection and time-of-flight measurements."""
        self.response = {
            'concept': 'Underwater Detection and Investigation',
            'explanation': """Ultrasound waves are used for detecting and investigating objects or groups of organisms underwater, leveraging the principles of reflection and time-of-flight measurements.""",
            'topic': 'Physics',
            'subtopic': 'Applications of Ultrasound Waves',
            'examples': ["Investigating schools of fish.", "Detecting remnants of capsized ships."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound_spectacles_for_the_blind'))
    def rule_ultrasound_spectacles_for_the_blind(self):
        """Ultrasound waves are incorporated into spectacles designed to assist blind individuals, likely by detecting obstacles or providing spatial awareness through sound cues."""
        self.response = {
            'concept': 'Ultrasound Spectacles for the Blind',
            'explanation': """Ultrasound waves are incorporated into spectacles designed to assist blind individuals, likely by detecting obstacles or providing spatial awareness through sound cues.""",
            'topic': 'Physics',
            'subtopic': 'Applications of Ultrasound Waves',
            'examples': ["Ultrasound waves are used in ultrasound spectacles worn by blind people."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound_scanning__medical_imaging_'))
    def rule_ultrasound_scanning__medical_imaging_(self):
        """Ultrasound scanning involves using ultrasound waves to examine internal organs of the human body. Waves emitted by a transmitter reflect off internal structures, and the reflected waves are used to create images and provide information about organ size, function, and condition."""
        self.response = {
            'concept': 'Ultrasound Scanning (Medical Imaging)',
            'explanation': """Ultrasound scanning involves using ultrasound waves to examine internal organs of the human body. Waves emitted by a transmitter reflect off internal structures, and the reflected waves are used to create images and provide information about organ size, function, and condition.""",
            'topic': 'Physics',
            'subtopic': 'Medical Applications of Ultrasound',
            'examples': ["Examining internal organs of the human body.", "Revealing information regarding the volume of blood sent out during a single compression of the heart, the size of the heart, and pulse rate.", "Observing the womb and the condition of the fetus inside the womb of a pregnant mother."]
        }
        self.halt()

    @Rule(Fact(query_topic='lithotripsy__therapeutic_ultrasound_'))
    def rule_lithotripsy__therapeutic_ultrasound_(self):
        """Lithotripsy is a medical technology that uses focused ultrasound waves to treat diseases by blasting or breaking down bladder stones or calcium oxalate crystals. High-energy ultrasound waves are directed to the affected areas."""
        self.response = {
            'concept': 'Lithotripsy (Therapeutic Ultrasound)',
            'explanation': """Lithotripsy is a medical technology that uses focused ultrasound waves to treat diseases by blasting or breaking down bladder stones or calcium oxalate crystals. High-energy ultrasound waves are directed to the affected areas.""",
            'topic': 'Physics',
            'subtopic': 'Medical Applications of Ultrasound',
            'examples': ["Blasting of bladder stones or calcium oxalate crystals by sending ultrasound waves to places where bladder stones are found.", "Instrument used for blasting bladder stones by using ultrasound waves."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound_wave_interaction_with_air_gaps'))
    def rule_ultrasound_wave_interaction_with_air_gaps(self):
        """High frequency ultrasound waves, when traveling through a solid medium, will not penetrate or enter an air gap they encounter. This principle allows for the detection of voids."""
        self.response = {
            'concept': 'Ultrasound Wave Interaction with Air Gaps',
            'explanation': """High frequency ultrasound waves, when traveling through a solid medium, will not penetrate or enter an air gap they encounter. This principle allows for the detection of voids.""",
            'topic': 'Physics',
            'subtopic': 'Ultrasound Waves and Applications',
            'examples': ["Detecting dangerous air gaps in solid components of airplanes.", "Detecting fractures in solid components of airplanes."]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound_soldering'))
    def rule_ultrasound_soldering(self):
        """Ultrasound waves can be used to solder metals by placing them in contact and impinging the area with ultrasound waves. The resulting vibrations cause the metals to rub, generating heat that melts them at the contact point, thus soldering them together."""
        self.response = {
            'concept': 'Ultrasound Soldering',
            'explanation': """Ultrasound waves can be used to solder metals by placing them in contact and impinging the area with ultrasound waves. The resulting vibrations cause the metals to rub, generating heat that melts them at the contact point, thus soldering them together.""",
            'topic': 'Physics',
            'subtopic': 'Ultrasound Applications',
            'examples': ["Soldering two metal pieces together using ultrasonic vibrations.", "Joining metals at their contact points by ultrasonically induced friction and heat."]
        }
        self.halt()

    @Rule(Fact(query_topic='musical_instruments'))
    def rule_musical_instruments(self):
        """Musical instruments are devices specifically designed to generate sounds that are pleasing to the ear. They achieve this by producing periodic (regular, repeating) vibrations."""
        self.response = {
            'concept': 'Musical Instruments',
            'explanation': """Musical instruments are devices specifically designed to generate sounds that are pleasing to the ear. They achieve this by producing periodic (regular, repeating) vibrations.""",
            'topic': 'Physics',
            'subtopic': 'Sound and Musical Instruments',
            'examples': ["A violin producing a pleasing melody.", "A piano playing a musical piece.", "A tuning fork generating a pure, periodic tone."]
        }
        self.halt()

    @Rule(Fact(query_topic='distinction_between_musical_sound_and_noise'))
    def rule_distinction_between_musical_sound_and_noise(self):
        """Musical sounds are characterized by waveforms that show repeating patterns, indicating periodic vibrations. In contrast, noise is characterized by waveforms that do not show a repeating pattern and are composed of irregular vibrations."""
        self.response = {
            'concept': 'Distinction Between Musical Sound and Noise',
            'explanation': """Musical sounds are characterized by waveforms that show repeating patterns, indicating periodic vibrations. In contrast, noise is characterized by waveforms that do not show a repeating pattern and are composed of irregular vibrations.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waveforms',
            'examples': ["The sound of a violin (repeating waveform).", "The sound of machinery in a factory (irregular waveform).", "The sound of a piano (repeating waveform)."]
        }
        self.halt()

    @Rule(Fact(query_topic='main_types_of_musical_instruments'))
    def rule_main_types_of_musical_instruments(self):
        """Musical instruments are primarily classified into three main categories based on their sound production mechanism."""
        self.response = {
            'concept': 'Main Types of Musical Instruments',
            'explanation': """Musical instruments are primarily classified into three main categories based on their sound production mechanism.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments Classification',
            'examples': ["String instruments", "Percussion instruments", "Wind instruments"]
        }
        self.halt()

    @Rule(Fact(query_topic='string_instruments'))
    def rule_string_instruments(self):
        """String instruments are musical instruments that produce sound through the vibrations of one or more stretched strings."""
        self.response = {
            'concept': 'String Instruments',
            'explanation': """String instruments are musical instruments that produce sound through the vibrations of one or more stretched strings.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments Classification',
            'examples': ["Violin", "Guitar", "Cello"]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_pitch_of_a_vibrating_string'))
    def rule_factors_affecting_pitch_of_a_vibrating_string(self):
        """The pitch of a sound produced by a vibrating string is influenced by its length, the tension applied to the string (how much it is stretched), and the mass per unit length of the string."""
        self.response = {
            'concept': 'Factors Affecting Pitch of a Vibrating String',
            'explanation': """The pitch of a sound produced by a vibrating string is influenced by its length, the tension applied to the string (how much it is stretched), and the mass per unit length of the string.""",
            'topic': 'Physics',
            'subtopic': 'Waves and Sound / Musical Instruments',
            'examples': ["Shortening a guitar string by pressing on a fret increases its pitch", "Tightening a violin string raises its pitch", "A thicker bass string (higher mass per unit length) produces a lower pitch than a thinner guitar string of the same length and tension"]
        }
        self.halt()

    @Rule(Fact(query_topic='percussion_instruments'))
    def rule_percussion_instruments(self):
        """Percussion instruments are musical instruments that generate sound through the vibration of stretched membranes, metal rods, or metal plates. These instruments produce sound when they are tapped or struck."""
        self.response = {
            'concept': 'Percussion Instruments',
            'explanation': """Percussion instruments are musical instruments that generate sound through the vibration of stretched membranes, metal rods, or metal plates. These instruments produce sound when they are tapped or struck.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments / Sound',
            'examples': ["Thabla (vibrating stretched membrane)", "Xylophone (vibrating metal rods)", "Bell (vibrating metal plates)"]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch_in_percussion_instruments'))
    def rule_pitch_in_percussion_instruments(self):
        """For percussion instruments, the pitch of the sound produced depends on the area and the tension of the vibrating membrane or metal plate."""
        self.response = {
            'concept': 'Pitch in Percussion Instruments',
            'explanation': """For percussion instruments, the pitch of the sound produced depends on the area and the tension of the vibrating membrane or metal plate.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments / Sound',
            'examples': ["A larger drum membrane typically produces a lower pitch", "Tightening the skin of a drum (increasing tension) raises its pitch", "The size of a gong or cymbal influences its characteristic pitch"]
        }
        self.halt()

    @Rule(Fact(query_topic='wind_instruments'))
    def rule_wind_instruments(self):
        """Wind instruments are musical instruments that generate sound by the vibrations of air columns within them."""
        self.response = {
            'concept': 'Wind Instruments',
            'explanation': """Wind instruments are musical instruments that generate sound by the vibrations of air columns within them.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments / Sound',
            'examples': ["Flute", "Saxophone", "Trumpet"]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch_in_wind_instruments'))
    def rule_pitch_in_wind_instruments(self):
        """The pitch of the sound produced by wind instruments depends on the length of the vibrating air column within the instrument."""
        self.response = {
            'concept': 'Pitch in Wind Instruments',
            'explanation': """The pitch of the sound produced by wind instruments depends on the length of the vibrating air column within the instrument.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments / Sound',
            'examples': ["Changing finger positions on a flute alters the effective length of the air column to produce different notes", "Extending the slide of a trombone lengthens the air column, lowering the pitch", "A clarinet produces different pitches by opening and closing keys, which changes the air column length"]
        }
        self.halt()

    @Rule(Fact(query_topic='frequency_of_vibration'))
    def rule_frequency_of_vibration(self):
        """Frequency is a measure of how many vibrations or cycles occur in a given unit of time. It is calculated as the total number of vibrations divided by the total time taken."""
        self.response = {
            'concept': 'Frequency of Vibration',
            'explanation': """Frequency is a measure of how many vibrations or cycles occur in a given unit of time. It is calculated as the total number of vibrations divided by the total time taken.""",
            'topic': 'Physics',
            'subtopic': 'Waves and Vibrations',
            'examples': ["If 50 vibrations occur in 5 seconds, the frequency is 10 Hz.", "The frequency of a pendulum is the number of swings per second.", "A higher frequency means more vibrations per unit time."]
        }
        self.halt()

    @Rule(Fact(query_topic='wavelength__sound_waves_'))
    def rule_wavelength__sound_waves_(self):
        """In sound waves, wavelength is the physical quantity representing the distance between two consecutive compressions or two consecutive rarefactions."""
        self.response = {
            'concept': 'Wavelength (Sound Waves)',
            'explanation': """In sound waves, wavelength is the physical quantity representing the distance between two consecutive compressions or two consecutive rarefactions.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["The distance from one compression to the next is one wavelength.", "The distance between two consecutive rarefactions indicates the wavelength.", "Wavelength helps characterize the spatial extent of a sound wave."]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch_of_sound'))
    def rule_pitch_of_sound(self):
        """Pitch is a characteristic of sound that is directly dependent on its frequency. A higher frequency corresponds to a higher pitch, and a lower frequency corresponds to a lower pitch."""
        self.response = {
            'concept': 'Pitch of Sound',
            'explanation': """Pitch is a characteristic of sound that is directly dependent on its frequency. A higher frequency corresponds to a higher pitch, and a lower frequency corresponds to a lower pitch.""",
            'topic': 'Physics',
            'subtopic': 'Sound Characteristics',
            'examples': ["A soprano singer produces sounds with a high pitch (high frequency).", "A bass guitar produces notes with a low pitch (low frequency).", "Adjusting the frequency changes the perceived pitch of a sound."]
        }
        self.halt()

    @Rule(Fact(query_topic='loudness_of_sound'))
    def rule_loudness_of_sound(self):
        """Loudness is a characteristic of sound that is dependent on its amplitude. A greater amplitude corresponds to a louder sound, while a smaller amplitude results in a softer sound."""
        self.response = {
            'concept': 'Loudness of Sound',
            'explanation': """Loudness is a characteristic of sound that is dependent on its amplitude. A greater amplitude corresponds to a louder sound, while a smaller amplitude results in a softer sound.""",
            'topic': 'Physics',
            'subtopic': 'Sound Characteristics',
            'examples': ["Hitting a drum harder increases the amplitude, making the sound louder.", "Whispering produces sounds with small amplitude and low loudness.", "The amplitude of a sound wave determines how intensely we perceive it."]
        }
        self.halt()

    @Rule(Fact(query_topic='quality__timbre__of_sound'))
    def rule_quality__timbre__of_sound(self):
        """Quality or timbre is the characteristic of sound that allows us to distinguish between different musical instruments or voices producing the same musical note (same frequency and loudness). It depends on the presence and relative intensity of overtones."""
        self.response = {
            'concept': 'Quality (Timbre) of Sound',
            'explanation': """Quality or timbre is the characteristic of sound that allows us to distinguish between different musical instruments or voices producing the same musical note (same frequency and loudness). It depends on the presence and relative intensity of overtones.""",
            'topic': 'Physics',
            'subtopic': 'Sound Characteristics',
            'examples': ["Identifying a trumpet from a clarinet playing the same note demonstrates timbre.", "The distinct sound of a piano versus a violin is due to their different timbres.", "Recognizing different people's voices even when they speak at the same pitch and volume."]
        }
        self.halt()

    @Rule(Fact(query_topic='characteristics_of_electromagnetic_waves'))
    def rule_characteristics_of_electromagnetic_waves(self):
        """Electromagnetic waves possess several key characteristics, including their ability to propagate through a vacuum (not requiring a medium), traveling at the speed of light in a vacuum, and being transverse waves."""
        self.response = {
            'concept': 'Characteristics of Electromagnetic Waves',
            'explanation': """Electromagnetic waves possess several key characteristics, including their ability to propagate through a vacuum (not requiring a medium), traveling at the speed of light in a vacuum, and being transverse waves.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Waves',
            'examples': ["Light waves are electromagnetic waves and can travel through space.", "Radio waves, a type of EM wave, can travel without air.", "X-rays also do not require a medium for propagation."]
        }
        self.halt()

    @Rule(Fact(query_topic='orientation_of_fields_and_propagation_in_em_waves'))
    def rule_orientation_of_fields_and_propagation_in_em_waves(self):
        """In an electromagnetic wave, the oscillating electric field, the oscillating magnetic field, and the direction of wave propagation are all mutually perpendicular to each other."""
        self.response = {
            'concept': 'Orientation of Fields and Propagation in EM Waves',
            'explanation': """In an electromagnetic wave, the oscillating electric field, the oscillating magnetic field, and the direction of wave propagation are all mutually perpendicular to each other.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Waves',
            'examples': ["The electric field is at a 90-degree angle to the magnetic field.", "Both the electric and magnetic fields are perpendicular to the direction the wave is moving.", "If the EM wave travels along the x-axis, the electric field might be along the y-axis and the magnetic field along the z-axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='wavelength__transverse_waves_'))
    def rule_wavelength__transverse_waves_(self):
        """For a transverse wave, wavelength is defined as the distance between two consecutive corresponding points on the wave that are in phase, such as two consecutive crests, two consecutive troughs, or two identical points on successive cycles."""
        self.response = {
            'concept': 'Wavelength (Transverse Waves)',
            'explanation': """For a transverse wave, wavelength is defined as the distance between two consecutive corresponding points on the wave that are in phase, such as two consecutive crests, two consecutive troughs, or two identical points on successive cycles.""",
            'topic': 'Physics',
            'subtopic': 'Transverse Waves',
            'examples': ["The distance between point D and point E (assuming they are consecutive crests or troughs in the figure) represents one wavelength.", "The distance from one crest to the next crest on a water wave.", "Measuring the distance between two identical points on successive cycles of a wave on a string."]
        }
        self.halt()

    @Rule(Fact(query_topic='classification_of_musical_instruments'))
    def rule_classification_of_musical_instruments(self):
        """Musical instruments are categorized based on the primary method they use to produce sound, such as vibrating strings, striking objects, or vibrating columns of air."""
        self.response = {
            'concept': 'Classification of Musical Instruments',
            'explanation': """Musical instruments are categorized based on the primary method they use to produce sound, such as vibrating strings, striking objects, or vibrating columns of air.""",
            'topic': 'Physics',
            'subtopic': 'Musical Instruments',
            'examples': ["String instruments include the guitar and violin.", "Percussion instruments include drums and cymbals.", "Wind instruments include the flute and trumpet."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_frequency_of_string_instruments'))
    def rule_factors_affecting_frequency_of_string_instruments(self):
        """The frequency of the sound generated by a string instrument depends on several factors of the vibrating string, including its length, tension, and mass per unit length (or thickness)."""
        self.response = {
            'concept': 'Factors Affecting Frequency of String Instruments',
            'explanation': """The frequency of the sound generated by a string instrument depends on several factors of the vibrating string, including its length, tension, and mass per unit length (or thickness).""",
            'topic': 'Physics',
            'subtopic': 'Musical Acoustics',
            'examples': ["Shorter strings produce higher frequencies (higher notes).", "Tighter strings produce higher frequencies.", "Thinner strings produce higher frequencies than thicker strings of the same length and tension."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_frequency_of_wind_instruments'))
    def rule_factors_affecting_frequency_of_wind_instruments(self):
        """The frequency of the sound generated by a wind instrument primarily depends on the effective length of the vibrating air column within the instrument and, to a lesser extent, the temperature of the air."""
        self.response = {
            'concept': 'Factors Affecting Frequency of Wind Instruments',
            'explanation': """The frequency of the sound generated by a wind instrument primarily depends on the effective length of the vibrating air column within the instrument and, to a lesser extent, the temperature of the air.""",
            'topic': 'Physics',
            'subtopic': 'Musical Acoustics',
            'examples': ["Opening or closing holes on a flute changes the effective length of the air column, altering the frequency.", "Longer air columns produce lower frequencies.", "The speed of sound in air (affected by temperature) influences the frequency produced."]
        }
        self.halt()

    @Rule(Fact(query_topic='factors_affecting_frequency_of_percussion_instruments'))
    def rule_factors_affecting_frequency_of_percussion_instruments(self):
        """The frequency of the sound generated by percussion instruments depends on factors such as the size, shape, material, and for membrane instruments, the tension of the vibrating surface."""
        self.response = {
            'concept': 'Factors Affecting Frequency of Percussion Instruments',
            'explanation': """The frequency of the sound generated by percussion instruments depends on factors such as the size, shape, material, and for membrane instruments, the tension of the vibrating surface.""",
            'topic': 'Physics',
            'subtopic': 'Musical Acoustics',
            'examples': ["Smaller drums produce higher frequencies than larger drums.", "Tightening a drumhead increases the frequency of the sound.", "Different materials (e.g., wood vs. metal) for xylophone bars produce different frequencies."]
        }
        self.halt()

    @Rule(Fact(query_topic='wave'))
    def rule_wave(self):
        """A disturbance traveling in a medium or in space."""
        self.response = {
            'concept': 'Wave',
            'explanation': """A disturbance traveling in a medium or in space.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Light traveling from the sun to Earth", "Sound traveling through air", "Although lightning and thunder both happen at the same time, there is a delay between seeing the light and hearing the sound of thunder."]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_wave'))
    def rule_mechanical_wave(self):
        """Waves that require a material medium to travel."""
        self.response = {
            'concept': 'Mechanical Wave',
            'explanation': """Waves that require a material medium to travel.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Sound waves in air", "Water waves on the surface of a pond", "Seismic waves traveling through the Earth"]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_wave'))
    def rule_transverse_wave(self):
        """Waves that propagate in a direction perpendicular to the direction of particle motion."""
        self.response = {
            'concept': 'Transverse Wave',
            'explanation': """Waves that propagate in a direction perpendicular to the direction of particle motion.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Light waves", "Waves on a stretched string", "Ripples on the surface of water"]
        }
        self.halt()

    @Rule(Fact(query_topic='longitudinal_wave'))
    def rule_longitudinal_wave(self):
        """Waves that propagate in the same direction as the particle motion."""
        self.response = {
            'concept': 'Longitudinal Wave',
            'explanation': """Waves that propagate in the same direction as the particle motion.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Sound waves", "P-waves (primary waves) of an earthquake", "Waves created by compressing and stretching a Slinky"]
        }
        self.halt()

    @Rule(Fact(query_topic='period_of_oscillation'))
    def rule_period_of_oscillation(self):
        """The time taken by one particle to complete a single oscillation."""
        self.response = {
            'concept': 'Period of Oscillation',
            'explanation': """The time taken by one particle to complete a single oscillation.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["If a pendulum swings back and forth in 2 seconds, its period is 2s", "The time taken for one complete wave cycle to pass a fixed point", "The duration of a single vibration of a guitar string"]
        }
        self.halt()

    @Rule(Fact(query_topic='frequency'))
    def rule_frequency(self):
        """The number of oscillations of a single particle in one second."""
        self.response = {
            'concept': 'Frequency',
            'explanation': """The number of oscillations of a single particle in one second.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["A wave completing 10 oscillations per second has a frequency of 10 Hz", "The number of times a tuning fork vibrates in one second", "The rate at which a radio wave oscillates"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_wave'))
    def rule_electromagnetic_wave(self):
        """Waves that do not need a material medium for propagation and can travel through a vacuum."""
        self.response = {
            'concept': 'Electromagnetic Wave',
            'explanation': """Waves that do not need a material medium for propagation and can travel through a vacuum.""",
            'topic': 'Physics',
            'subtopic': 'Waves and their Applications',
            'examples': ["Radio waves used for communication", "Microwaves in an oven", "Visible light from the sun"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_wave__type_'))
    def rule_sound_wave__type_(self):
        """Sound waves are a specific type of longitudinal wave."""
        self.response = {
            'concept': 'Sound Wave (Type)',
            'explanation': """Sound waves are a specific type of longitudinal wave.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Speech generated by vocal cords", "Music produced by instruments", "The rumble of thunder"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_wave__medium_requirement_'))
    def rule_sound_wave__medium_requirement_(self):
        """Sound waves need a material medium for propagation and cannot travel through a vacuum."""
        self.response = {
            'concept': 'Sound Wave (Medium Requirement)',
            'explanation': """Sound waves need a material medium for propagation and cannot travel through a vacuum.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Sound cannot be heard in the vacuum of space", "If a ringing bell is held by hand, it stops ringing as the vibrations are damped", "A bell placed inside a vacuum jar will not be heard when rung"]
        }
        self.halt()

    @Rule(Fact(query_topic='characteristics_of_sound'))
    def rule_characteristics_of_sound(self):
        """The three main distinguishing properties of sound are pitch, loudness, and quality (timbre)."""
        self.response = {
            'concept': 'Characteristics of Sound',
            'explanation': """The three main distinguishing properties of sound are pitch, loudness, and quality (timbre).""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["A high note played on a flute (pitch)", "A loud shout (loudness)", "The unique sound of a trumpet compared to a clarinet (quality)"]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch'))
    def rule_pitch(self):
        """The characteristic of sound that depends on the frequency of the wave. Higher frequency results in higher pitch."""
        self.response = {
            'concept': 'Pitch',
            'explanation': """The characteristic of sound that depends on the frequency of the wave. Higher frequency results in higher pitch.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["A soprano singer produces high-pitched sounds due to high vocal cord frequency", "A low-pitched bass guitar note has a low frequency", "The pitch of a flute changes as holes are opened or closed, altering the vibrating air column's frequency"]
        }
        self.halt()

    @Rule(Fact(query_topic='loudness'))
    def rule_loudness(self):
        """The characteristic of sound that depends on the amplitude of the wave. Larger amplitude results in louder sound."""
        self.response = {
            'concept': 'Loudness',
            'explanation': """The characteristic of sound that depends on the amplitude of the wave. Larger amplitude results in louder sound.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Shouting increases the amplitude of sound waves, making the voice louder", "A quiet whisper has a small sound wave amplitude", "Turning up the volume on a speaker increases the amplitude of the sound waves produced"]
        }
        self.halt()

    @Rule(Fact(query_topic='quality_of_sound__timbre_'))
    def rule_quality_of_sound__timbre_(self):
        """The characteristic of sound that depends on the shape of the waveform, which allows us to distinguish different sound sources even if they have the same pitch and loudness."""
        self.response = {
            'concept': 'Quality of Sound (Timbre)',
            'explanation': """The characteristic of sound that depends on the shape of the waveform, which allows us to distinguish different sound sources even if they have the same pitch and loudness.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["A piano and a guitar playing the same note sound different due to their unique waveforms", "Different human voices have distinct qualities (timbre)", "The rich sound of an orchestra is due to the combination of various instrument timbres"]
        }
        self.halt()

    @Rule(Fact(query_topic='musical_sound_vs__noise'))
    def rule_musical_sound_vs__noise(self):
        """Sounds with regular periods are generally pleasing to the ear and considered musical, while sounds without regular periods produce noise."""
        self.response = {
            'concept': 'Musical Sound vs. Noise',
            'explanation': """Sounds with regular periods are generally pleasing to the ear and considered musical, while sounds without regular periods produce noise.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["A melody played on a violin (regular period, musical sound)", "The rhythmic beat of a drum (regular period, musical sound)", "The jarring sound of a car horn (irregular period, noise)"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_production_in_musical_instruments'))
    def rule_sound_production_in_musical_instruments(self):
        """Musical instruments produce sounds through vibrations: string instruments by vibrating strings, percussion instruments by vibrating membranes, rods, or metal plates, and wind instruments by vibrating air columns."""
        self.response = {
            'concept': 'Sound Production in Musical Instruments',
            'explanation': """Musical instruments produce sounds through vibrations: string instruments by vibrating strings, percussion instruments by vibrating membranes, rods, or metal plates, and wind instruments by vibrating air columns.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["A guitar produces sound from vibrating strings", "A drum makes sound by the vibration of its membrane when struck", "A trumpet produces sound by the vibration of an air column"]
        }
        self.halt()

    @Rule(Fact(query_topic='hearing_range'))
    def rule_hearing_range(self):
        """The specific frequency range that can be perceived as sound by an animal."""
        self.response = {
            'concept': 'Hearing Range',
            'explanation': """The specific frequency range that can be perceived as sound by an animal.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Humans typically have a hearing range of 20 Hz to 20,000 Hz", "Dogs can hear higher frequencies than humans, extending into the ultrasonic range", "Elephants can perceive sounds at much lower frequencies than humans, in the infra-sound range"]
        }
        self.halt()

    @Rule(Fact(query_topic='infra_sound'))
    def rule_infra_sound(self):
        """Sounds with frequencies below 20 Hz, which is below the typical human hearing range."""
        self.response = {
            'concept': 'Infra-sound',
            'explanation': """Sounds with frequencies below 20 Hz, which is below the typical human hearing range.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Elephants use infra-sound for long-distance communication", "Large natural phenomena like earthquakes can generate infra-sound", "Some animals can detect impending storms by sensing infra-sound"]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound'))
    def rule_ultrasound(self):
        """Sounds with frequencies above 20,000 Hz, which is above the typical human hearing range."""
        self.response = {
            'concept': 'Ultrasound',
            'explanation': """Sounds with frequencies above 20,000 Hz, which is above the typical human hearing range.""",
            'topic': 'Physics',
            'subtopic': 'Sound Waves',
            'examples': ["Medical imaging (sonography) uses ultrasound to visualize internal organs", "Bats use ultrasound for echolocation to navigate and hunt in darkness", "Dog whistles produce ultrasound, which dogs can hear but humans cannot"]
        }
        self.halt()

    @Rule(Fact(query_topic='mechanical_waves'))
    def rule_mechanical_waves(self):
        """Waves that require a material medium (like air, water, or solids) to propagate and transmit energy."""
        self.response = {
            'concept': 'Mechanical waves',
            'explanation': """Waves that require a material medium (like air, water, or solids) to propagate and transmit energy.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Sound waves", "Water waves", "Seismic waves"]
        }
        self.halt()

    @Rule(Fact(query_topic='transverse_waves'))
    def rule_transverse_waves(self):
        """Waves in which the oscillations of the medium are perpendicular to the direction of wave propagation."""
        self.response = {
            'concept': 'Transverse waves',
            'explanation': """Waves in which the oscillations of the medium are perpendicular to the direction of wave propagation.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Waves on a string", "Electromagnetic waves (when considering their field components)"]
        }
        self.halt()

    @Rule(Fact(query_topic='longitudinal_waves'))
    def rule_longitudinal_waves(self):
        """Waves in which the oscillations of the medium are parallel to the direction of wave propagation."""
        self.response = {
            'concept': 'Longitudinal waves',
            'explanation': """Waves in which the oscillations of the medium are parallel to the direction of wave propagation.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Sound waves", "Compression waves in a spring"]
        }
        self.halt()

    @Rule(Fact(query_topic='period__of_a_wave_'))
    def rule_period__of_a_wave_(self):
        """The time taken for one complete oscillation or cycle of a wave to occur, measured in seconds."""
        self.response = {
            'concept': 'Period (of a wave)',
            'explanation': """The time taken for one complete oscillation or cycle of a wave to occur, measured in seconds.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["The period of a pendulum's swing", "The period of an ocean wave reaching the shore"]
        }
        self.halt()

    @Rule(Fact(query_topic='frequency__of_a_wave_'))
    def rule_frequency__of_a_wave_(self):
        """The number of complete oscillations or cycles of a wave that occur per unit time, measured in Hertz (Hz)."""
        self.response = {
            'concept': 'Frequency (of a wave)',
            'explanation': """The number of complete oscillations or cycles of a wave that occur per unit time, measured in Hertz (Hz).""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["A sound wave with a frequency of 440 Hz", "Radio waves transmit at specific frequencies"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_waves'))
    def rule_electromagnetic_waves(self):
        """Waves that consist of oscillating electric and magnetic fields, can travel through a vacuum, and do not require a material medium for propagation."""
        self.response = {
            'concept': 'Electromagnetic waves',
            'explanation': """Waves that consist of oscillating electric and magnetic fields, can travel through a vacuum, and do not require a material medium for propagation.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["Light waves", "Radio waves", "X-rays"]
        }
        self.halt()

    @Rule(Fact(query_topic='electromagnetic_spectrum'))
    def rule_electromagnetic_spectrum(self):
        """The entire range of all types of electromagnetic radiation, ordered by frequency or wavelength, including visible light and invisible forms."""
        self.response = {
            'concept': 'Electromagnetic spectrum',
            'explanation': """The entire range of all types of electromagnetic radiation, ordered by frequency or wavelength, including visible light and invisible forms.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Radio waves", "Microwaves", "Ultraviolet radiation"]
        }
        self.halt()

    @Rule(Fact(query_topic='ultraviolet_radiation'))
    def rule_ultraviolet_radiation(self):
        """A type of electromagnetic radiation with wavelengths shorter than visible light but longer than X-rays, often associated with sunburns."""
        self.response = {
            'concept': 'Ultraviolet radiation',
            'explanation': """A type of electromagnetic radiation with wavelengths shorter than visible light but longer than X-rays, often associated with sunburns.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Sunlight contains UV radiation", "UV lamps used for sterilization"]
        }
        self.halt()

    @Rule(Fact(query_topic='infrared_radiation'))
    def rule_infrared_radiation(self):
        """A type of electromagnetic radiation with wavelengths longer than visible light but shorter than microwaves, often perceived as heat."""
        self.response = {
            'concept': 'Infrared radiation',
            'explanation': """A type of electromagnetic radiation with wavelengths longer than visible light but shorter than microwaves, often perceived as heat.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Heat from a warm object", "Remote controls use infrared signals"]
        }
        self.halt()

    @Rule(Fact(query_topic='micro_waves'))
    def rule_micro_waves(self):
        """A type of electromagnetic radiation with wavelengths between infrared and radio waves, used in applications like cooking and communication."""
        self.response = {
            'concept': 'Micro waves',
            'explanation': """A type of electromagnetic radiation with wavelengths between infrared and radio waves, used in applications like cooking and communication.""",
            'topic': 'Physics',
            'subtopic': 'Electromagnetic Spectrum',
            'examples': ["Microwave ovens", "Radar systems", "Wireless LANs"]
        }
        self.halt()

    @Rule(Fact(query_topic='sound_waves'))
    def rule_sound_waves(self):
        """Mechanical waves that result from vibrations and propagate through a medium, producing the sensation of hearing."""
        self.response = {
            'concept': 'Sound waves',
            'explanation': """Mechanical waves that result from vibrations and propagate through a medium, producing the sensation of hearing.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["Human speech", "Music from an instrument", "Echoes"]
        }
        self.halt()

    @Rule(Fact(query_topic='hearing_range'))
    def rule_hearing_range(self):
        """The range of sound frequencies that an animal or human can typically detect and perceive."""
        self.response = {
            'concept': 'Hearing range',
            'explanation': """The range of sound frequencies that an animal or human can typically detect and perceive.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["Human hearing range (20 Hz to 20,000 Hz)", "Dog hearing range extends to higher frequencies"]
        }
        self.halt()

    @Rule(Fact(query_topic='infrasound'))
    def rule_infrasound(self):
        """Sound waves with frequencies below the lower limit of human audibility (typically below 20 Hz)."""
        self.response = {
            'concept': 'Infrasound',
            'explanation': """Sound waves with frequencies below the lower limit of human audibility (typically below 20 Hz).""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["Elephant communication", "Seismic waves from earthquakes"]
        }
        self.halt()

    @Rule(Fact(query_topic='ultrasound'))
    def rule_ultrasound(self):
        """Sound waves with frequencies above the upper limit of human audibility (typically above 20,000 Hz)."""
        self.response = {
            'concept': 'Ultrasound',
            'explanation': """Sound waves with frequencies above the upper limit of human audibility (typically above 20,000 Hz).""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["Medical imaging (sonography)", "Bat echolocation"]
        }
        self.halt()

    @Rule(Fact(query_topic='pitch__of_sound_'))
    def rule_pitch__of_sound_(self):
        """The perceptual property of sounds that allows their ordering on a frequency-related scale; primarily determined by the frequency of the sound wave."""
        self.response = {
            'concept': 'Pitch (of sound)',
            'explanation': """The perceptual property of sounds that allows their ordering on a frequency-related scale; primarily determined by the frequency of the sound wave.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["A high pitch note from a flute", "A low pitch sound from a bass drum"]
        }
        self.halt()

    @Rule(Fact(query_topic='quality_of_sound'))
    def rule_quality_of_sound(self):
        """The characteristic of a sound (also known as timbre) that distinguishes it from other sounds of the same pitch and loudness, often due to the waveform and overtone structure."""
        self.response = {
            'concept': 'Quality of sound',
            'explanation': """The characteristic of a sound (also known as timbre) that distinguishes it from other sounds of the same pitch and loudness, often due to the waveform and overtone structure.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["The difference between a violin and a piano playing the same note", "Distinguishing voices of different people"]
        }
        self.halt()

    @Rule(Fact(query_topic='loudness__of_sound_'))
    def rule_loudness__of_sound_(self):
        """The perceptual property of sounds that is related to the intensity or amplitude of the sound wave, determining how strong or weak a sound seems."""
        self.response = {
            'concept': 'Loudness (of sound)',
            'explanation': """The perceptual property of sounds that is related to the intensity or amplitude of the sound wave, determining how strong or weak a sound seems.""",
            'topic': 'Physics',
            'subtopic': 'Sound',
            'examples': ["A loud explosion", "A quiet whisper"]
        }
        self.halt()

    @Rule(Fact(query_topic='amplitude__of_a_wave_'))
    def rule_amplitude__of_a_wave_(self):
        """The maximum displacement or distance moved by a point on a vibrating body or wave from its equilibrium (rest) position."""
        self.response = {
            'concept': 'Amplitude (of a wave)',
            'explanation': """The maximum displacement or distance moved by a point on a vibrating body or wave from its equilibrium (rest) position.""",
            'topic': 'Physics',
            'subtopic': 'Waves',
            'examples': ["The height of a water wave from its mean level", "The extent of a pendulum's swing", "The intensity of a sound wave"]
        }
        self.halt()

    @Rule(Fact(query_topic='visual_sensation'))
    def rule_visual_sensation(self):
        """The ability to perceive objects, which is achieved when light from an object reaches our eyes."""
        self.response = {
            'concept': 'Visual Sensation',
            'explanation': """The ability to perceive objects, which is achieved when light from an object reaches our eyes.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Seeing a book because light reflects off it", "Inability to see in complete darkness"]
        }
        self.halt()

    @Rule(Fact(query_topic='luminous_objects'))
    def rule_luminous_objects(self):
        """Objects that produce and emit their own light, allowing them to be seen directly."""
        self.response = {
            'concept': 'Luminous objects',
            'explanation': """Objects that produce and emit their own light, allowing them to be seen directly.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["a candle flame", "a light bulb", "the Sun"]
        }
        self.halt()

    @Rule(Fact(query_topic='non_luminous_objects'))
    def rule_non_luminous_objects(self):
        """Objects that do not emit their own light but are seen when light from another source falls on them and is reflected into our eyes."""
        self.response = {
            'concept': 'Non-luminous objects',
            'explanation': """Objects that do not emit their own light but are seen when light from another source falls on them and is reflected into our eyes.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["a book", "a table", "the Moon (reflects sunlight)"]
        }
        self.halt()

    @Rule(Fact(query_topic='transparent_objects'))
    def rule_transparent_objects(self):
        """Materials that allow light to pass through them completely without significant scattering, enabling clear vision of objects on the other side."""
        self.response = {
            'concept': 'Transparent objects',
            'explanation': """Materials that allow light to pass through them completely without significant scattering, enabling clear vision of objects on the other side.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["glass", "polythene", "clear water"]
        }
        self.halt()

    @Rule(Fact(query_topic='opaque_objects'))
    def rule_opaque_objects(self):
        """Materials that do not allow any light to pass through them, blocking vision completely."""
        self.response = {
            'concept': 'Opaque objects',
            'explanation': """Materials that do not allow any light to pass through them, blocking vision completely.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["stones", "bricks", "wood"]
        }
        self.halt()

    @Rule(Fact(query_topic='translucent_materials'))
    def rule_translucent_materials(self):
        """Materials that allow some light to pass through, but scatter it in irregular directions, making it impossible to see objects on the other side clearly."""
        self.response = {
            'concept': 'Translucent materials',
            'explanation': """Materials that allow some light to pass through, but scatter it in irregular directions, making it impossible to see objects on the other side clearly.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["tissue paper", "oil paper", "frosted glass"]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray'))
    def rule_light_ray(self):
        """A theoretical representation of the path and direction of light, typically depicted as a straight line with an arrow in geometrical optics."""
        self.response = {
            'concept': 'Light ray',
            'explanation': """A theoretical representation of the path and direction of light, typically depicted as a straight line with an arrow in geometrical optics.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A ray of sunlight passing through a prism", "Parallel rays of light from a distant source"]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray'))
    def rule_light_ray(self):
        """A conceptual representation of the path of light, indicated by a line with an essential arrow head to show its direction."""
        self.response = {
            'concept': 'Light Ray',
            'explanation': """A conceptual representation of the path of light, indicated by a line with an essential arrow head to show its direction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A single line representing the path of light from a source", "An arrow indicating the travel direction of light", "The line 'AB' in Figure 5.3 and 5.4 before it hits the mirror"]
        }
        self.halt()

    @Rule(Fact(query_topic='light_beam'))
    def rule_light_beam(self):
        """A collection or bundle of light rays."""
        self.response = {
            'concept': 'Light Beam',
            'explanation': """A collection or bundle of light rays.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Sunlight passing through a window", "Light from a flashlight", "The collective light emitted by a car headlight"]
        }
        self.halt()

    @Rule(Fact(query_topic='parallel_light_beam'))
    def rule_parallel_light_beam(self):
        """A bundle of light rays that travel parallel to each other."""
        self.response = {
            'concept': 'Parallel Light Beam',
            'explanation': """A bundle of light rays that travel parallel to each other.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light from a laser pointer", "Rays of light from a very distant star", "Light passing through a collimator"]
        }
        self.halt()

    @Rule(Fact(query_topic='convergent_light_beam'))
    def rule_convergent_light_beam(self):
        """A bundle of light rays that meet or converge at a single point."""
        self.response = {
            'concept': 'Convergent Light Beam',
            'explanation': """A bundle of light rays that meet or converge at a single point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light focused by a convex lens", "Sunlight concentrated by a magnifying glass", "Rays gathering at a focal point"]
        }
        self.halt()

    @Rule(Fact(query_topic='divergent_light_beam'))
    def rule_divergent_light_beam(self):
        """A bundle of light rays that spread out and travel away from a given point."""
        self.response = {
            'concept': 'Divergent Light Beam',
            'explanation': """A bundle of light rays that spread out and travel away from a given point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light spreading from an incandescent light bulb", "Rays emerging from a point source", "Light after passing through a concave lens"]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_light'))
    def rule_reflection_of_light(self):
        """The phenomenon where light rays incident on a surface change their propagation direction."""
        self.response = {
            'concept': 'Reflection of Light',
            'explanation': """The phenomenon where light rays incident on a surface change their propagation direction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Seeing your image in a plane mirror", "Light bouncing off a polished metal surface", "The gleam of light from a still water surface"]
        }
        self.halt()

    @Rule(Fact(query_topic='incident_ray'))
    def rule_incident_ray(self):
        """The light ray that strikes a reflecting surface at a specific point."""
        self.response = {
            'concept': 'Incident Ray',
            'explanation': """The light ray that strikes a reflecting surface at a specific point.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["The ray AB in Figure 5.4, striking the mirror", "A laser beam hitting a mirror", "Any light ray before it is reflected"]
        }
        self.halt()

    @Rule(Fact(query_topic='reflected_ray'))
    def rule_reflected_ray(self):
        """The light ray that bounces off the reflecting surface after being incident upon it."""
        self.response = {
            'concept': 'Reflected Ray',
            'explanation': """The light ray that bounces off the reflecting surface after being incident upon it.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["The ray BC in Figure 5.4, after leaving the mirror", "The light that travels from your mirror to your eyes", "BA in Figure 5.3, reflected from a perpendicular incidence"]
        }
        self.halt()

    @Rule(Fact(query_topic='normal__to_a_reflecting_surface_'))
    def rule_normal__to_a_reflecting_surface_(self):
        """An imaginary line drawn perpendicular (at 90 degrees) to the reflecting surface at the point where the incident ray strikes."""
        self.response = {
            'concept': 'Normal (to a reflecting surface)',
            'explanation': """An imaginary line drawn perpendicular (at 90 degrees) to the reflecting surface at the point where the incident ray strikes.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["The line BX in Figure 5.4, at point B on the mirror", "A perpendicular line to the mirror surface at the point of impact", "An orthogonal line to the interface between two media"]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_incidence__i_'))
    def rule_angle_of_incidence__i_(self):
        """The angle formed between the incident ray and the normal at the point of incidence."""
        self.response = {
            'concept': 'Angle of Incidence (i)',
            'explanation': """The angle formed between the incident ray and the normal at the point of incidence.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["Angle ABX in Figure 5.4", "The angle a laser beam makes with the normal when it hits a mirror", "If the incident ray is along the normal, the angle of incidence is 0 degrees"]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_reflection__r_'))
    def rule_angle_of_reflection__r_(self):
        """The angle formed between the reflected ray and the normal at the point of incidence."""
        self.response = {
            'concept': 'Angle of Reflection (r)',
            'explanation': """The angle formed between the reflected ray and the normal at the point of incidence.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["Angle CBX in Figure 5.4", "The angle the reflected light makes with the normal", "If the light reflects back along the normal, the angle of reflection is 0 degrees"]
        }
        self.halt()

    @Rule(Fact(query_topic='first_law_of_reflection'))
    def rule_first_law_of_reflection(self):
        """States that the incident ray, the reflected ray, and the normal at the point of incidence all lie on the same plane."""
        self.response = {
            'concept': 'First Law of Reflection',
            'explanation': """States that the incident ray, the reflected ray, and the normal at the point of incidence all lie on the same plane.""",
            'topic': 'Physics',
            'subtopic': 'Laws of Reflection',
            'examples': ["Imagine all three lines drawn on a single flat piece of paper", "The entire reflection event occurs within a 2D plane", "No part of the reflection process goes 'into' or 'out of' the surface plane"]
        }
        self.halt()

    @Rule(Fact(query_topic='second_law_of_reflection'))
    def rule_second_law_of_reflection(self):
        """States that the angle of incidence is equal to the angle of reflection."""
        self.response = {
            'concept': 'Second Law of Reflection',
            'explanation': """States that the angle of incidence is equal to the angle of reflection.""",
            'topic': 'Physics',
            'subtopic': 'Laws of Reflection',
            'examples': ["If the angle of incidence (i) is 30 degrees, then the angle of reflection (r) will also be 30 degrees", "Light hitting a mirror at a 45-degree angle to the normal will reflect at a 45-degree angle", "i = r"]
        }
        self.halt()

    @Rule(Fact(query_topic='law_of_reflection'))
    def rule_law_of_reflection(self):
        """The angle of incidence (i) is equal to the angle of reflection (r). This is a fundamental principle governing how light rays bounce off a surface."""
        self.response = {
            'concept': 'Law of Reflection',
            'explanation': """The angle of incidence (i) is equal to the angle of reflection (r). This is a fundamental principle governing how light rays bounce off a surface.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Reflection',
            'examples': ["A light ray hitting a mirror at 45 degrees to the normal will reflect at 45 degrees.", "When a laser beam strikes a smooth, shiny surface, its angle of entry and exit are identical."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_a_plane_mirror'))
    def rule_image_formation_by_a_plane_mirror(self):
        """When a point object is placed in front of a plane mirror, light rays from the object propagate towards the mirror, reflect, and then reach an observer's eye. The observer perceives these reflected rays as originating from a point behind the mirror, which forms the image."""
        self.response = {
            'concept': 'Image Formation by a Plane Mirror',
            'explanation': """When a point object is placed in front of a plane mirror, light rays from the object propagate towards the mirror, reflect, and then reach an observer's eye. The observer perceives these reflected rays as originating from a point behind the mirror, which forms the image.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Plane Mirrors',
            'examples': ["Seeing your own reflection in a bathroom mirror.", "The image of a tree reflected in a calm pond."]
        }
        self.halt()

    @Rule(Fact(query_topic='virtual_image'))
    def rule_virtual_image(self):
        """A virtual image is an image where no actual light rays pass through its location. Because there are no light rays at the image's position, it cannot be projected onto a screen. All images formed by plane mirrors are virtual."""
        self.response = {
            'concept': 'Virtual Image',
            'explanation': """A virtual image is an image where no actual light rays pass through its location. Because there are no light rays at the image's position, it cannot be projected onto a screen. All images formed by plane mirrors are virtual.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Plane Mirrors',
            'examples': ["The image of a person looking into a dressing table mirror.", "The reflection of clouds in a glass window.", "The apparent image of an object when viewed through a magnifying glass."]
        }
        self.halt()

    @Rule(Fact(query_topic='object_and_image_distance_in_plane_mirrors'))
    def rule_object_and_image_distance_in_plane_mirrors(self):
        """For a plane mirror, the distance from the object to the mirror (object distance) is always equal to the distance from the image to the mirror (image distance)."""
        self.response = {
            'concept': 'Object and Image Distance in Plane Mirrors',
            'explanation': """For a plane mirror, the distance from the object to the mirror (object distance) is always equal to the distance from the image to the mirror (image distance).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Plane Mirrors',
            'examples': ["If you stand 1 meter in front of a plane mirror, your image will appear to be 1 meter behind the mirror.", "A candle placed 20 cm from a plane mirror will produce an image that is 20 cm behind the mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='lateral_inversion_by_plane_mirrors'))
    def rule_lateral_inversion_by_plane_mirrors(self):
        """Images formed by plane mirrors are identical to their objects but are laterally inverted. This means the right side of the object appears as the left side of the image, and vice versa."""
        self.response = {
            'concept': 'Lateral Inversion by Plane Mirrors',
            'explanation': """Images formed by plane mirrors are identical to their objects but are laterally inverted. This means the right side of the object appears as the left side of the image, and vice versa.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Plane Mirrors',
            'examples': ["The word 'AMBULANCE' is often written inverted on the front of ambulances (ECNALUBMA) so it appears correctly in a vehicle's rear-view mirror.", "If you raise your right hand while looking in a plane mirror, your reflection will appear to raise its left hand.", "Text written on a piece of paper will appear reversed when viewed in a plane mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_and_characteristics_of_convex_mirrors'))
    def rule_uses_and_characteristics_of_convex_mirrors(self):
        """Convex mirrors are curved mirrors used to provide a wide field of view, making a large area appear as a small image. They are commonly utilized as rear-view mirrors in vehicles and as security mirrors in shops."""
        self.response = {
            'concept': 'Uses and Characteristics of Convex Mirrors',
            'explanation': """Convex mirrors are curved mirrors used to provide a wide field of view, making a large area appear as a small image. They are commonly utilized as rear-view mirrors in vehicles and as security mirrors in shops.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Curved Mirrors',
            'examples': ["Rear-view mirrors on cars and motorcycles.", "Security mirrors installed in convenience stores to observe a large area.", "Mirrors placed at blind corners in parking garages."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_concave_mirrors'))
    def rule_uses_of_concave_mirrors(self):
        """Concave mirrors are a type of curved mirror used by dentists for specific applications. (The excerpt does not elaborate further on the exact function for dentists)."""
        self.response = {
            'concept': 'Uses of Concave Mirrors',
            'explanation': """Concave mirrors are a type of curved mirror used by dentists for specific applications. (The excerpt does not elaborate further on the exact function for dentists).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Curved Mirrors',
            'examples': ["A dentist using a concave mirror to examine a patient's teeth.", "Some shaving mirrors are concave to provide a magnified reflection."]
        }
        self.halt()

    @Rule(Fact(query_topic='uses_of_concave_mirrors'))
    def rule_uses_of_concave_mirrors(self):
        """Concave mirrors are utilized when an enlarged image is desired, such as for dental examinations or for shaving, leveraging their ability to produce magnified reflections."""
        self.response = {
            'concept': 'Uses of Concave Mirrors',
            'explanation': """Concave mirrors are utilized when an enlarged image is desired, such as for dental examinations or for shaving, leveraging their ability to produce magnified reflections.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Applications of Curved Mirrors',
            'examples': ["Dentists use them to view inside patients' mouths.", "Used for shaving to see an enlarged view of the face.", "To obtain enlarged images of teeth."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_properties_of_concave_mirrors'))
    def rule_image_properties_of_concave_mirrors(self):
        """Concave mirrors possess the characteristic ability to produce enlarged images."""
        self.response = {
            'concept': 'Image Properties of Concave Mirrors',
            'explanation': """Concave mirrors possess the characteristic ability to produce enlarged images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Image Formation by Concave Mirrors',
            'examples': ["Figure 5.6 shows an enlarged image from a concave mirror.", "An enlarged image of a tooth when viewed by a dentist.", "The magnified reflection seen in a shaving mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_properties_of_convex_mirrors'))
    def rule_image_properties_of_convex_mirrors(self):
        """Convex mirrors are characterized by their ability to produce diminished (smaller) images."""
        self.response = {
            'concept': 'Image Properties of Convex Mirrors',
            'explanation': """Convex mirrors are characterized by their ability to produce diminished (smaller) images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Image Formation by Convex Mirrors',
            'examples': ["Figure 5.6 shows a diminished image from a convex mirror.", "Objects appearing smaller than their actual size in a convex mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='curved_mirrors'))
    def rule_curved_mirrors(self):
        """Mirrors that have reflecting surfaces which are curved, rather than flat, are known as curved mirrors."""
        self.response = {
            'concept': 'Curved Mirrors',
            'explanation': """Mirrors that have reflecting surfaces which are curved, rather than flat, are known as curved mirrors.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Introduction to Curved Mirrors',
            'examples': ["Concave mirrors", "Convex mirrors", "Any non-flat mirror used for reflection"]
        }
        self.halt()

    @Rule(Fact(query_topic='spherical_mirrors'))
    def rule_spherical_mirrors(self):
        """If the curved reflecting surface of a mirror is a section of a sphere, the mirror is specifically referred to as a spherical mirror."""
        self.response = {
            'concept': 'Spherical Mirrors',
            'explanation': """If the curved reflecting surface of a mirror is a section of a sphere, the mirror is specifically referred to as a spherical mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Types of Curved Mirrors',
            'examples': ["A concave mirror formed from a part of a sphere.", "A convex mirror formed from a part of a sphere.", "Mirrors depicted in Figure 5.7 as parts of hypothetical spheres."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_curved_mirrors'))
    def rule_types_of_curved_mirrors(self):
        """Curved mirrors are primarily categorized into two main types: concave mirrors and convex mirrors."""
        self.response = {
            'concept': 'Types of Curved Mirrors',
            'explanation': """Curved mirrors are primarily categorized into two main types: concave mirrors and convex mirrors.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Classification of Curved Mirrors',
            'examples': ["Concave mirrors", "Convex mirrors"]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_description'))
    def rule_concave_mirror_description(self):
        """A concave mirror is defined by its reflecting surface, which is curved inward."""
        self.response = {
            'concept': 'Concave Mirror Description',
            'explanation': """A concave mirror is defined by its reflecting surface, which is curved inward.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Anatomy of Concave Mirrors',
            'examples': ["The inward-curving surface shown for a concave mirror in Figure 5.7.", "The inner surface of a shiny spoon.", "A mirror used by dentists which curves inward."]
        }
        self.halt()

    @Rule(Fact(query_topic='convex_mirror_description'))
    def rule_convex_mirror_description(self):
        """A convex mirror is characterized by its reflecting surface, which is curved outward."""
        self.response = {
            'concept': 'Convex Mirror Description',
            'explanation': """A convex mirror is characterized by its reflecting surface, which is curved outward.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Anatomy of Convex Mirrors',
            'examples': ["The outward-curving surface shown for a convex mirror in Figure 5.7.", "The outer surface of a shiny spoon.", "Security mirrors that curve outward."]
        }
        self.halt()

    @Rule(Fact(query_topic='centre_of_curvature__c_'))
    def rule_centre_of_curvature__c_(self):
        """The centre of curvature (C) is the central point of the hypothetical sphere from which the spherical mirror's reflecting surface is a part."""
        self.response = {
            'concept': 'Centre of Curvature (C)',
            'explanation': """The centre of curvature (C) is the central point of the hypothetical sphere from which the spherical mirror's reflecting surface is a part.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirror Terminology',
            'examples': ["Point C illustrated in Figure 5.7.", "The geometric center of the sphere that defines the mirror's curve.", "A reference point for understanding the mirror's curvature."]
        }
        self.halt()

    @Rule(Fact(query_topic='pole__p_'))
    def rule_pole__p_(self):
        """The pole (P) is defined as the central point on the reflecting surface of a curved mirror."""
        self.response = {
            'concept': 'Pole (P)',
            'explanation': """The pole (P) is defined as the central point on the reflecting surface of a curved mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirror Terminology',
            'examples': ["Point P illustrated in Figure 5.7.", "The exact midpoint of the mirror's surface.", "The point where the principal axis intersects the mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='principal_axis'))
    def rule_principal_axis(self):
        """The principal axis is an imaginary straight line that connects the pole (P) of the mirror and its centre of curvature (C). This axis is perpendicular to the mirror surface at the pole."""
        self.response = {
            'concept': 'Principal Axis',
            'explanation': """The principal axis is an imaginary straight line that connects the pole (P) of the mirror and its centre of curvature (C). This axis is perpendicular to the mirror surface at the pole.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirror Terminology',
            'examples': ["The line joining P and C in Figure 5.7.", "An axis used to define the orientation of the mirror.", "The line along which light rays often travel in optical diagrams."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_light_rays_along_principal_axis'))
    def rule_reflection_of_light_rays_along_principal_axis(self):
        """Light rays that travel along the principal axis towards a spherical mirror have an incident angle of zero, resulting in an angle of reflection that is also zero. Consequently, these rays reflect back directly along their original path."""
        self.response = {
            'concept': 'Reflection of Light Rays Along Principal Axis',
            'explanation': """Light rays that travel along the principal axis towards a spherical mirror have an incident angle of zero, resulting in an angle of reflection that is also zero. Consequently, these rays reflect back directly along their original path.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Ray Tracing in Spherical Mirrors',
            'examples': ["A laser beam directed precisely along the principal axis reflecting back on itself.", "Light passing through the center of curvature and reflecting back.", "Rays hitting the mirror perpendicularly at the pole P."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_parallel_rays_by_concave_mirror'))
    def rule_reflection_of_parallel_rays_by_concave_mirror(self):
        """Light rays arriving parallel to the principal axis of a concave mirror converge and pass through a single point on the principal axis after reflecting from the mirror. If a screen is positioned at this point, a small bright spot can be observed."""
        self.response = {
            'concept': 'Reflection of Parallel Rays by Concave Mirror',
            'explanation': """Light rays arriving parallel to the principal axis of a concave mirror converge and pass through a single point on the principal axis after reflecting from the mirror. If a screen is positioned at this point, a small bright spot can be observed.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Ray Tracing and Focal Point',
            'examples': ["Sunlight rays focused by a concave mirror to create a hot spot.", "A parallel beam of light from a distant source converging to a single point.", "The formation of a small bright spot on a screen placed at the point of convergence."]
        }
        self.halt()

    @Rule(Fact(query_topic='focus__focal_point__of_a_concave_mirror'))
    def rule_focus__focal_point__of_a_concave_mirror(self):
        """For a concave mirror, rays of light coming parallel to the principal axis converge at a single point after reflection. This point is known as the focus or focal point (F)."""
        self.response = {
            'concept': 'Focus (Focal Point) of a Concave Mirror',
            'explanation': """For a concave mirror, rays of light coming parallel to the principal axis converge at a single point after reflection. This point is known as the focus or focal point (F).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Concave Mirrors',
            'examples': ["Sunlight (parallel rays) falling on a concave mirror converges at its focal point.", "A parabolic satellite dish, a type of concave mirror, concentrates incoming parallel radio waves at its focal point.", "Figure 5.8 illustrates parallel rays converging at point F after reflecting off a concave mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='focus__focal_point__of_a_convex_mirror'))
    def rule_focus__focal_point__of_a_convex_mirror(self):
        """For a convex mirror, rays of light coming parallel to the principal axis are reflected as a divergent beam. These divergent reflected rays appear to be coming from a point behind the mirror, which is known as the focus or focal point (F)."""
        self.response = {
            'concept': 'Focus (Focal Point) of a Convex Mirror',
            'explanation': """For a convex mirror, rays of light coming parallel to the principal axis are reflected as a divergent beam. These divergent reflected rays appear to be coming from a point behind the mirror, which is known as the focus or focal point (F).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Convex Mirrors',
            'examples': ["Light reflecting off a convex rearview mirror appears to originate from a virtual focal point behind the mirror.", "A security mirror in a shop, which is convex, makes objects appear smaller because the reflected light seems to diverge from its virtual focal point.", "Figure 5.9 shows parallel rays reflecting divergently from a convex mirror, appearing to come from point F."]
        }
        self.halt()

    @Rule(Fact(query_topic='location_of_the_focal_point'))
    def rule_location_of_the_focal_point(self):
        """The focal point (F) of any spherical mirror is situated at the mid-point on the line connecting the pole (P) and the centre of curvature (C) of the mirror."""
        self.response = {
            'concept': 'Location of the Focal Point',
            'explanation': """The focal point (F) of any spherical mirror is situated at the mid-point on the line connecting the pole (P) and the centre of curvature (C) of the mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors',
            'examples': ["If the pole is at 0 cm and the center of curvature is at 20 cm, the focal point is at 10 cm.", "For a mirror with a radius of curvature of 30 cm, its focal point lies 15 cm from the pole.", "The focal point always bisects the distance between the pole and the center of curvature."]
        }
        self.halt()

    @Rule(Fact(query_topic='focal_length__f_'))
    def rule_focal_length__f_(self):
        """The focal length (f) of a spherical mirror is defined as the distance between the pole (P) and the focal point (F)."""
        self.response = {
            'concept': 'Focal Length (f)',
            'explanation': """The focal length (f) of a spherical mirror is defined as the distance between the pole (P) and the focal point (F).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors',
            'examples': ["If the focal point is 12 cm from the pole, the focal length is 12 cm.", "A concave mirror with a focal point 10 cm in front of it has a focal length of 10 cm.", "The focal length of a convex mirror is typically considered negative by convention."]
        }
        self.halt()

    @Rule(Fact(query_topic='radius_of_curvature__r_'))
    def rule_radius_of_curvature__r_(self):
        """The radius of curvature (r) of a spherical mirror is defined as the distance between the pole (P) and the centre of curvature (C) of the mirror."""
        self.response = {
            'concept': 'Radius of Curvature (r)',
            'explanation': """The radius of curvature (r) of a spherical mirror is defined as the distance between the pole (P) and the centre of curvature (C) of the mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors',
            'examples': ["If the center of curvature is 25 cm from the pole, the radius of curvature is 25 cm.", "A mirror that forms part of a sphere with a 40 cm radius will have a radius of curvature of 40 cm.", "The radius of curvature is the radius of the sphere from which the mirror is cut."]
        }
        self.halt()

    @Rule(Fact(query_topic='relationship_between_radius_of_curvature_and_focal_length'))
    def rule_relationship_between_radius_of_curvature_and_focal_length(self):
        """The radius of curvature (r) is exactly twice the focal length (f) for any spherical mirror, expressed as r = 2f."""
        self.response = {
            'concept': 'Relationship between Radius of Curvature and Focal Length',
            'explanation': """The radius of curvature (r) is exactly twice the focal length (f) for any spherical mirror, expressed as r = 2f.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors',
            'examples': ["A concave mirror with a focal length of 8 cm has a radius of curvature of 16 cm.", "If a convex mirror has a radius of curvature of 30 cm, its focal length will be 15 cm.", "This fundamental relationship helps in designing and understanding spherical mirrors."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_ray_rule__ray_along_principal_axis'))
    def rule_concave_mirror_ray_rule__ray_along_principal_axis(self):
        """A ray of light coming along the principal axis of a concave mirror returns along the principal axis after reflection."""
        self.response = {
            'concept': 'Concave Mirror Ray Rule: Ray along Principal Axis',
            'explanation': """A ray of light coming along the principal axis of a concave mirror returns along the principal axis after reflection.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Concave Mirrors - Ray Tracing',
            'examples': ["If a laser beam is shone precisely along the principal axis into a concave mirror, it will reflect directly back.", "A ray hitting the pole (P) along the principal axis reflects back along the same line.", "Figure 5.10 illustrates this rule, showing a ray reflecting back along the principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_ray_rule__ray_parallel_to_principal_axis'))
    def rule_concave_mirror_ray_rule__ray_parallel_to_principal_axis(self):
        """A ray of light coming parallel to the principal axis passes through the focal point (F) after being reflected by a concave mirror."""
        self.response = {
            'concept': 'Concave Mirror Ray Rule: Ray Parallel to Principal Axis',
            'explanation': """A ray of light coming parallel to the principal axis passes through the focal point (F) after being reflected by a concave mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Concave Mirrors - Ray Tracing',
            'examples': ["Sunlight, approximated as parallel rays, converges at the focal point of a concave mirror.", "In a ray diagram, an incoming horizontal ray hits the concave mirror and then passes through F.", "Figure 5.11 depicts this rule, where parallel incident rays converge at the focal point F."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_ray_rule__ray_through_focal_point'))
    def rule_concave_mirror_ray_rule__ray_through_focal_point(self):
        """A ray of light coming towards a concave mirror through the focal point (F) is reflected parallel to the principal axis."""
        self.response = {
            'concept': 'Concave Mirror Ray Rule: Ray Through Focal Point',
            'explanation': """A ray of light coming towards a concave mirror through the focal point (F) is reflected parallel to the principal axis.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Concave Mirrors - Ray Tracing',
            'examples': ["In a car headlight, a bulb placed at the focal point of a concave reflector produces a parallel beam of light.", "A ray diagram shows an incoming ray passing through point F and then reflecting horizontally.", "Figure 5.12 illustrates a ray passing through F and then reflecting parallel to the principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_ray_rule__ray_through_centre_of_curvature'))
    def rule_concave_mirror_ray_rule__ray_through_centre_of_curvature(self):
        """A ray of light coming towards a concave mirror through the center of curvature (C) is reflected back through the center of curvature."""
        self.response = {
            'concept': 'Concave Mirror Ray Rule: Ray Through Centre of Curvature',
            'explanation': """A ray of light coming towards a concave mirror through the center of curvature (C) is reflected back through the center of curvature.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Spherical Mirrors - Concave Mirrors - Ray Tracing',
            'examples': ["If a light source is placed at the center of curvature of a concave mirror, the reflected rays retrace their path to the source.", "Any ray that passes through the center of curvature strikes the mirror's surface normally (perpendicularly).", "This rule is crucial for tracing images formed by concave mirrors when the object is at C."]
        }
        self.halt()

    @Rule(Fact(query_topic='property_of_line_from_center_of_curvature_to_mirror_surface'))
    def rule_property_of_line_from_center_of_curvature_to_mirror_surface(self):
        """Any line drawn from the center of curvature to the surface of a spherical mirror is perpendicular (normal) to the mirror's surface at that point."""
        self.response = {
            'concept': 'Property of Line from Center of Curvature to Mirror Surface',
            'explanation': """Any line drawn from the center of curvature to the surface of a spherical mirror is perpendicular (normal) to the mirror's surface at that point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["A radius of a spherical mirror is always normal to its surface.", "Light rays passing through the center of curvature strike the mirror perpendicularly."]
        }
        self.halt()

    @Rule(Fact(query_topic='law_of_reflection__angle_of_incidence_and_reflection_'))
    def rule_law_of_reflection__angle_of_incidence_and_reflection_(self):
        """For any ray of light incident on a mirror, the angle of incidence (i), measured with respect to the normal to the surface, is equal to the angle of reflection (r)."""
        self.response = {
            'concept': 'Law of Reflection (Angle of Incidence and Reflection)',
            'explanation': """For any ray of light incident on a mirror, the angle of incidence (i), measured with respect to the normal to the surface, is equal to the angle of reflection (r).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Reflection',
            'examples': ["If an incident ray hits the mirror at 30 degrees to the normal, the reflected ray will also be at 30 degrees to the normal.", "The incident ray, the reflected ray, and the normal to the surface all lie in the same plane."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_rays_along_principal_axis'))
    def rule_reflection_of_rays_along_principal_axis(self):
        """Light rays that travel along the principal axis of a spherical mirror will reflect back along the same principal axis after striking the mirror."""
        self.response = {
            'concept': 'Reflection of Rays along Principal Axis',
            'explanation': """Light rays that travel along the principal axis of a spherical mirror will reflect back along the same principal axis after striking the mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors - Ray Tracing Rules',
            'examples': ["If a laser beam is aimed directly down the principal axis of a concave mirror, it retraces its path.", "A ray traveling along the principal axis is incident normally (perpendicularly) to the mirror at the pole."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_parallel_rays_by_concave_mirror'))
    def rule_reflection_of_parallel_rays_by_concave_mirror(self):
        """Light rays that travel parallel to the principal axis of a concave mirror will converge and pass through the focal point after reflection."""
        self.response = {
            'concept': 'Reflection of Parallel Rays by Concave Mirror',
            'explanation': """Light rays that travel parallel to the principal axis of a concave mirror will converge and pass through the focal point after reflection.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors - Ray Tracing Rules',
            'examples': ["Sunlight, approximated as parallel rays, focuses at the focal point of a concave mirror.", "This property is used to concentrate solar energy at a single point.", "The image of a very distant object formed by a concave mirror is located at its focal point."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection_of_rays_through_center_of_curvature_by_concave_mirror'))
    def rule_reflection_of_rays_through_center_of_curvature_by_concave_mirror(self):
        """A light ray that passes through the center of curvature of a spherical mirror strikes the mirror normally (perpendicularly) and is therefore reflected back along its original path."""
        self.response = {
            'concept': 'Reflection of Rays through Center of Curvature by Concave Mirror',
            'explanation': """A light ray that passes through the center of curvature of a spherical mirror strikes the mirror normally (perpendicularly) and is therefore reflected back along its original path.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors - Ray Tracing Rules',
            'examples': ["If a light source is placed at the center of curvature, its rays return to the source after reflection.", "This ray acts as its own normal at the point of incidence on the mirror.", "The angle of incidence for such a ray is 0 degrees, hence the angle of reflection is also 0 degrees."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_concave_mirror__object_within_focal_length_'))
    def rule_image_formation_by_concave_mirror__object_within_focal_length_(self):
        """When an object is placed between the pole (P) and the focal point (F) of a concave mirror (i.e., closer than the focal length), the mirror forms an enlarged, upright, and virtual image."""
        self.response = {
            'concept': 'Image Formation by Concave Mirror (Object within Focal Length)',
            'explanation': """When an object is placed between the pole (P) and the focal point (F) of a concave mirror (i.e., closer than the focal length), the mirror forms an enlarged, upright, and virtual image.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors - Image Properties',
            'examples': ["Looking at your face very close to a concave shaving mirror results in a large, upright reflection.", "A dentist uses a concave mirror to see an enlarged, virtual image of a patient's tooth."]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_a_real_image'))
    def rule_definition_of_a_real_image(self):
        """A real image is an image formed by the actual convergence of light rays after reflection or refraction. Real images can be projected onto a screen."""
        self.response = {
            'concept': 'Definition of a Real Image',
            'explanation': """A real image is an image formed by the actual convergence of light rays after reflection or refraction. Real images can be projected onto a screen.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Image Properties',
            'examples': ["The image projected onto a cinema screen is a real image.", "The image formed on the retina of the eye is a real image.", "An image of a distant object formed on a white screen by a concave mirror is a real image."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_determination_of_focal_length_of_concave_mirror__distant_object_method_'))
    def rule_experimental_determination_of_focal_length_of_concave_mirror__distant_object_method_(self):
        """The focal length of a concave mirror can be determined by holding it towards a distant object (e.g., a window scene) and adjusting a screen in front of it until a clear, inverted, real image of the object is formed. The distance between the mirror and the screen at this point is approximately the focal length."""
        self.response = {
            'concept': 'Experimental Determination of Focal Length of Concave Mirror (Distant Object Method)',
            'explanation': """The focal length of a concave mirror can be determined by holding it towards a distant object (e.g., a window scene) and adjusting a screen in front of it until a clear, inverted, real image of the object is formed. The distance between the mirror and the screen at this point is approximately the focal length.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors - Experiments',
            'examples': ["Using sunlight to find the focal point by focusing its rays to a sharp spot on a piece of paper.", "Measuring the distance from the mirror to the screen when a clear, upside-down image of a faraway building is formed.", "This method assumes parallel rays from the distant object converge at the focal point."]
        }
        self.halt()

    @Rule(Fact(query_topic='parallel_rays_from_distant_objects'))
    def rule_parallel_rays_from_distant_objects(self):
        """Light rays originating from objects located very far away can be considered as parallel when they reach a mirror."""
        self.response = {
            'concept': 'Parallel Rays from Distant Objects',
            'explanation': """Light rays originating from objects located very far away can be considered as parallel when they reach a mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["Light rays from the sun reaching Earth's surface.", "Light from a distant star entering a telescope.", "Rays from a far-off building reflecting off a small mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_position_for_distant_objects__concave_mirror_'))
    def rule_image_position_for_distant_objects__concave_mirror_(self):
        """When light rays from a far away object, considered parallel, strike a concave mirror, the image formed is approximately at the focal length of the mirror."""
        self.response = {
            'concept': 'Image Position for Distant Objects (Concave Mirror)',
            'explanation': """When light rays from a far away object, considered parallel, strike a concave mirror, the image formed is approximately at the focal length of the mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["Using sunlight to find the focal length of a concave mirror.", "The image of a distant mountain formed by a concave mirror is at its focal point.", "Approximating the focal length by observing the sharp image of a distant streetlight."]
        }
        self.halt()

    @Rule(Fact(query_topic='dependence_of_image_characteristics_on_object_position__concave_mirror_'))
    def rule_dependence_of_image_characteristics_on_object_position__concave_mirror_(self):
        """For a concave mirror, the specific characteristics of the image formed (its position, nature like real/virtual, and size) are entirely determined by the object's position relative to the mirror."""
        self.response = {
            'concept': 'Dependence of Image Characteristics on Object Position (Concave Mirror)',
            'explanation': """For a concave mirror, the specific characteristics of the image formed (its position, nature like real/virtual, and size) are entirely determined by the object's position relative to the mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["An object placed beyond the center of curvature forms a real, inverted, diminished image.", "An object placed between the focal point and the pole forms a virtual, upright, magnified image.", "An object placed at the center of curvature forms a real, inverted, same-size image at the center of curvature."]
        }
        self.halt()

    @Rule(Fact(query_topic='principle_of_image_formation__ray_diagrams_'))
    def rule_principle_of_image_formation__ray_diagrams_(self):
        """The image of a point object in front of a mirror is located at the point where two or more light rays originating from that object point either physically meet after reflection, or where their extended reflected paths appear to meet."""
        self.response = {
            'concept': 'Principle of Image Formation (Ray Diagrams)',
            'explanation': """The image of a point object in front of a mirror is located at the point where two or more light rays originating from that object point either physically meet after reflection, or where their extended reflected paths appear to meet.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Ray Diagrams',
            'examples': ["Drawing two standard rays (parallel to principal axis, passing through focus) to find an image.", "Locating the image of a candle flame by finding the intersection of reflected rays from its tip.", "Determining a virtual image by extending reflected rays backward until they intersect."]
        }
        self.halt()

    @Rule(Fact(query_topic='ray_tracing_for_extended_objects'))
    def rule_ray_tracing_for_extended_objects(self):
        """To accurately find the position of the image for an extended object (not a single point), it is necessary to trace light rays coming from different significant points of the object, typically the top and bottom."""
        self.response = {
            'concept': 'Ray Tracing for Extended Objects',
            'explanation': """To accurately find the position of the image for an extended object (not a single point), it is necessary to trace light rays coming from different significant points of the object, typically the top and bottom.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Ray Diagrams',
            'examples': ["Drawing rays from the top of a vertical arrow and its base to locate its full image.", "Finding the image of a candle flame by tracing rays from the tip and the base of the flame.", "Analyzing how a human body appears in a mirror by considering rays from the head and feet."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_of_object_points_on_principal_axis'))
    def rule_image_of_object_points_on_principal_axis(self):
        """If a point on an object is situated on the principal axis of a mirror, all light rays originating from that point will travel along the principal axis (or appear to) after reflection. Consequently, the image of that specific point will also be formed on the principal axis."""
        self.response = {
            'concept': 'Image of Object Points on Principal Axis',
            'explanation': """If a point on an object is situated on the principal axis of a mirror, all light rays originating from that point will travel along the principal axis (or appear to) after reflection. Consequently, the image of that specific point will also be formed on the principal axis.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Ray Diagrams',
            'examples': ["The image of the base of a vertical candle, if placed on the principal axis, will also be on the principal axis.", "A tiny dot marked directly on the principal axis will have its image also on the principal axis.", "Rays from the center of a sphere placed on the principal axis will reflect back along the principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='ray_diagram_construction_principle'))
    def rule_ray_diagram_construction_principle(self):
        """To draw the image of an object placed vertically on the principal axis, it is sufficient to draw rays from the top of the object. Any two light rays can be used, and the image of the top of the object is the point of intersection of these two rays. Ray diagrams help determine the nature of the image formed at different object distances."""
        self.response = {
            'concept': 'Ray Diagram Construction Principle',
            'explanation': """To draw the image of an object placed vertically on the principal axis, it is sufficient to draw rays from the top of the object. Any two light rays can be used, and the image of the top of the object is the point of intersection of these two rays. Ray diagrams help determine the nature of the image formed at different object distances.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Ray Diagrams',
            'examples': ["Drawing two rays from the top of an arrow to locate its image.", "Using a ray diagram to find if an image is inverted or upright.", "Determining the magnification of an image using the intersection point of reflected rays."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_between_mirror_and_focal_point__concave_mirror_'))
    def rule_image_formation__object_between_mirror_and_focal_point__concave_mirror_(self):
        """When an object is positioned between the mirror (pole) and the focal point, the image formed is virtual, upright, and larger than the object. This image cannot be formed on a screen and can only be seen by viewing through the mirror. To locate the image, trace two rays: one parallel to the principal axis (reflects through the focal point) and another through the center of curvature (reflects along its original path). Extend these reflected rays backward with dotted lines; their intersection point indicates the image location."""
        self.response = {
            'concept': 'Image Formation: Object between Mirror and Focal Point (Concave Mirror)',
            'explanation': """When an object is positioned between the mirror (pole) and the focal point, the image formed is virtual, upright, and larger than the object. This image cannot be formed on a screen and can only be seen by viewing through the mirror. To locate the image, trace two rays: one parallel to the principal axis (reflects through the focal point) and another through the center of curvature (reflects along its original path). Extend these reflected rays backward with dotted lines; their intersection point indicates the image location.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Concave Mirrors / Image Formation',
            'examples': ["The enlarged, upright image seen in a make-up mirror when held close to the face.", "A dentist using a small concave mirror to view a magnified image of a tooth.", "Observing an upright, magnified image of a thumb when it's placed very close to a concave mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='virtual_images'))
    def rule_virtual_images(self):
        """Virtual images are images that cannot be formed or projected onto a screen. They are not 'real' in the sense that light rays do not actually converge at the image location. Instead, they appear to originate from a point behind the mirror (or lens) and can only be seen by viewing through the optical device. They are formed by the apparent intersection of diverging reflected or refracted rays."""
        self.response = {
            'concept': 'Virtual Images',
            'explanation': """Virtual images are images that cannot be formed or projected onto a screen. They are not 'real' in the sense that light rays do not actually converge at the image location. Instead, they appear to originate from a point behind the mirror (or lens) and can only be seen by viewing through the optical device. They are formed by the apparent intersection of diverging reflected or refracted rays.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Image Characteristics',
            'examples': ["Your reflection in a plane mirror.", "The image produced by a convex mirror, such as a security mirror in a store.", "The image formed when looking through a magnifying glass at a distant object."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_on_the_focal_point__concave_mirror_'))
    def rule_image_formation__object_on_the_focal_point__concave_mirror_(self):
        """When an object is placed precisely on the focal point of a concave mirror, its image is formed at infinity. This occurs because any two rays originating from the top of the object and reflecting off the mirror will emerge parallel to each other. Since parallel rays never intersect, the image is considered to be formed at an infinite distance."""
        self.response = {
            'concept': 'Image Formation: Object on the Focal Point (Concave Mirror)',
            'explanation': """When an object is placed precisely on the focal point of a concave mirror, its image is formed at infinity. This occurs because any two rays originating from the top of the object and reflecting off the mirror will emerge parallel to each other. Since parallel rays never intersect, the image is considered to be formed at an infinite distance.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Concave Mirrors / Image Formation',
            'examples': ["A car headlight uses a bulb placed at the focal point of a concave reflector to produce a parallel beam of light.", "If you place an object exactly at the focal point of a concave mirror, you will not see a distinct image formed on a screen at any finite distance.", "The principle used in some searchlights where the light source is positioned at the focal point to create a strong, directed beam."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_of_an_object_placed_on_the_focal_point__f_'))
    def rule_image_of_an_object_placed_on_the_focal_point__f_(self):
        """When an object is placed on the focal point, assuming that two parallel rays meet at infinity, the image formed will be very large and inverted."""
        self.response = {
            'concept': 'Image of an object placed on the focal point (F)',
            'explanation': """When an object is placed on the focal point, assuming that two parallel rays meet at infinity, the image formed will be very large and inverted.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Parallel rays meet at infinity.", "The image produced is very large.", "The image produced is inverted."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_of_an_object_placed_between_the_center_of_curvature__c__and_the_focal_point__f_'))
    def rule_image_of_an_object_placed_between_the_center_of_curvature__c__and_the_focal_point__f_(self):
        """For an object placed between the center of curvature and the focal point, the image is real, inverted, larger than the object, and is formed beyond the center of curvature. This can be determined by considering a ray coming from the top of the object parallel to the principal axis and another ray passing through the center of curvature."""
        self.response = {
            'concept': 'Image of an object placed between the center of curvature (C) and the focal point (F)',
            'explanation': """For an object placed between the center of curvature and the focal point, the image is real, inverted, larger than the object, and is formed beyond the center of curvature. This can be determined by considering a ray coming from the top of the object parallel to the principal axis and another ray passing through the center of curvature.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Image is real and inverted.", "Image is larger than the object.", "Image is formed beyond the center of curvature."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_of_an_object_placed_on_the_center_of_curvature__c_'))
    def rule_image_of_an_object_placed_on_the_center_of_curvature__c_(self):
        """When an object is positioned at the center of curvature, the image is a real, inverted image formed directly below the center of curvature. The height of the image is equal to the height of the object. Its position can be found by considering a ray coming from the top of the object through the focal point and a ray coming parallel to the principal axis."""
        self.response = {
            'concept': 'Image of an object placed on the center of curvature (C)',
            'explanation': """When an object is positioned at the center of curvature, the image is a real, inverted image formed directly below the center of curvature. The height of the image is equal to the height of the object. Its position can be found by considering a ray coming from the top of the object through the focal point and a ray coming parallel to the principal axis.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Image is directly below the center of curvature.", "Image height is equal to object height.", "The image formed is real and inverted."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_of_an_object_placed_beyond_the_center_of_curvature__c_'))
    def rule_image_of_an_object_placed_beyond_the_center_of_curvature__c_(self):
        """To find the location of the image for an object positioned beyond the center of curvature, one can consider two rays coming from the top of the object: one parallel to the principal axis (which returns through the focal point after reflection) and the other passing through the center of curvature (which reflects back along itself)."""
        self.response = {
            'concept': 'Image of an object placed beyond the center of curvature (C)',
            'explanation': """To find the location of the image for an object positioned beyond the center of curvature, one can consider two rays coming from the top of the object: one parallel to the principal axis (which returns through the focal point after reflection) and the other passing through the center of curvature (which reflects back along itself).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Choose a ray parallel to the principal axis.", "Choose a ray passing through the center of curvature.", "The ray parallel to the principal axis returns through the focal point."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror__image_formation_for_object_beyond_center_of_curvature__c_'))
    def rule_concave_mirror__image_formation_for_object_beyond_center_of_curvature__c_(self):
        """When an object is placed at a point beyond the center of curvature (C) of a concave mirror, the image is formed between the focal point (F) and the center of curvature (C). This image is smaller than the object, inverted, and real."""
        self.response = {
            'concept': 'Concave Mirror: Image formation for Object beyond Center of Curvature (C)',
            'explanation': """When an object is placed at a point beyond the center of curvature (C) of a concave mirror, the image is formed between the focal point (F) and the center of curvature (C). This image is smaller than the object, inverted, and real.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["Image formed between C and F.", "Image is smaller than the object, inverted and real.", "Figure 5.21 illustrates this image formation."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror__image_formation_for_object_at_infinity'))
    def rule_concave_mirror__image_formation_for_object_at_infinity(self):
        """When an object is placed very far from a concave mirror, its image is formed on the focal point (F) of the mirror, on the same side as the object. This image is smaller than the object, inverted, and real (as it can be seen on a screen)."""
        self.response = {
            'concept': 'Concave Mirror: Image formation for Object at Infinity',
            'explanation': """When an object is placed very far from a concave mirror, its image is formed on the focal point (F) of the mirror, on the same side as the object. This image is smaller than the object, inverted, and real (as it can be seen on a screen).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors',
            'examples': ["Object very far from the mirror -> image formed on the focal point.", "Image is smaller than the object and is inverted.", "Since this image can be seen on a screen, it is a real image."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_within_focal_length'))
    def rule_concave_mirror_image_properties__object_within_focal_length(self):
        """If an object is placed at a distance less than the focal length from a concave mirror, the image formed is virtual, upright, and larger than the object. The image is formed at a distance greater than the object distance."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object within Focal Length',
            'explanation': """If an object is placed at a distance less than the focal length from a concave mirror, the image formed is virtual, upright, and larger than the object. The image is formed at a distance greater than the object distance.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Object distance: less than focal length.", "Image size: larger than the object.", "Image properties: virtual, upright."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_at_focal_length'))
    def rule_concave_mirror_image_properties__object_at_focal_length(self):
        """When an object is placed exactly at the focal length of a concave mirror, the image is formed at infinity."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object at Focal Length',
            'explanation': """When an object is placed exactly at the focal length of a concave mirror, the image is formed at infinity.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Position of Object: focal length.", "Position of Image: infinity."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_between_focal_point__f__and_center_of_curvature__c_'))
    def rule_concave_mirror_image_properties__object_between_focal_point__f__and_center_of_curvature__c_(self):
        """When an object is placed at a distance greater than the focal length and less than twice the focal length (i.e., between F and C) from a concave mirror, the image formed is real, inverted, and larger than the object. The image is formed beyond twice the focal length (i.e., beyond C)."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object between Focal Point (F) and Center of Curvature (C)',
            'explanation': """When an object is placed at a distance greater than the focal length and less than twice the focal length (i.e., between F and C) from a concave mirror, the image formed is real, inverted, and larger than the object. The image is formed beyond twice the focal length (i.e., beyond C).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Object distance: greater than focal length and less than twice the focal length.", "Image size: larger than the object.", "Image properties: real, inverted."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_at_center_of_curvature__c_'))
    def rule_concave_mirror_image_properties__object_at_center_of_curvature__c_(self):
        """When an object is placed at twice the focal length (i.e., at the center of curvature, C) of a concave mirror, the image formed is real, inverted, and the same size as the object. The image is also formed at twice the focal length (at C)."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object at Center of Curvature (C)',
            'explanation': """When an object is placed at twice the focal length (i.e., at the center of curvature, C) of a concave mirror, the image formed is real, inverted, and the same size as the object. The image is also formed at twice the focal length (at C).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Object distance: twice the focal length.", "Image distance: twice the focal length.", "Image properties: real, inverted, same size as the object."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_greater_than_twice_focal_length__beyond_c_'))
    def rule_concave_mirror_image_properties__object_greater_than_twice_focal_length__beyond_c_(self):
        """When an object is placed at a distance greater than twice the focal length (i.e., beyond C) from a concave mirror, the image formed is real, inverted, and smaller than the object. The image is formed between the focal length and twice the focal length (i.e., between F and C)."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object greater than twice Focal Length (beyond C)',
            'explanation': """When an object is placed at a distance greater than twice the focal length (i.e., beyond C) from a concave mirror, the image formed is real, inverted, and smaller than the object. The image is formed between the focal length and twice the focal length (i.e., between F and C).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Object distance: greater than twice focal length.", "Image distance: greater than focal length and less than twice the focal length.", "Image properties: real, inverted, smaller than the object."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_properties__object_very_far__table_summary_'))
    def rule_concave_mirror_image_properties__object_very_far__table_summary_(self):
        """When an object is placed very far from a concave mirror, its image is formed at the focal point. This image is real, inverted, and much smaller than the object."""
        self.response = {
            'concept': 'Concave Mirror Image Properties: Object Very Far (Table Summary)',
            'explanation': """When an object is placed very far from a concave mirror, its image is formed at the focal point. This image is real, inverted, and much smaller than the object.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Mirrors (Table Summary)',
            'examples': ["Position of Object: very far.", "Position of Image: at focal point.", "Image properties: real, inverted, much smaller than the object."]
        }
        self.halt()

    @Rule(Fact(query_topic='convex_mirror_reflection__rays_along_principal_axis'))
    def rule_convex_mirror_reflection__rays_along_principal_axis(self):
        """In a convex mirror, light rays that come towards the mirror along its principal axis are reflected back along the same path."""
        self.response = {
            'concept': 'Convex Mirror Reflection: Rays along Principal Axis',
            'explanation': """In a convex mirror, light rays that come towards the mirror along its principal axis are reflected back along the same path.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Mirrors',
            'examples': ["Figure 5.22(a) shows light rays coming along the principal axis.", "Rays coming towards the mirror along the principal axis are reflected back along the same path after reflection."]
        }
        self.halt()

    @Rule(Fact(query_topic='parallel_ray_reflection_by_convex_mirror'))
    def rule_parallel_ray_reflection_by_convex_mirror(self):
        """Rays coming parallel to the principal axis of a convex mirror are reflected as a divergent beam. These divergent rays appear to originate from a single point on the principal axis inside the mirror, known as its focal point."""
        self.response = {
            'concept': 'Parallel Ray Reflection by Convex Mirror',
            'explanation': """Rays coming parallel to the principal axis of a convex mirror are reflected as a divergent beam. These divergent rays appear to originate from a single point on the principal axis inside the mirror, known as its focal point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Mirrors - Ray Tracing',
            'examples': ["Sunlight (effectively parallel rays) reflecting off a convex rearview mirror spreads out.", "Light from a distant object reflecting off a convex surface will diverge."]
        }
        self.halt()

    @Rule(Fact(query_topic='focal_point_directed_ray_reflection_by_convex_mirror'))
    def rule_focal_point_directed_ray_reflection_by_convex_mirror(self):
        """A ray that approaches a convex mirror, directed towards its focal point, is reflected back along a path parallel to the principal axis."""
        self.response = {
            'concept': 'Focal Point-Directed Ray Reflection by Convex Mirror',
            'explanation': """A ray that approaches a convex mirror, directed towards its focal point, is reflected back along a path parallel to the principal axis.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Mirrors - Ray Tracing',
            'examples': ["A laser beam aimed at the virtual focal point of a convex mirror reflects parallel to the principal axis.", "Light intended to converge at the focal point before hitting the mirror will emerge parallel after reflection."]
        }
        self.halt()

    @Rule(Fact(query_topic='centre_of_curvature_directed_ray_reflection_by_convex_mirror'))
    def rule_centre_of_curvature_directed_ray_reflection_by_convex_mirror(self):
        """A ray that approaches a convex mirror, directed towards its centre of curvature, is reflected back along its original path. This is because any straight line drawn from the centre of curvature to the mirror surface is a normal (perpendicular) to the surface."""
        self.response = {
            'concept': 'Centre of Curvature-Directed Ray Reflection by Convex Mirror',
            'explanation': """A ray that approaches a convex mirror, directed towards its centre of curvature, is reflected back along its original path. This is because any straight line drawn from the centre of curvature to the mirror surface is a normal (perpendicular) to the surface.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Mirrors - Ray Tracing',
            'examples': ["If a light ray strikes a convex mirror along a line passing through its center of curvature, it retraces its path.", "A light beam sent towards the centre of curvature of a convex mirror bounces straight back."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_convex_mirrors'))
    def rule_image_formation_by_convex_mirrors(self):
        """Convex mirrors always form upright, virtual, and smaller images, regardless of the distance between the object and the mirror. They do not form real images; to view the image, one must look at the object through the convex mirror."""
        self.response = {
            'concept': 'Image Formation by Convex Mirrors',
            'explanation': """Convex mirrors always form upright, virtual, and smaller images, regardless of the distance between the object and the mirror. They do not form real images; to view the image, one must look at the object through the convex mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Mirrors - Image Characteristics',
            'examples': ["The reflection of your face in a convex rearview mirror is always upright and smaller.", "Security mirrors in shops provide a wide, virtual, and reduced view of the area.", "Looking at your reflection on the back (outer) surface of a spoon."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light'))
    def rule_refraction_of_light(self):
        """Refraction is the phenomenon where light rays bend when they pass from one medium into another, such as from air to water. This bending is the reason for various optical illusions."""
        self.response = {
            'concept': 'Refraction of Light',
            'explanation': """Refraction is the phenomenon where light rays bend when they pass from one medium into another, such as from air to water. This bending is the reason for various optical illusions.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["A pencil placed inside a glass of water appears bent when viewed from the top.", "A straw in a drink looks disconnected or broken at the water's surface.", "The apparent shallowness of objects at the bottom of a swimming pool."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light'))
    def rule_refraction_of_light(self):
        """The bending of light rays upon entering one medium from another medium with different optical properties."""
        self.response = {
            'concept': 'Refraction of Light',
            'explanation': """The bending of light rays upon entering one medium from another medium with different optical properties.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The apparent bending of a pencil placed partly in water.", "A coin at the bottom of a container of water appearing slightly raised.", "The script on a book page viewed through a block of glass appearing raised."]
        }
        self.halt()

    @Rule(Fact(query_topic='apparent_position_of_submerged_objects'))
    def rule_apparent_position_of_submerged_objects(self):
        """When light rays from an object submerged in a denser medium (like water) enter a rarer medium (like air), they bend away from the normal, causing the object to appear to be at a shallower (raised) position than its actual (real) depth."""
        self.response = {
            'concept': 'Apparent Position of Submerged Objects',
            'explanation': """When light rays from an object submerged in a denser medium (like water) enter a rarer medium (like air), they bend away from the normal, causing the object to appear to be at a shallower (raised) position than its actual (real) depth.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A coin at the bottom of a container with water appears to be slightly raised above its actual position.", "The part of a pencil inside water appears to be in a different position than the part above the water level.", "An object at the bottom of a vessel of water has an apparent depth less than its real depth."]
        }
        self.halt()

    @Rule(Fact(query_topic='conditions_for_light_refraction'))
    def rule_conditions_for_light_refraction(self):
        """Refraction of light occurs only if the light rays arrive from a direction other than at a 90-degree angle on the surface separating the two different media."""
        self.response = {
            'concept': 'Conditions for Light Refraction',
            'explanation': """Refraction of light occurs only if the light rays arrive from a direction other than at a 90-degree angle on the surface separating the two different media.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light rays entering air from water at an oblique angle will refract.", "Light rays from a pencil inside water entering air from the water surface at an angle.", "Light rays entering a block of glass from air at an angle will bend."]
        }
        self.halt()

    @Rule(Fact(query_topic='cause_of_refraction'))
    def rule_cause_of_refraction(self):
        """The primary reason for the bending of light rays (refraction) when they pass from one medium to another is the difference in the speeds of light between the two media."""
        self.response = {
            'concept': 'Cause of Refraction',
            'explanation': """The primary reason for the bending of light rays (refraction) when they pass from one medium to another is the difference in the speeds of light between the two media.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light's speed of 3 × 10⁸ ms⁻¹ in a vacuum reduces when it enters another medium.", "Light travels at a different speed in water compared to air.", "Light travels at a different speed in glass compared to air."]
        }
        self.halt()

    @Rule(Fact(query_topic='optically_denser_and_rarer_media'))
    def rule_optically_denser_and_rarer_media(self):
        """A medium in which the speed of light is lower compared to another medium is called an optically denser medium. Conversely, the medium with the higher speed of light is called an optically rarer medium."""
        self.response = {
            'concept': 'Optically Denser and Rarer Media',
            'explanation': """A medium in which the speed of light is lower compared to another medium is called an optically denser medium. Conversely, the medium with the higher speed of light is called an optically rarer medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["If light slows down when entering medium X from medium Y, then medium X is optically denser than medium Y.", "A vacuum is an optically rarer medium compared to water.", "Water is optically denser than air, as light travels slower in water."]
        }
        self.halt()

    @Rule(Fact(query_topic='speed_of_light_in_different_media'))
    def rule_speed_of_light_in_different_media(self):
        """The speed at which light travels is not constant and varies depending on the medium it propagates through. Different materials cause light to slow down to different extents."""
        self.response = {
            'concept': 'Speed of Light in Different Media',
            'explanation': """The speed at which light travels is not constant and varies depending on the medium it propagates through. Different materials cause light to slow down to different extents.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Speed of Light',
            'examples': ["Light travels at 300,000 km s-1 in air.", "Light travels at 225,000 km s-1 in water.", "Light travels at 124,000 km s-1 in diamond."]
        }
        self.halt()

    @Rule(Fact(query_topic='incident_ray'))
    def rule_incident_ray(self):
        """The incident ray is the path of a ray of light that approaches and strikes the surface separating two different media, before it enters the second medium."""
        self.response = {
            'concept': 'Incident Ray',
            'explanation': """The incident ray is the path of a ray of light that approaches and strikes the surface separating two different media, before it enters the second medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction Terminology',
            'examples': ["Line AB represents the incident ray as it travels across the block of glass from air.", "A laser beam hitting the surface of a swimming pool.", "The light from the sun striking a window pane."]
        }
        self.halt()

    @Rule(Fact(query_topic='normal_line'))
    def rule_normal_line(self):
        """The normal is an imaginary line drawn perpendicular (at a 90-degree angle) to the surface at the precise point where the incident ray strikes or exits the surface. It serves as a reference for measuring angles of incidence and refraction."""
        self.response = {
            'concept': 'Normal Line',
            'explanation': """The normal is an imaginary line drawn perpendicular (at a 90-degree angle) to the surface at the precise point where the incident ray strikes or exits the surface. It serves as a reference for measuring angles of incidence and refraction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction Terminology',
            'examples': ["Line XY is the normal drawn to the glass surface PQ at point B.", "A line drawn perpendicular to a water-air interface at the point where light enters.", "The line at 90 degrees to a mirror's surface where a light ray reflects."]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_incidence__i_'))
    def rule_angle_of_incidence__i_(self):
        """The angle of incidence is the angle measured between the incident ray and the normal line at the point where the light ray strikes the surface. It is often denoted by 'i'."""
        self.response = {
            'concept': 'Angle of Incidence (i)',
            'explanation': """The angle of incidence is the angle measured between the incident ray and the normal line at the point where the light ray strikes the surface. It is often denoted by 'i'.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction Terminology',
            'examples': ["The angle 'i' in Figure 5.26, formed by ray AB and normal XY.", "If a light ray hits a surface perpendicularly, its angle of incidence is 0 degrees.", "The angle formed when a light beam approaches a prism surface relative to its perpendicular."]
        }
        self.halt()

    @Rule(Fact(query_topic='refracted_ray'))
    def rule_refracted_ray(self):
        """The refracted ray is the path of the light ray after it has entered the second medium and undergone a change in direction (bending) due to refraction."""
        self.response = {
            'concept': 'Refracted Ray',
            'explanation': """The refracted ray is the path of the light ray after it has entered the second medium and undergone a change in direction (bending) due to refraction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction Terminology',
            'examples': ["The ray BC represents the refracted ray as it travels inside the block of glass.", "The light path through water after an incident ray from air.", "The bent ray of light emerging from a spectacle lens."]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_refraction__r_'))
    def rule_angle_of_refraction__r_(self):
        """The angle of refraction is the angle measured between the refracted ray and the normal line at the point where the light ray enters the second medium. It is often denoted by 'r'."""
        self.response = {
            'concept': 'Angle of Refraction (r)',
            'explanation': """The angle of refraction is the angle measured between the refracted ray and the normal line at the point where the light ray enters the second medium. It is often denoted by 'r'.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction Terminology',
            'examples': ["The angle 'r' in Figure 5.26, formed by ray BC and normal XY.", "When light bends towards the normal (e.g., from air to glass), the angle of refraction (r) is smaller than the angle of incidence (i).", "The angle a light ray makes with the perpendicular as it travels through a diamond."]
        }
        self.halt()

    @Rule(Fact(query_topic='emergent_ray'))
    def rule_emergent_ray(self):
        """When a refracted light ray travels back into a rarer medium (like air) from a denser medium (like glass), the ray that has emerged back into the rarer medium is known as the emergent ray."""
        self.response = {
            'concept': 'Emergent Ray',
            'explanation': """When a refracted light ray travels back into a rarer medium (like air) from a denser medium (like glass), the ray that has emerged back into the rarer medium is known as the emergent ray.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["A light ray exiting a glass prism into the surrounding air.", "The ray of light that leaves a glass slab and re-enters the atmosphere.", "Light passing through a thick block of ice and emerging into the air."]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_emergence'))
    def rule_angle_of_emergence(self):
        """The angle formed between the emergent ray and the normal drawn to the surface at the point where the light ray emerges from a medium is defined as the angle of emergence (e)."""
        self.response = {
            'concept': 'Angle of Emergence',
            'explanation': """The angle formed between the emergent ray and the normal drawn to the surface at the point where the light ray emerges from a medium is defined as the angle of emergence (e).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["The angle measured at point C between the ray CD and the normal when light leaves a glass block.", "If light exits a lens, the angle its final path makes with the normal at the exit point.", "Determining the angle 'e' for light leaving a transparent plastic sheet into air."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_from_rarer_to_denser_medium'))
    def rule_refraction_from_rarer_to_denser_medium(self):
        """When a light ray travels from an optically rarer medium (e.g., air) into an optically denser medium (e.g., glass), the light rays are refracted or bend towards the normal."""
        self.response = {
            'concept': 'Refraction from Rarer to Denser Medium',
            'explanation': """When a light ray travels from an optically rarer medium (e.g., air) into an optically denser medium (e.g., glass), the light rays are refracted or bend towards the normal.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light entering water from air bends towards the normal.", "A laser beam passing from air into a diamond refracts towards the normal.", "Sunlight hitting the surface of a swimming pool and bending inward."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_from_denser_to_rarer_medium'))
    def rule_refraction_from_denser_to_rarer_medium(self):
        """When a light ray travels from an optically denser medium (e.g., glass) into an optically rarer medium (e.g., air), the light rays are refracted or bend away from the normal."""
        self.response = {
            'concept': 'Refraction from Denser to Rarer Medium',
            'explanation': """When a light ray travels from an optically denser medium (e.g., glass) into an optically rarer medium (e.g., air), the light rays are refracted or bend away from the normal.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light exiting a glass block into air bends away from the normal.", "A light ray traveling from water into air will bend away from the normal.", "The apparent shallower depth of a pool when viewed from above, due to light bending away from the normal as it exits water."]
        }
        self.halt()

    @Rule(Fact(query_topic='determining_relative_medium_density_by_refraction'))
    def rule_determining_relative_medium_density_by_refraction(self):
        """If a light ray bends towards the normal when traveling from the first medium to the second, the second medium is optically denser compared to the first. Conversely, if the ray bends away from the normal, the second medium is optically rarer compared to the first."""
        self.response = {
            'concept': 'Determining Relative Medium Density by Refraction',
            'explanation': """If a light ray bends towards the normal when traveling from the first medium to the second, the second medium is optically denser compared to the first. Conversely, if the ray bends away from the normal, the second medium is optically rarer compared to the first.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["If light from air bends towards the normal in an unknown liquid, the liquid is optically denser than air.", "If light from glass bends away from the normal upon entering another transparent material, that material is optically rarer than glass.", "Observing light bending when passing from olive oil to water to determine which is optically denser."]
        }
        self.halt()

    @Rule(Fact(query_topic='first_law_of_refraction'))
    def rule_first_law_of_refraction(self):
        """The incident ray, the refracted ray, and the normal to the surface, all drawn at the point of incidence, lie in the same plane."""
        self.response = {
            'concept': 'First Law of Refraction',
            'explanation': """The incident ray, the refracted ray, and the normal to the surface, all drawn at the point of incidence, lie in the same plane.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Laws of Refraction',
            'examples': ["When drawing a ray diagram, all three lines (incident, refracted, normal) can be represented on a single 2D sheet of paper.", "The plane defined by the incident ray and the normal also contains the refracted ray.", "If the normal is along the z-axis and the incident ray is in the xy-plane, the refracted ray will also be in the xy-plane."]
        }
        self.halt()

    @Rule(Fact(query_topic='second_law_of_refraction__snell_s_law_'))
    def rule_second_law_of_refraction__snell_s_law_(self):
        """When light refracts from one medium to another, the ratio of the sine of the incident angle (sin i) to the sine of the refracted angle (sin r) is a constant. This constant, known as the refractive index (n), depends solely on the two media involved. It is mathematically expressed as: Refractive index (n) = (sin i) / (sin r)."""
        self.response = {
            'concept': "Second Law of Refraction (Snell's Law)",
            'explanation': """When light refracts from one medium to another, the ratio of the sine of the incident angle (sin i) to the sine of the refracted angle (sin r) is a constant. This constant, known as the refractive index (n), depends solely on the two media involved. It is mathematically expressed as: Refractive index (n) = (sin i) / (sin r).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Laws of Refraction',
            'examples': ["If light enters water from air at an incident angle of 45 degrees and refracts to 32 degrees, Snell's law allows calculation of water's refractive index.", "Using Snell's Law to find the angle of refraction when light passes from glass (n=1.5) to air (n=1.0) at a given incident angle.", "The refractive index for a light ray traveling from air to glass is represented as n_ag."]
        }
        self.halt()

    @Rule(Fact(query_topic='refractive_index__relative_'))
    def rule_refractive_index__relative_(self):
        """The refractive index defined as 'relative' describes the bending of light when it passes from one medium to another. It depends on the properties of both media involved. For example, n_ga represents the refractive index for light entering from glass to air."""
        self.response = {
            'concept': 'Refractive Index (Relative)',
            'explanation': """The refractive index defined as 'relative' describes the bending of light when it passes from one medium to another. It depends on the properties of both media involved. For example, n_ga represents the refractive index for light entering from glass to air.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The refractive index of water relative to air (n_aw) is 1.33.", "The refractive index of glass relative to air (n_ag) is 1.5.", "When light passes from a medium with a higher refractive index to one with a lower index, it bends away from the normal."]
        }
        self.halt()

    @Rule(Fact(query_topic='refractive_index_of_a_medium__absolute_'))
    def rule_refractive_index_of_a_medium__absolute_(self):
        """When a light ray travels from a vacuum into a specific medium, the refractive index is referred to as the 'refractive index of that medium' or absolute refractive index, as it depends only on that single medium. Practically, due to the difficulty of vacuum measurements and the slight difference in light velocity between air and vacuum, the refractive index of a medium relative to air is often used as its absolute refractive index. The index of refraction has no units."""
        self.response = {
            'concept': 'Refractive Index of a Medium (Absolute)',
            'explanation': """When a light ray travels from a vacuum into a specific medium, the refractive index is referred to as the 'refractive index of that medium' or absolute refractive index, as it depends only on that single medium. Practically, due to the difficulty of vacuum measurements and the slight difference in light velocity between air and vacuum, the refractive index of a medium relative to air is often used as its absolute refractive index. The index of refraction has no units.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The refractive index of water is the ratio of the sine of the incident angle to the sine of the refracted angle when a light ray travels from a vacuum to water.", "A stated refractive index of 1.5 for glass typically refers to its value relative to air.", "Since the velocity of light in air is very close to that in a vacuum, using air as the reference medium is a common practical approximation."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection'))
    def rule_total_internal_reflection(self):
        """Total internal reflection occurs when a light ray, traveling from a denser medium to a rarer medium, strikes the interface at an incident angle greater than the critical angle. Instead of refracting into the rarer medium, the light is entirely reflected back into the denser medium."""
        self.response = {
            'concept': 'Total Internal Reflection',
            'explanation': """Total internal reflection occurs when a light ray, traveling from a denser medium to a rarer medium, strikes the interface at an incident angle greater than the critical angle. Instead of refracting into the rarer medium, the light is entirely reflected back into the denser medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light passing through an optical fiber undergoes total internal reflection, allowing it to travel long distances.", "The sparkling of a diamond is partly due to total internal reflection within its facets.", "When underwater, looking up at an angle greater than the critical angle, you can see reflections of the bottom of the pool rather than objects outside the water."]
        }
        self.halt()

    @Rule(Fact(query_topic='critical_angle'))
    def rule_critical_angle(self):
        """The critical angle is the specific angle of incidence inside a denser medium, where the refracted ray travels exactly along the interface between the dense and rare media. At this angle, the angle of refraction is 90 degrees. If the incident angle increases beyond the critical angle, total internal reflection will occur."""
        self.response = {
            'concept': 'Critical Angle',
            'explanation': """The critical angle is the specific angle of incidence inside a denser medium, where the refracted ray travels exactly along the interface between the dense and rare media. At this angle, the angle of refraction is 90 degrees. If the incident angle increases beyond the critical angle, total internal reflection will occur.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["For light traveling from water to air, if the incident angle in water reaches the critical angle, the light will propagate along the water's surface.", "The critical angle for a specific pair of media can be calculated using Snell's Law.", "If the incident angle is less than the critical angle, the light ray will be refracted into the rarer medium."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection'))
    def rule_total_internal_reflection(self):
        """Total internal reflection is the phenomenon where a light ray, attempting to pass from a denser medium (like water, glass, or diamond) to a rarer medium (like air), reflects back into the original denser medium. This occurs when the angle of incidence within the denser medium is greater than the critical angle for that specific interface."""
        self.response = {
            'concept': 'Total Internal Reflection',
            'explanation': """Total internal reflection is the phenomenon where a light ray, attempting to pass from a denser medium (like water, glass, or diamond) to a rarer medium (like air), reflects back into the original denser medium. This occurs when the angle of incidence within the denser medium is greater than the critical angle for that specific interface.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light traveling from water to air will undergo total internal reflection if the incident angle is greater than 49°.", "Light traveling from glass to air will undergo total internal reflection if the incident angle is greater than 42°.", "Light traveling from diamond to air will undergo total internal reflection if the incident angle is greater than 24°."]
        }
        self.halt()

    @Rule(Fact(query_topic='optical_fibers'))
    def rule_optical_fibers(self):
        """Optical fibers are flexible, transparent strands typically made of glass or plastic. They are designed to transmit light rays over long distances by continuously undergoing total internal reflection as light travels from one end of the fiber to the other, ensuring minimal loss of light intensity."""
        self.response = {
            'concept': 'Optical Fibers',
            'explanation': """Optical fibers are flexible, transparent strands typically made of glass or plastic. They are designed to transmit light rays over long distances by continuously undergoing total internal reflection as light travels from one end of the fiber to the other, ensuring minimal loss of light intensity.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Endoscopes, used for observing internal organs of the human body, utilize optical fibers.", "Optical fibers are widely used in telephone communication for transmitting data.", "They are a primary component in modern Internet connections and are also used in decorative lighting."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection_by_prisms'))
    def rule_total_internal_reflection_by_prisms(self):
        """Prisms, specifically those with one 90-degree angle and two 45-degree angles, can be effectively used to produce total internal reflection. When a light ray enters the prism and strikes an internal surface at an angle greater than the critical angle of the prism material (e.g., 43 degrees for glass), it undergoes total internal reflection, allowing for precise bending of light rays without significant loss."""
        self.response = {
            'concept': 'Total Internal Reflection by Prisms',
            'explanation': """Prisms, specifically those with one 90-degree angle and two 45-degree angles, can be effectively used to produce total internal reflection. When a light ray enters the prism and strikes an internal surface at an angle greater than the critical angle of the prism material (e.g., 43 degrees for glass), it undergoes total internal reflection, allowing for precise bending of light rays without significant loss.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Prisms are used in cameras to redirect light paths.", "They are incorporated into telescopes to manipulate and magnify images.", "Binoculars utilize these prisms to alter the light path and provide a clear, upright image."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction'))
    def rule_refraction(self):
        """Refraction is the bending of light as it passes from one medium to another (e.g., from water to air), causing objects to appear in a different position than their actual location due to the change in light speed and direction."""
        self.response = {
            'concept': 'Refraction',
            'explanation': """Refraction is the bending of light as it passes from one medium to another (e.g., from water to air), causing objects to appear in a different position than their actual location due to the change in light speed and direction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A fish viewed from above water appears to be at a higher position.", "A spoon half-submerged in water appears bent at the water's surface.", "Light bending as it enters a prism."]
        }
        self.halt()

    @Rule(Fact(query_topic='lens'))
    def rule_lens(self):
        """An optical device with curved surfaces, made of transparent material (like glass or plastic), that alters the path of light rays passing through it by refraction to form images."""
        self.response = {
            'concept': 'Lens',
            'explanation': """An optical device with curved surfaces, made of transparent material (like glass or plastic), that alters the path of light rays passing through it by refraction to form images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The lens in the human eye", "A magnifying glass", "A camera lens"]
        }
        self.halt()

    @Rule(Fact(query_topic='applications_of_lenses'))
    def rule_applications_of_lenses(self):
        """Lenses are vital components in various instruments used to enhance vision, either by magnifying small objects or bringing distant objects into clear view."""
        self.response = {
            'concept': 'Applications of Lenses',
            'explanation': """Lenses are vital components in various instruments used to enhance vision, either by magnifying small objects or bringing distant objects into clear view.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Telescopes and binoculars for seeing far-away objects clearly.", "Microscopes for viewing very small objects not visible to the naked eye.", "Magnifying glasses (simple microscopes) for enlarging small objects."]
        }
        self.halt()

    @Rule(Fact(query_topic='lens_materials'))
    def rule_lens_materials(self):
        """Lenses can be made from any transparent material capable of altering light's path through refraction, commonly glass or plastic, but sometimes even liquids like water."""
        self.response = {
            'concept': 'Lens Materials',
            'explanation': """Lenses can be made from any transparent material capable of altering light's path through refraction, commonly glass or plastic, but sometimes even liquids like water.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Glass lenses used in traditional spectacles.", "Plastic lenses increasingly used in modern optics.", "Water droplets forming natural lenses."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_lenses_by_surface_shape'))
    def rule_types_of_lenses_by_surface_shape(self):
        """Lenses are classified based on the curvature of their two surfaces: bi-convex (two convex surfaces), plano-convex (one convex, one plane), bi-concave (two concave surfaces), and plano-concave (one concave, one plane)."""
        self.response = {
            'concept': 'Types of Lenses by Surface Shape',
            'explanation': """Lenses are classified based on the curvature of their two surfaces: bi-convex (two convex surfaces), plano-convex (one convex, one plane), bi-concave (two concave surfaces), and plano-concave (one concave, one plane).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A bi-convex lens, like those often found in magnifying glasses.", "A plano-convex lens, with one flat and one curved side.", "A bi-concave lens, used to correct short-sightedness."]
        }
        self.halt()

    @Rule(Fact(query_topic='convex_lens_surfaces'))
    def rule_convex_lens_surfaces(self):
        """The two curved surfaces of a convex lens can be conceptualized as being parts of two distinct imaginary spherical surfaces, each with its own center of curvature."""
        self.response = {
            'concept': 'Convex Lens Surfaces',
            'explanation': """The two curved surfaces of a convex lens can be conceptualized as being parts of two distinct imaginary spherical surfaces, each with its own center of curvature.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The front surface of a bi-convex lens derived from a sphere.", "The back surface of a bi-convex lens derived from another sphere.", "The single curved surface of a plano-convex lens originating from a sphere."]
        }
        self.halt()

    @Rule(Fact(query_topic='principal_axis'))
    def rule_principal_axis(self):
        """The principal axis of a lens is the imaginary line that joins the two centres of curvature (C1 and C2) of the spherical surfaces forming the lens. At the points where it intersects the lens surfaces, the principal axis is perpendicular to those surfaces."""
        self.response = {
            'concept': 'Principal Axis',
            'explanation': """The principal axis of a lens is the imaginary line that joins the two centres of curvature (C1 and C2) of the spherical surfaces forming the lens. At the points where it intersects the lens surfaces, the principal axis is perpendicular to those surfaces.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["The central line passing through a biconvex lens along which the lens is symmetrical.", "An imaginary straight line connecting the centers of the spheres from which the lens surfaces are derived."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray_along_principal_axis'))
    def rule_light_ray_along_principal_axis(self):
        """A light ray that enters the lens traveling exactly along its principal axis will pass through the lens and leave it without experiencing any bending or deviation."""
        self.response = {
            'concept': 'Light Ray Along Principal Axis',
            'explanation': """A light ray that enters the lens traveling exactly along its principal axis will pass through the lens and leave it without experiencing any bending or deviation.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses - Ray Tracing',
            'examples': ["A laser beam directed precisely along the principal axis of a magnifying glass.", "Light from a distant source traveling through the exact center of a camera lens along its principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='optical_centre'))
    def rule_optical_centre(self):
        """The optical centre of a lens is defined as the midpoint between its two surfaces. Any light ray that travels through the optical centre of the lens will pass through the lens without any bending or deviation."""
        self.response = {
            'concept': 'Optical Centre',
            'explanation': """The optical centre of a lens is defined as the midpoint between its two surfaces. Any light ray that travels through the optical centre of the lens will pass through the lens without any bending or deviation.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["The geometric center of a symmetrical lens.", "The point 'O' often marked in ray diagrams where light rays pass undeflected.", "A light ray entering a lens and passing directly through its center, exiting parallel to its incident path."]
        }
        self.halt()

    @Rule(Fact(query_topic='behavior_of_parallel_light_with_convex_lens'))
    def rule_behavior_of_parallel_light_with_convex_lens(self):
        """When parallel light rays (such as those from a very distant source like the Sun) pass through a convex lens, they are refracted by the lens and converge to a single point on the principal axis."""
        self.response = {
            'concept': 'Behavior of Parallel Light with Convex Lens',
            'explanation': """When parallel light rays (such as those from a very distant source like the Sun) pass through a convex lens, they are refracted by the lens and converge to a single point on the principal axis.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses - Convex Lens Properties',
            'examples': ["Using a convex lens to focus sunlight into a small, bright spot that can burn paper.", "Parallel light rays from a projector's lamp converging after passing through the projection lens.", "A telescope's objective lens bringing parallel rays from a distant star to a sharp focus."]
        }
        self.halt()

    @Rule(Fact(query_topic='focus__focal_point__of_a_convex_lens'))
    def rule_focus__focal_point__of_a_convex_lens(self):
        """The focus, or focal point, of a convex lens is the specific point on the principal axis where all light rays that are initially traveling parallel to the principal axis converge after refracting through the lens."""
        self.response = {
            'concept': 'Focus (Focal Point) of a Convex Lens',
            'explanation': """The focus, or focal point, of a convex lens is the specific point on the principal axis where all light rays that are initially traveling parallel to the principal axis converge after refracting through the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses - Convex Lens Properties',
            'examples': ["The point 'F' indicated on the principal axis of a convex lens in ray diagrams.", "The location where the sharpest image of a very distant object (like the moon) is formed by a convex lens.", "The specific point where concentrated sunlight causes a high temperature after passing through a convex lens."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light_through_a_lens'))
    def rule_refraction_of_light_through_a_lens(self):
        """When a light ray enters a lens (moving from a rarer to a denser medium), it bends towards the normal to the lens surface. Conversely, when the ray leaves the lens (moving from a denser to a rarer medium), it bends away from the normal. In both instances, the light ray ultimately bends towards the principal axis of the lens."""
        self.response = {
            'concept': 'Refraction of Light through a Lens',
            'explanation': """When a light ray enters a lens (moving from a rarer to a denser medium), it bends towards the normal to the lens surface. Conversely, when the ray leaves the lens (moving from a denser to a rarer medium), it bends away from the normal. In both instances, the light ray ultimately bends towards the principal axis of the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A light ray from air entering a glass convex lens.", "A light ray exiting a glass lens into the air.", "The path of sunlight through a magnifying glass."]
        }
        self.halt()

    @Rule(Fact(query_topic='focus__focal_point__of_a_lens'))
    def rule_focus__focal_point__of_a_lens(self):
        """The focus, or focal point, of a lens is a single point on the principal axis where all light rays that enter the lens parallel to the principal axis converge after undergoing refraction. A lens typically has two focal points, one on each side, both equidistant from the optical centre of the lens."""
        self.response = {
            'concept': 'Focus (Focal Point) of a Lens',
            'explanation': """The focus, or focal point, of a lens is a single point on the principal axis where all light rays that enter the lens parallel to the principal axis converge after undergoing refraction. A lens typically has two focal points, one on each side, both equidistant from the optical centre of the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The point where parallel sun rays meet after passing through a convex lens.", "The 'F' indicated in a lens ray diagram.", "The point where light from a very distant object converges to form an image."]
        }
        self.halt()

    @Rule(Fact(query_topic='focal_length_of_a_lens'))
    def rule_focal_length_of_a_lens(self):
        """The focal length of a lens is defined as the distance from the optical centre of the lens to its focal point. Both focal points of a lens are located at the same distance from the optical centre. In ray diagrams and calculations, the focal point is denoted by 'F' and the focal length by 'f'."""
        self.response = {
            'concept': 'Focal Length of a Lens',
            'explanation': """The focal length of a lens is defined as the distance from the optical centre of the lens to its focal point. Both focal points of a lens are located at the same distance from the optical centre. In ray diagrams and calculations, the focal point is denoted by 'F' and the focal length by 'f'.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A camera lens with a focal length of 50 mm.", "The distance 'f' used in the lens formula (1/f = 1/v - 1/u).", "Measuring the distance from a lens to a screen for a clear image of a distant object."]
        }
        self.halt()

    @Rule(Fact(query_topic='real_image_formation'))
    def rule_real_image_formation(self):
        """A real image is formed when light rays, after being refracted by a lens, actually converge and intersect at a specific point. Because the light rays genuinely meet at the image location, a real image can be projected onto a screen."""
        self.response = {
            'concept': 'Real Image Formation',
            'explanation': """A real image is formed when light rays, after being refracted by a lens, actually converge and intersect at a specific point. Because the light rays genuinely meet at the image location, a real image can be projected onto a screen.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The image projected onto a movie screen in a cinema.", "The image formed on a camera's sensor.", "The clear, inverted image of a window formed on a white paper by a convex lens."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_determination_of_convex_lens_focal_length'))
    def rule_experimental_determination_of_convex_lens_focal_length(self):
        """The focal length of a convex lens can be determined experimentally by pointing the lens towards a distant object (e.g., a window scene) and then adjusting a screen or white paper on the opposite side of the lens. When a clear, inverted image of the distant object is formed on the screen, the distance between the lens and the screen is equal to the focal length of the lens."""
        self.response = {
            'concept': 'Experimental Determination of Convex Lens Focal Length',
            'explanation': """The focal length of a convex lens can be determined experimentally by pointing the lens towards a distant object (e.g., a window scene) and then adjusting a screen or white paper on the opposite side of the lens. When a clear, inverted image of the distant object is formed on the screen, the distance between the lens and the screen is equal to the focal length of the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Holding a convex lens towards a distant tree and finding the screen position for a sharp image.", "Using sunlight to form a concentrated bright spot on paper to find the focal length.", "The activity of forming a clear image of a window on a screen to measure 'f'."]
        }
        self.halt()

    @Rule(Fact(query_topic='special_ray_through_optical_axis__convex_lens_'))
    def rule_special_ray_through_optical_axis__convex_lens_(self):
        """A light ray passing through the optical axis (center) of a convex lens goes straight without any refraction, maintaining its original path."""
        self.response = {
            'concept': 'Special Ray through Optical Axis (Convex Lens)',
            'explanation': """A light ray passing through the optical axis (center) of a convex lens goes straight without any refraction, maintaining its original path.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Lenses - Ray Diagrams',
            'examples': ["A ray from the top of an object traveling through the optical center C of the lens will not deviate.", "A light beam aimed precisely at the geometric center of a convex lens passes through unbent.", "In a ray diagram, the ray passing through 'C' continues in a straight line."]
        }
        self.halt()

    @Rule(Fact(query_topic='special_ray_parallel_to_principal_axis__convex_lens_'))
    def rule_special_ray_parallel_to_principal_axis__convex_lens_(self):
        """A light ray that enters a convex lens parallel to the principal axis will refract and pass through the focal point (F) on the opposite side of the lens after emerging."""
        self.response = {
            'concept': 'Special Ray Parallel to Principal Axis (Convex Lens)',
            'explanation': """A light ray that enters a convex lens parallel to the principal axis will refract and pass through the focal point (F) on the opposite side of the lens after emerging.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Lenses - Ray Diagrams',
            'examples': ["A ray from an object's top traveling horizontally toward the lens will converge at the focal point F'.", "Sunlight rays, being effectively parallel, will focus at the focal point of a convex lens.", "In a ray diagram, a ray parallel to the principal axis bends to pass through F on the other side."]
        }
        self.halt()

    @Rule(Fact(query_topic='special_ray_through_focal_point__convex_lens_'))
    def rule_special_ray_through_focal_point__convex_lens_(self):
        """A light ray that passes through the focal point (F) on one side of a convex lens will emerge parallel to the principal axis after refracting by the lens."""
        self.response = {
            'concept': 'Special Ray through Focal Point (Convex Lens)',
            'explanation': """A light ray that passes through the focal point (F) on one side of a convex lens will emerge parallel to the principal axis after refracting by the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Lenses - Ray Diagrams',
            'examples': ["If a ray from an object goes through the focal point F on the incident side, it will exit the lens parallel to the principal axis.", "A light source placed at the focal point of a convex lens will produce a parallel beam of light.", "In a ray diagram, a ray passing through F before the lens exits parallel to the principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_between_lens_and_focal_point__convex_lens_'))
    def rule_image_formation__object_between_lens_and_focal_point__convex_lens_(self):
        """When an object is placed between a convex lens and its focal point, the image formed is virtual, enlarged (larger than the object), and upright (erect). This image cannot be projected onto a screen because the refracted rays do not actually converge, but rather appear to diverge from a point behind the object when extended backward."""
        self.response = {
            'concept': 'Image Formation: Object Between Lens and Focal Point (Convex Lens)',
            'explanation': """When an object is placed between a convex lens and its focal point, the image formed is virtual, enlarged (larger than the object), and upright (erect). This image cannot be projected onto a screen because the refracted rays do not actually converge, but rather appear to diverge from a point behind the object when extended backward.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Convex Lenses - Image Formation',
            'examples': ["When using a magnifying glass (a convex lens) to view a small object held close to the lens, the object appears larger and upright.", "Placing a coin at a distance of 5 cm from a convex lens with a 10 cm focal length will produce a magnified, upright, virtual image.", "Observing fine print through a convex lens held closer than its focal length shows a larger, virtual version of the text."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_at_focal_point__convex_lens_'))
    def rule_image_formation__object_at_focal_point__convex_lens_(self):
        """When an object is placed at the focal point (f) of a convex lens, light rays coming parallel to the principal axis refract through the focal point. A ray passing through the optical centre (C) travels directly without refraction. Both these rays travel as parallel rays when reaching the eye, resulting in the image being formed at infinity. This image is larger than the object."""
        self.response = {
            'concept': 'Image Formation: Object at Focal Point (Convex Lens)',
            'explanation': """When an object is placed at the focal point (f) of a convex lens, light rays coming parallel to the principal axis refract through the focal point. A ray passing through the optical centre (C) travels directly without refraction. Both these rays travel as parallel rays when reaching the eye, resulting in the image being formed at infinity. This image is larger than the object.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Placing a light source at the focal point of a converging lens to create a parallel beam.", "A flashlight's reflector positions the bulb at its focal point to produce a parallel light beam.", "Creating an extremely magnified image that is perceived to be at an infinite distance."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_between_f_and_2f__convex_lens_'))
    def rule_image_formation__object_between_f_and_2f__convex_lens_(self):
        """When an object is placed at a distance between the focal length (f) and twice the focal length (2f) of a convex lens, the image is formed on the opposite side of the lens at a distance greater than 2f. This image is magnified, inverted, and real."""
        self.response = {
            'concept': 'Image Formation: Object Between f and 2f (Convex Lens)',
            'explanation': """When an object is placed at a distance between the focal length (f) and twice the focal length (2f) of a convex lens, the image is formed on the opposite side of the lens at a distance greater than 2f. This image is magnified, inverted, and real.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A slide projector uses this setup to project a magnified, inverted image onto a screen.", "An overhead projector magnifies the image of a transparency for a larger display.", "Demonstrating a larger, inverted real image of an object in an optics experiment."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_at_2f__convex_lens_'))
    def rule_image_formation__object_at_2f__convex_lens_(self):
        """When an object is placed at a distance exactly twice the focal length (2f) from a convex lens, the image is formed at a distance 2f on the opposite side of the lens. The height of the image is equal to that of the object. It is a real, inverted (up side down) image."""
        self.response = {
            'concept': 'Image Formation: Object at 2f (Convex Lens)',
            'explanation': """When an object is placed at a distance exactly twice the focal length (2f) from a convex lens, the image is formed at a distance 2f on the opposite side of the lens. The height of the image is equal to that of the object. It is a real, inverted (up side down) image.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A photographic copying system creating a 1:1 real image replica.", "Using a convex lens to project a real image that is the same size as the original object.", "An optical arrangement designed to produce a faithful, same-size reproduction of an object."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation__object_beyond_2f__convex_lens_'))
    def rule_image_formation__object_beyond_2f__convex_lens_(self):
        """When an object is placed at a distance greater than twice the focal length (2f) from a convex lens, the image is formed on the opposite side of the lens, at a point between the focal length (f) and twice the focal length (2f). This image is diminished, real, and inverted (up side down). The image becomes smaller as the object distance increases."""
        self.response = {
            'concept': 'Image Formation: Object Beyond 2f (Convex Lens)',
            'explanation': """When an object is placed at a distance greater than twice the focal length (2f) from a convex lens, the image is formed on the opposite side of the lens, at a point between the focal length (f) and twice the focal length (2f). This image is diminished, real, and inverted (up side down). The image becomes smaller as the object distance increases.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A camera lens forming a smaller, real, inverted image of a distant landscape on the sensor.", "The human eye's lens forming a diminished, real, inverted image on the retina.", "A simple telescope's objective lens forming a reduced image of a far-off celestial body."]
        }
        self.halt()

    @Rule(Fact(query_topic='principal_axis_of_a_lens'))
    def rule_principal_axis_of_a_lens(self):
        """The principal axis is the imaginary straight line that connects the centers of curvature (C1 and C2) of the two spherical surfaces forming a lens. This axis is central to understanding how light interacts with the lens."""
        self.response = {
            'concept': 'Principal Axis of a Lens',
            'explanation': """The principal axis is the imaginary straight line that connects the centers of curvature (C1 and C2) of the two spherical surfaces forming a lens. This axis is central to understanding how light interacts with the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["The line that joins these two centre points (C1 and C2) is called the principal axis of the lens.", "In Figure 5.43, the line passing through C1 and C2 represents the principal axis of the concave lens."]
        }
        self.halt()

    @Rule(Fact(query_topic='optical_centre_of_a_lens'))
    def rule_optical_centre_of_a_lens(self):
        """The optical centre (labeled as C in diagrams) is the central point of the lens. It's a critical point for tracing light rays through the lens."""
        self.response = {
            'concept': 'Optical Centre of a Lens',
            'explanation': """The optical centre (labeled as C in diagrams) is the central point of the lens. It's a critical point for tracing light rays through the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["The centre point of the lens, labeled as C, is called the optical centre.", "Any light ray that goes through the optical centre travels straight."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray_behavior___through_principal_axis__lenses_'))
    def rule_light_ray_behavior___through_principal_axis__lenses_(self):
        """A light ray that travels along the principal axis of either a convex or a concave lens passes through the lens without undergoing any bending or deviation from its original path."""
        self.response = {
            'concept': 'Light Ray Behavior - Through Principal Axis (Lenses)',
            'explanation': """A light ray that travels along the principal axis of either a convex or a concave lens passes through the lens without undergoing any bending or deviation from its original path.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lens Ray Tracing',
            'examples': ["In both convex lenses and concave lenses, a light ray that travels through the principal axis passes through the lens without bending.", "A laser beam aligned with the principal axis of a lens will not change direction after passing through it."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray_behavior___through_optical_centre__lenses_'))
    def rule_light_ray_behavior___through_optical_centre__lenses_(self):
        """Any light ray that passes directly through the optical centre of a lens (both convex and concave) continues its path straight through without bending or changing its direction."""
        self.response = {
            'concept': 'Light Ray Behavior - Through Optical Centre (Lenses)',
            'explanation': """Any light ray that passes directly through the optical centre of a lens (both convex and concave) continues its path straight through without bending or changing its direction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lens Ray Tracing',
            'examples': ["Any light ray that goes through the optical centre travels straight, without bending.", "If a ray of light is aimed precisely at the optical centre of a concave lens, it will emerge on the other side undeflected."]
        }
        self.halt()

    @Rule(Fact(query_topic='light_ray_behavior___parallel_to_principal_axis__concave_lens_'))
    def rule_light_ray_behavior___parallel_to_principal_axis__concave_lens_(self):
        """When light rays approach a concave lens parallel to its principal axis, they are refracted away from the principal axis after passing through the lens. This means the rays diverge."""
        self.response = {
            'concept': 'Light Ray Behavior - Parallel to Principal Axis (Concave Lens)',
            'explanation': """When light rays approach a concave lens parallel to its principal axis, they are refracted away from the principal axis after passing through the lens. This means the rays diverge.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Lenses Ray Tracing',
            'examples': ["Such rays, as shown in figure 5.44, are refracted away from the principal axis after passing through the lens.", "That means they diverge.", "Sunlight hitting a concave lens in parallel will spread out after refraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='focal_point_of_a_concave_lens'))
    def rule_focal_point_of_a_concave_lens(self):
        """The focal point of a concave lens is the specific point on the principal axis from which the light rays, after entering the lens parallel to the principal axis and diverging, appear to originate when traced backward."""
        self.response = {
            'concept': 'Focal Point of a Concave Lens',
            'explanation': """The focal point of a concave lens is the specific point on the principal axis from which the light rays, after entering the lens parallel to the principal axis and diverging, appear to originate when traced backward.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Concave Lenses',
            'examples': ["The point from which these divergent rays appear to come from is called the focal point of that lens.", "In Figure 5.44, 'F' on the principal axis represents the focal point.", "If you extend the diverging rays backward from a concave lens, they converge at its focal point."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_concave_lenses'))
    def rule_image_formation_by_concave_lenses(self):
        """Concave lenses do not form real images. Instead, they consistently form virtual, upright, and diminished images, regardless of the object's distance from the lens. To view the image, one must look directly through the lens."""
        self.response = {
            'concept': 'Image Formation by Concave Lenses',
            'explanation': """Concave lenses do not form real images. Instead, they consistently form virtual, upright, and diminished images, regardless of the object's distance from the lens. To view the image, one must look directly through the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["Placing a lighted candle in front of a concave lens will not produce a real image on a screen.", "Looking at an object through a concave lens reveals a smaller, upright, and virtual image."]
        }
        self.halt()

    @Rule(Fact(query_topic='hand_lens___simple_microscope'))
    def rule_hand_lens___simple_microscope(self):
        """A hand lens, also known as a simple microscope or magnifying lens, is a convex lens used to create magnified images of objects. This occurs when the object is positioned closer to the lens than its focal length."""
        self.response = {
            'concept': 'Hand Lens / Simple Microscope',
            'explanation': """A hand lens, also known as a simple microscope or magnifying lens, is a convex lens used to create magnified images of objects. This occurs when the object is positioned closer to the lens than its focal length.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Optical Instruments',
            'examples': ["Using a magnifying glass to view small insects.", "Examining intricate parts of flowers with a hand lens."]
        }
        self.halt()

    @Rule(Fact(query_topic='principle_of_reversibility_of_light'))
    def rule_principle_of_reversibility_of_light(self):
        """This principle states that if the direction of a light ray is reversed, it will precisely retrace its original path. This holds true even when the light ray has undergone a combination of multiple reflections and refractions."""
        self.response = {
            'concept': 'Principle of Reversibility of Light',
            'explanation': """This principle states that if the direction of a light ray is reversed, it will precisely retrace its original path. This holds true even when the light ray has undergone a combination of multiple reflections and refractions.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Light Properties',
            'examples': ["If a light ray passes through a series of lenses and mirrors, reversing its final direction will make it retrace the exact same path backward.", "A light ray reflecting off a mirror will travel back along its original path if its direction is inverted."]
        }
        self.halt()

    @Rule(Fact(query_topic='cameras_and_image_formation'))
    def rule_cameras_and_image_formation(self):
        """Cameras utilize convex lenses to form real, inverted images on a photographic film or digital sensor. By adjusting the lens, the distance between the lens and the film/sensor changes, allowing for clear focus and image acquisition of objects at varying distances."""
        self.response = {
            'concept': 'Cameras and Image Formation',
            'explanation': """Cameras utilize convex lenses to form real, inverted images on a photographic film or digital sensor. By adjusting the lens, the distance between the lens and the film/sensor changes, allowing for clear focus and image acquisition of objects at varying distances.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Optical Instruments',
            'examples': ["Convex lenses in cameras form real, inverted images on the film.", "Adjusting a camera's lens to bring distant objects into sharp focus.", "Obtaining clear images of objects at different distances by changing the lens-to-film distance."]
        }
        self.halt()

    @Rule(Fact(query_topic='microscope'))
    def rule_microscope(self):
        """An optical instrument used to observe tiny objects that are not visible to the naked eye. It consists of two primary lenses, an objective lens and an eyepiece, which combine to produce a very high magnification of the object."""
        self.response = {
            'concept': 'Microscope',
            'explanation': """An optical instrument used to observe tiny objects that are not visible to the naked eye. It consists of two primary lenses, an objective lens and an eyepiece, which combine to produce a very high magnification of the object.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Optical Instruments',
            'examples': ["Observing the intricate details of a bacteria cell.", "Viewing the cellular structure of a plant leaf.", "Examining the fine print on a stamp."]
        }
        self.halt()

    @Rule(Fact(query_topic='virtual_image__mirrors_'))
    def rule_virtual_image__mirrors_(self):
        """An image formed by a mirror that cannot be projected onto a screen because the light rays do not actually converge at the image location; they only appear to diverge from it. These images are typically upright."""
        self.response = {
            'concept': 'Virtual Image (Mirrors)',
            'explanation': """An image formed by a mirror that cannot be projected onto a screen because the light rays do not actually converge at the image location; they only appear to diverge from it. These images are typically upright.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Reflection',
            'examples': ["The image you see of yourself in a plane mirror.", "The image of cars viewed in a convex rearview mirror.", "The magnified image formed by a concave mirror when an object is placed between its pole and focal point."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror_image_formation__object_between_pole_and_focal_point_'))
    def rule_concave_mirror_image_formation__object_between_pole_and_focal_point_(self):
        """When an object is placed between the pole and the focal point of a concave mirror, the image formed is virtual, upright, and larger than the object. Moving the object closer to the pole of the mirror will result in the image becoming smaller."""
        self.response = {
            'concept': 'Concave Mirror Image Formation (Object between Pole and Focal Point)',
            'explanation': """When an object is placed between the pole and the focal point of a concave mirror, the image formed is virtual, upright, and larger than the object. Moving the object closer to the pole of the mirror will result in the image becoming smaller.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Reflection / Concave Mirrors',
            'examples': ["Using a concave mirror as a shaving mirror to see a magnified, upright reflection.", "A dentist using a concave mirror to get a magnified view of a tooth.", "The image formed when holding a small object very close to a concave make-up mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light'))
    def rule_refraction_of_light(self):
        """The bending of light as it passes from one transparent medium into another. When light enters a denser medium from a rarer medium, it bends towards the normal. Conversely, when it enters a rarer medium from a denser medium, it bends away from the normal."""
        self.response = {
            'concept': 'Refraction of Light',
            'explanation': """The bending of light as it passes from one transparent medium into another. When light enters a denser medium from a rarer medium, it bends towards the normal. Conversely, when it enters a rarer medium from a denser medium, it bends away from the normal.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction',
            'examples': ["A straw appearing bent when placed partially in a glass of water.", "Light passing through a lens to focus an image.", "The apparent shallowing of a swimming pool."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection'))
    def rule_total_internal_reflection(self):
        """A phenomenon that occurs when a ray of light traveling from a denser medium to a rarer medium strikes the interface at an angle of incidence greater than the critical angle. In this condition, no light is refracted; instead, all the light is reflected back into the denser medium."""
        self.response = {
            'concept': 'Total Internal Reflection',
            'explanation': """A phenomenon that occurs when a ray of light traveling from a denser medium to a rarer medium strikes the interface at an angle of incidence greater than the critical angle. In this condition, no light is refracted; instead, all the light is reflected back into the denser medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics / Refraction / Total Internal Reflection',
            'examples': ["The sparkling effect observed in a cut diamond.", "The transmission of light signals through fiber optic cables.", "The shimmering appearance of a mirage on a hot road."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_a_convex_lens_when_object_is_beyond_twice_the_focal_length'))
    def rule_image_formation_by_a_convex_lens_when_object_is_beyond_twice_the_focal_length(self):
        """When an object is placed in front of a convex lens at a distance greater than twice its focal length (u > 2f), the lens forms a real, inverted, and diminished image between the focal point (f) and twice the focal length (2f) on the opposite side of the lens."""
        self.response = {
            'concept': 'Image formation by a convex lens when object is beyond twice the focal length',
            'explanation': """When an object is placed in front of a convex lens at a distance greater than twice its focal length (u > 2f), the lens forms a real, inverted, and diminished image between the focal point (f) and twice the focal length (2f) on the opposite side of the lens.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["An object placed at 30 cm from a convex lens with a focal length of 10 cm.", "A distant tree viewed through a convex lens, forming a smaller, inverted image.", "A camera lens focusing light from a faraway object onto the sensor."]
        }
        self.halt()

    @Rule(Fact(query_topic='distinguishing_between_real_and_virtual_images'))
    def rule_distinguishing_between_real_and_virtual_images(self):
        """A real image is formed by the actual intersection of light rays and can be projected onto a screen. A virtual image is formed when light rays only appear to diverge from a point and cannot be projected onto a screen."""
        self.response = {
            'concept': 'Distinguishing between real and virtual images',
            'explanation': """A real image is formed by the actual intersection of light rays and can be projected onto a screen. A virtual image is formed when light rays only appear to diverge from a point and cannot be projected onto a screen.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses & Mirrors',
            'examples': ["Using a screen to determine if an image formed by a lens is real or virtual.", "The image seen in a plane mirror is always virtual.", "The image projected by a cinema projector onto a screen is real."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection__tir__in_optical_fibres'))
    def rule_total_internal_reflection__tir__in_optical_fibres(self):
        """Optical fibres utilize total internal reflection to transmit light. When light travels from a denser medium (core) to a rarer medium (cladding) at an angle of incidence greater than the critical angle, it is completely reflected back into the denser medium, allowing efficient light transmission over long distances."""
        self.response = {
            'concept': 'Total Internal Reflection (TIR) in optical fibres',
            'explanation': """Optical fibres utilize total internal reflection to transmit light. When light travels from a denser medium (core) to a rarer medium (cladding) at an angle of incidence greater than the critical angle, it is completely reflected back into the denser medium, allowing efficient light transmission over long distances.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Optical Instruments',
            'examples': ["Light traveling through an endoscope to view internal body organs.", "High-speed data transmission over long distances using fibre optic cables.", "Decorative lamps with glowing plastic strands that rely on internal reflection."]
        }
        self.halt()

    @Rule(Fact(query_topic='change_in_speed_of_light_when_passing_through_different_media'))
    def rule_change_in_speed_of_light_when_passing_through_different_media(self):
        """The speed of light changes as it passes from one transparent medium to another due to a change in the refractive index. Light slows down when entering an optically denser medium (higher refractive index) and speeds up when entering an optically rarer medium (lower refractive index)."""
        self.response = {
            'concept': 'Change in speed of light when passing through different media',
            'explanation': """The speed of light changes as it passes from one transparent medium to another due to a change in the refractive index. Light slows down when entering an optically denser medium (higher refractive index) and speeds up when entering an optically rarer medium (lower refractive index).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light slowing down as it enters an optical fibre from air.", "Light speeding up as it exits a glass block into air.", "The apparent bending of a spoon in a glass of water is due to light's speed change."]
        }
        self.halt()

    @Rule(Fact(query_topic='object_distances_for_largest_and_smallest_real_images_by_a_convex_lens'))
    def rule_object_distances_for_largest_and_smallest_real_images_by_a_convex_lens(self):
        """For a convex lens, the largest real image is obtained when the object is placed just beyond the focal point (between f and 2f, closer to f). The smallest real image (a point image) is formed when the object is placed at a very large distance (effectively infinity)."""
        self.response = {
            'concept': 'Object distances for largest and smallest real images by a convex lens',
            'explanation': """For a convex lens, the largest real image is obtained when the object is placed just beyond the focal point (between f and 2f, closer to f). The smallest real image (a point image) is formed when the object is placed at a very large distance (effectively infinity).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["Placing an object just outside the focal point of a projector lens to get a highly magnified image.", "Focusing sunlight (object at infinity) with a convex lens to produce a tiny, bright spot (smallest real image).", "Using a magnifying glass to form a large real image of a distant object by careful positioning."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_identification_of_lenses_by_focal_length'))
    def rule_experimental_identification_of_lenses_by_focal_length(self):
        """The focal length of a convex lens can be determined by focusing light from a very distant object (e.g., the sun or a distant window) onto a screen and measuring the distance between the lens and the sharp, inverted image. Lenses can be distinguished by comparing their focal lengths determined this way."""
        self.response = {
            'concept': 'Experimental identification of lenses by focal length',
            'explanation': """The focal length of a convex lens can be determined by focusing light from a very distant object (e.g., the sun or a distant window) onto a screen and measuring the distance between the lens and the sharp, inverted image. Lenses can be distinguished by comparing their focal lengths determined this way.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Experiments',
            'examples': ["Using sunlight to find the exact focal length of an unknown convex lens.", "Comparing the image size and distance for different lenses to identify their focal lengths.", "Observing how a lens magnifies or diminishes a nearby object to estimate its focal length and type."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light'))
    def rule_refraction_of_light(self):
        """Refraction is the phenomenon where light changes its direction (bends) as it passes from one transparent medium to another, caused by a change in its speed."""
        self.response = {
            'concept': 'Refraction of light',
            'explanation': """Refraction is the phenomenon where light changes its direction (bends) as it passes from one transparent medium to another, caused by a change in its speed.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["A pencil appearing bent when partially immersed in water.", "Light bending as it enters a swimming pool from the air.", "The separation of white light into colors by a prism."]
        }
        self.halt()

    @Rule(Fact(query_topic='cause_of_light_changing_direction_during_refraction'))
    def rule_cause_of_light_changing_direction_during_refraction(self):
        """Light changes direction during refraction because its speed changes when it moves from one medium to another with a different refractive index. If the light ray strikes the interface at an angle, one part of the wavefront changes speed before the other, causing the wavefront to pivot and the ray to bend."""
        self.response = {
            'concept': 'Cause of light changing direction during refraction',
            'explanation': """Light changes direction during refraction because its speed changes when it moves from one medium to another with a different refractive index. If the light ray strikes the interface at an angle, one part of the wavefront changes speed before the other, causing the wavefront to pivot and the ray to bend.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light from a fish in water appearing to come from a shallower depth to an observer in air.", "The apparent shift in position of an object viewed through a thick glass slab.", "The ability of lenses to focus or diverge light rays."]
        }
        self.halt()

    @Rule(Fact(query_topic='critical_angle_in_optics'))
    def rule_critical_angle_in_optics(self):
        """The critical angle is the specific angle of incidence in an optically denser medium for which the angle of refraction in the optically rarer medium is 90 degrees. If the angle of incidence exceeds the critical angle, total internal reflection occurs."""
        self.response = {
            'concept': 'Critical angle in optics',
            'explanation': """The critical angle is the specific angle of incidence in an optically denser medium for which the angle of refraction in the optically rarer medium is 90 degrees. If the angle of incidence exceeds the critical angle, total internal reflection occurs.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Total Internal Reflection',
            'examples': ["The shimmering effect observed when looking up from underwater.", "The angle at which light reflects entirely within a diamond, making it sparkle.", "Fibre optics systems relying on light entering at angles greater than the critical angle."]
        }
        self.halt()

    @Rule(Fact(query_topic='multiple_paths_of_light_involving_refraction_and_reflection'))
    def rule_multiple_paths_of_light_involving_refraction_and_reflection(self):
        """Light can travel from a source to an observer via different paths, which may include direct refraction through an interface, or undergoing total internal reflection within a medium before refracting out, leading to multiple perceived images or paths."""
        self.response = {
            'concept': 'Multiple paths of light involving refraction and reflection',
            'explanation': """Light can travel from a source to an observer via different paths, which may include direct refraction through an interface, or undergoing total internal reflection within a medium before refracting out, leading to multiple perceived images or paths.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction & Reflection',
            'examples': ["Observing an object both directly through a water surface and via its reflection off the surface.", "Light rays from an object inside an aquarium reaching an observer from various angles.", "Seeing reflections in a window pane both from outside and inside the room simultaneously."]
        }
        self.halt()

    @Rule(Fact(query_topic='experimental_investigation_of_light_refraction_from_glass_to_air'))
    def rule_experimental_investigation_of_light_refraction_from_glass_to_air(self):
        """An experiment to investigate refraction from glass to air involves shining a light ray through a glass block and measuring its path as it exits into the air. By measuring the angle of incidence (i) inside the glass and the angle of refraction (r) in the air, the relationship between these angles and the refractive indices can be studied (e.g., using Snell's Law)."""
        self.response = {
            'concept': 'Experimental investigation of light refraction from glass to air',
            'explanation': """An experiment to investigate refraction from glass to air involves shining a light ray through a glass block and measuring its path as it exits into the air. By measuring the angle of incidence (i) inside the glass and the angle of refraction (r) in the air, the relationship between these angles and the refractive indices can be studied (e.g., using Snell's Law).""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Experiments',
            'examples': ["Using a protractor and a light box to measure angles 'i' and 'r' for a ray passing from glass to air.", "Plotting a graph of sin i versus sin r to determine the refractive index of glass relative to air.", "Observing how the refracted ray bends away from the normal when exiting glass into air."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection__tir_'))
    def rule_total_internal_reflection__tir_(self):
        """Total Internal Reflection (TIR) occurs when a light ray traveling from a denser medium (higher refractive index) to a less dense medium (lower refractive index) strikes the interface at an angle of incidence greater than the critical angle. Instead of refracting into the less dense medium, the light is entirely reflected back into the denser medium."""
        self.response = {
            'concept': 'Total Internal Reflection (TIR)',
            'explanation': """Total Internal Reflection (TIR) occurs when a light ray traveling from a denser medium (higher refractive index) to a less dense medium (lower refractive index) strikes the interface at an angle of incidence greater than the critical angle. Instead of refracting into the less dense medium, the light is entirely reflected back into the denser medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light reflecting within an optical fibre for telecommunication.", "The shimmering effect observed when looking up from underwater at an angle.", "Diamonds sparkle due to their high refractive index causing many internal reflections."]
        }
        self.halt()

    @Rule(Fact(query_topic='changes_in_light_properties_during_refraction'))
    def rule_changes_in_light_properties_during_refraction(self):
        """When light passes from one medium to another, especially from a less dense medium (e.g., air) to a denser medium (e.g., glass or water), several properties change. The speed of light decreases, and its wavelength also decreases. Consequently, the light ray bends towards the normal. However, the frequency of the light remains constant during refraction."""
        self.response = {
            'concept': 'Changes in Light Properties During Refraction',
            'explanation': """When light passes from one medium to another, especially from a less dense medium (e.g., air) to a denser medium (e.g., glass or water), several properties change. The speed of light decreases, and its wavelength also decreases. Consequently, the light ray bends towards the normal. However, the frequency of the light remains constant during refraction.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Refraction',
            'examples': ["Light entering a glass block from air slows down and bends towards the normal.", "A light beam passing from air into water experiences a decrease in speed and wavelength.", "Different colors of light refract at slightly different angles when entering a prism, leading to dispersion, because their speeds in the medium vary."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_characteristics_of_common_optical_devices'))
    def rule_image_characteristics_of_common_optical_devices(self):
        """Different optical devices utilize lenses (and sometimes mirrors) to produce images with specific characteristics (nature, size, and position) tailored for their intended function:"""
        self.response = {
            'concept': 'Image Characteristics of Common Optical Devices',
            'explanation': """Different optical devices utilize lenses (and sometimes mirrors) to produce images with specific characteristics (nature, size, and position) tailored for their intended function:""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Optical Devices',
            'examples': ["The human eye forms a real, inverted, and diminished image on the retina.", "A projector forms a real, inverted, and magnified image on a distant screen.", "A magnifying glass forms a virtual, upright, and magnified image on the same side as the object."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_convex_lens__object_within_focal_length_'))
    def rule_image_formation_by_convex_lens__object_within_focal_length_(self):
        """When an object is placed in front of a convex lens at a distance less than its focal length (i.e., between the optical centre and the principal focus, F), the lens forms a virtual, upright, and magnified image. This image appears on the same side of the lens as the object. This configuration is the principle behind a simple magnifying glass."""
        self.response = {
            'concept': 'Image Formation by Convex Lens (Object within Focal Length)',
            'explanation': """When an object is placed in front of a convex lens at a distance less than its focal length (i.e., between the optical centre and the principal focus, F), the lens forms a virtual, upright, and magnified image. This image appears on the same side of the lens as the object. This configuration is the principle behind a simple magnifying glass.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["Using a magnifying glass to clearly view small print.", "A jeweller examining a tiny gemstone with a loupe.", "Observing a magnified, upright image of an insect through a hand lens held close to it."]
        }
        self.halt()

    @Rule(Fact(query_topic='ray_tracing_for_lenses'))
    def rule_ray_tracing_for_lenses(self):
        """Ray tracing is a graphical method used to determine the position, size, and nature of the image formed by a lens. It involves drawing at least two principal rays from a point on the object to the lens and then tracing their refracted paths. The intersection of these refracted rays (or their extensions) locates the corresponding image point."""
        self.response = {
            'concept': 'Ray Tracing for Lenses',
            'explanation': """Ray tracing is a graphical method used to determine the position, size, and nature of the image formed by a lens. It involves drawing at least two principal rays from a point on the object to the lens and then tracing their refracted paths. The intersection of these refracted rays (or their extensions) locates the corresponding image point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["Drawing a ray parallel to the principal axis that refracts through the focal point (F').", "Drawing a ray through the optical centre that passes undeviated.", "Drawing a ray through the focal point (F) on the object side that refracts parallel to the principal axis."]
        }
        self.halt()

    @Rule(Fact(query_topic='magnification_of_lenses'))
    def rule_magnification_of_lenses(self):
        """Linear magnification (M) of a lens is a dimensionless quantity defined as the ratio of the height of the image (h_i) to the height of the object (h_o). It can also be expressed as the negative ratio of the image distance (v) to the object distance (u) from the optical centre. M = h_i / h_o = -v / u. A positive magnification indicates an upright image, while a negative magnification indicates an inverted image."""
        self.response = {
            'concept': 'Magnification of Lenses',
            'explanation': """Linear magnification (M) of a lens is a dimensionless quantity defined as the ratio of the height of the image (h_i) to the height of the object (h_o). It can also be expressed as the negative ratio of the image distance (v) to the object distance (u) from the optical centre. M = h_i / h_o = -v / u. A positive magnification indicates an upright image, while a negative magnification indicates an inverted image.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["If an object of 2 cm height forms a 4 cm image, the magnification is 2.", "A magnification of -0.5 indicates a real, inverted, and diminished image.", "For a projector creating an image 20 times larger than the slide, the magnitude of magnification is 20."]
        }
        self.halt()

    @Rule(Fact(query_topic='effect_of_object_position_on_convex_lens_image__real_image_'))
    def rule_effect_of_object_position_on_convex_lens_image__real_image_(self):
        """For a convex lens forming a real image, as the object moves closer to the principal focus (F) from a position beyond 2F, the real image formed moves further away from the lens (and further from F' on the opposite side). Concurrently, the size of the image increases, becoming larger than the object. When the object reaches F, the image is formed at infinity."""
        self.response = {
            'concept': 'Effect of Object Position on Convex Lens Image (Real Image)',
            'explanation': """For a convex lens forming a real image, as the object moves closer to the principal focus (F) from a position beyond 2F, the real image formed moves further away from the lens (and further from F' on the opposite side). Concurrently, the size of the image increases, becoming larger than the object. When the object reaches F, the image is formed at infinity.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics - Lenses',
            'examples': ["Moving an object from 3F to 2F for a convex lens will cause the image to move from between F' and 2F' to exactly 2F', while increasing in size.", "To obtain a larger projected image, the projector (object) must be moved closer to its lens's focal point.", "As a distant car approaches, its real image formed by a convex lens (e.g., in a camera) moves closer to the focal point and becomes larger."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_mirrors'))
    def rule_types_of_mirrors(self):
        """There are two types of mirrors - plane mirrors and curved mirrors. Curved mirrors can be either convex mirrors or concave mirrors."""
        self.response = {
            'concept': 'Types of Mirrors',
            'explanation': """There are two types of mirrors - plane mirrors and curved mirrors. Curved mirrors can be either convex mirrors or concave mirrors.""",
            'topic': 'Physics',
            'subtopic': 'Mirrors',
            'examples': ["A bathroom mirror is a plane mirror.", "A car's passenger side mirror is often a convex mirror.", "A shaving mirror is typically a concave mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='characteristics_of_images_formed_by_plane_mirrors'))
    def rule_characteristics_of_images_formed_by_plane_mirrors(self):
        """Images formed by plane mirrors are virtual and upright. They are the same size as the object."""
        self.response = {
            'concept': 'Characteristics of Images formed by Plane Mirrors',
            'explanation': """Images formed by plane mirrors are virtual and upright. They are the same size as the object.""",
            'topic': 'Physics',
            'subtopic': 'Plane Mirrors',
            'examples': ["Your reflection in a flat mirror is virtual, upright, and appears to be the same size as you.", "The image of a sign reflected in a still pond.", "A reflection in a shop window before the shop opens."]
        }
        self.halt()

    @Rule(Fact(query_topic='first_law_of_reflection'))
    def rule_first_law_of_reflection(self):
        """The incident ray, the reflected ray and the normal to the surface at the point of reflection lie on the same plane."""
        self.response = {
            'concept': 'First Law of Reflection',
            'explanation': """The incident ray, the reflected ray and the normal to the surface at the point of reflection lie on the same plane.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["If a laser beam hits a mirror, the incoming beam, the reflected beam, and the normal to the mirror's surface at that point can all be drawn on a single piece of paper.", "Observing light reflecting off a perfectly smooth metal surface, all components remain within a two-dimensional plane.", "The path of light reflecting off a calm water surface adheres to this planar rule."]
        }
        self.halt()

    @Rule(Fact(query_topic='second_law_of_reflection'))
    def rule_second_law_of_reflection(self):
        """When light is reflected from a mirror, the angle of incidence is equal to the angle of reflection."""
        self.response = {
            'concept': 'Second Law of Reflection',
            'explanation': """When light is reflected from a mirror, the angle of incidence is equal to the angle of reflection.""",
            'topic': 'Physics',
            'subtopic': 'Reflection of Light',
            'examples': ["If a light ray strikes a mirror at an angle of 30 degrees to the normal, it will reflect off at an angle of 30 degrees to the normal.", "A billiard ball hitting the cushion and bouncing off at an equal angle relative to the cushion's normal.", "Light bouncing symmetrically off a polished surface."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_convex_lenses__as_described_in_text_'))
    def rule_image_formation_by_convex_lenses__as_described_in_text_(self):
        """When an object is placed in front of a convex lens, the images are diminished, upright and virtual, irrespective of the object distance."""
        self.response = {
            'concept': 'Image Formation by Convex Lenses (as described in text)',
            'explanation': """When an object is placed in front of a convex lens, the images are diminished, upright and virtual, irrespective of the object distance.""",
            'topic': 'Physics',
            'subtopic': 'Lenses',
            'examples': ["An object viewed through a specific convex lens setup designed to consistently produce diminished, upright, and virtual images.", "A specific type of optical instrument using a convex lens that creates a smaller, virtual image regardless of how close or far the object is.", "Observing an object through a convex lens that always results in an upright and shrunken image."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_of_light'))
    def rule_refraction_of_light(self):
        """The bending of light when passing from one medium to another is called refraction of light."""
        self.response = {
            'concept': 'Refraction of Light',
            'explanation': """The bending of light when passing from one medium to another is called refraction of light.""",
            'topic': 'Physics',
            'subtopic': 'Refraction',
            'examples': ["A straw appearing bent when placed in a glass of water.", "Light passing through a prism and separating into a spectrum of colors.", "Looking through a window pane at an angle, objects beyond appear slightly shifted."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_from_rare_to_dense_medium'))
    def rule_refraction_from_rare_to_dense_medium(self):
        """When light travels from a rare medium to a dense medium, the ray bends towards the normal."""
        self.response = {
            'concept': 'Refraction from Rare to Dense Medium',
            'explanation': """When light travels from a rare medium to a dense medium, the ray bends towards the normal.""",
            'topic': 'Physics',
            'subtopic': 'Refraction',
            'examples': ["Light entering water from air bends towards the normal.", "A laser beam passing from air into a block of glass.", "Sunlight entering the atmosphere from space."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction_from_dense_to_rare_medium'))
    def rule_refraction_from_dense_to_rare_medium(self):
        """When light travels from a dense medium to a rare medium, the ray bends away from the normal."""
        self.response = {
            'concept': 'Refraction from Dense to Rare Medium',
            'explanation': """When light travels from a dense medium to a rare medium, the ray bends away from the normal.""",
            'topic': 'Physics',
            'subtopic': 'Refraction',
            'examples': ["Light exiting water to enter air bends away from the normal.", "A light beam leaving a diamond and entering the atmosphere.", "Fish viewing objects above water see them higher than they actually are."]
        }
        self.halt()

    @Rule(Fact(query_topic='first_law_of_refraction'))
    def rule_first_law_of_refraction(self):
        """When light undergoes refraction, the incident ray, the refracted ray and the normal to the surface at the point of refraction lie on the same plane."""
        self.response = {
            'concept': 'First Law of Refraction',
            'explanation': """When light undergoes refraction, the incident ray, the refracted ray and the normal to the surface at the point of refraction lie on the same plane.""",
            'topic': 'Physics',
            'subtopic': 'Refraction of Light',
            'examples': ["A light ray entering water, the refracted ray, and the normal all visible on a flat surface.", "Observing how a light beam bends as it crosses from air to glass, with all paths confined to a single plane.", "A laser striking a water surface and its bent path remaining in the same plane as the incident ray."]
        }
        self.halt()

    @Rule(Fact(query_topic='definition_of_index_of_refraction'))
    def rule_definition_of_index_of_refraction(self):
        """Index of refraction = Sine of the angle of incidence / Sine of the angle of refraction."""
        self.response = {
            'concept': 'Definition of Index of Refraction',
            'explanation': """Index of refraction = Sine of the angle of incidence / Sine of the angle of refraction.""",
            'topic': 'Physics',
            'subtopic': 'Refraction',
            'examples': ["Calculating the refractive index of water given a 30-degree angle of incidence and a 22-degree angle of refraction.", "Using Snell's Law to determine the refractive index of a transparent material.", "Measuring the degree of light bending when it enters a new medium to find its index of refraction."]
        }
        self.halt()

    @Rule(Fact(query_topic='critical_angle'))
    def rule_critical_angle(self):
        """When light travels from a denser medium to a rare medium, at a certain value of the angle of incidence, the refracted ray travels along the surface between the two media. The angle of incidence in this situation is called the critical angle (c)."""
        self.response = {
            'concept': 'Critical Angle',
            'explanation': """When light travels from a denser medium to a rare medium, at a certain value of the angle of incidence, the refracted ray travels along the surface between the two media. The angle of incidence in this situation is called the critical angle (c).""",
            'topic': 'Physics',
            'subtopic': 'Total Internal Reflection',
            'examples': ["The critical angle for light going from water to air is approximately 48.6 degrees.", "At the critical angle, a light ray skims along the boundary of the two media rather than entering the rarer medium.", "Determining the maximum angle of incidence for light to escape a denser medium."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection'))
    def rule_total_internal_reflection(self):
        """When a ray of light travels from a denser medium to a rare medium with an angle of incidence greater than the critical angle, the ray is reflected back into the denser medium. This is called total internal reflection."""
        self.response = {
            'concept': 'Total Internal Reflection',
            'explanation': """When a ray of light travels from a denser medium to a rare medium with an angle of incidence greater than the critical angle, the ray is reflected back into the denser medium. This is called total internal reflection.""",
            'topic': 'Physics',
            'subtopic': 'Total Internal Reflection',
            'examples': ["The shimmering effect seen when looking up at the water surface from underwater, acting like a mirror.", "Light reflecting repeatedly inside a prism to change its direction.", "The sparkle of a diamond, caused by internal reflections."]
        }
        self.halt()

    @Rule(Fact(query_topic='application_of_total_internal_reflection__optical_fibers'))
    def rule_application_of_total_internal_reflection__optical_fibers(self):
        """Light travels through optical fibers by undergoing total internal reflection."""
        self.response = {
            'concept': 'Application of Total Internal Reflection: Optical Fibers',
            'explanation': """Light travels through optical fibers by undergoing total internal reflection.""",
            'topic': 'Physics',
            'subtopic': 'Total Internal Reflection / Applications',
            'examples': ["High-speed internet data transmission via fiber optic cables.", "Medical endoscopes using total internal reflection to view inside the human body.", "Decorative fiber optic lamps that guide light to the tips of their strands."]
        }
        self.halt()

    @Rule(Fact(query_topic='types_of_lenses'))
    def rule_types_of_lenses(self):
        """There are many types of lenses such as bi-convex lenses, bi-concave lenses, plano-convex lenses, and plano-concave lenses."""
        self.response = {
            'concept': 'Types of Lenses',
            'explanation': """There are many types of lenses such as bi-convex lenses, bi-concave lenses, plano-convex lenses, and plano-concave lenses.""",
            'topic': 'Physics',
            'subtopic': 'Lenses',
            'examples': ["A magnifying glass is typically a bi-convex lens.", "Eyeglasses for correcting vision can use various types of lenses.", "Elements within camera lenses can include bi-concave or plano-convex designs."]
        }
        self.halt()

    @Rule(Fact(query_topic='image_formation_by_bi_convex_lenses__as_described_in_text_'))
    def rule_image_formation_by_bi_convex_lenses__as_described_in_text_(self):
        """When an object is placed in front of a bi-convex lens, the image is upright, diminished and virtual, irrespective of the object distance."""
        self.response = {
            'concept': 'Image Formation by Bi-convex Lenses (as described in text)',
            'explanation': """When an object is placed in front of a bi-convex lens, the image is upright, diminished and virtual, irrespective of the object distance.""",
            'topic': 'Physics',
            'subtopic': 'Lenses',
            'examples': ["An object viewed through a specific bi-convex lens setup that always produces diminished, upright, and virtual images.", "A camera lens component (if designed to) that yields a virtual, reduced image irrespective of object distance.", "A scenario where a bi-convex lens consistently forms an upright image smaller than the object."]
        }
        self.halt()

    @Rule(Fact(query_topic='reflection'))
    def rule_reflection(self):
        """The bouncing back of light (or other waves) when it strikes a surface."""
        self.response = {
            'concept': 'Reflection',
            'explanation': """The bouncing back of light (or other waves) when it strikes a surface.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light reflecting off a mirror to form an image.", "The reflection of sunlight from the surface of water.", "A polished metal surface acting as a reflector."]
        }
        self.halt()

    @Rule(Fact(query_topic='total_internal_reflection'))
    def rule_total_internal_reflection(self):
        """The complete reflection of a ray of light within a denser medium from its boundary with a less dense medium, occurring when the angle of incidence exceeds a critical angle."""
        self.response = {
            'concept': 'Total internal reflection',
            'explanation': """The complete reflection of a ray of light within a denser medium from its boundary with a less dense medium, occurring when the angle of incidence exceeds a critical angle.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Light transmission through optical fibers.", "The sparkle of a cut diamond.", "Mirages observed on hot roads."]
        }
        self.halt()

    @Rule(Fact(query_topic='mirrors'))
    def rule_mirrors(self):
        """Surfaces that reflect light and are capable of forming images."""
        self.response = {
            'concept': 'Mirrors',
            'explanation': """Surfaces that reflect light and are capable of forming images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A plane mirror used for personal grooming.", "A convex mirror used as a car's rear-view mirror.", "A concave mirror used in a telescope."]
        }
        self.halt()

    @Rule(Fact(query_topic='apparent_depth'))
    def rule_apparent_depth(self):
        """The perceived depth of an object submerged in a fluid, which appears shallower than its real depth due to the refraction of light."""
        self.response = {
            'concept': 'Apparent depth',
            'explanation': """The perceived depth of an object submerged in a fluid, which appears shallower than its real depth due to the refraction of light.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A swimming pool appearing shallower than it actually is.", "A coin at the bottom of a glass of water appearing closer to the surface.", "A fishing spear needing to be aimed below the perceived position of a fish."]
        }
        self.halt()

    @Rule(Fact(query_topic='binoculars'))
    def rule_binoculars(self):
        """An optical instrument consisting of two identical or mirror-symmetrical telescopes mounted side-by-side, allowing the user to view distant objects with both eyes simultaneously."""
        self.response = {
            'concept': 'Binoculars',
            'explanation': """An optical instrument consisting of two identical or mirror-symmetrical telescopes mounted side-by-side, allowing the user to view distant objects with both eyes simultaneously.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Using binoculars to observe birds in a forest.", "Watching a distant sporting event with enhanced clarity.", "Astronomers using binoculars for skygazing."]
        }
        self.halt()

    @Rule(Fact(query_topic='focal'))
    def rule_focal(self):
        """Pertaining to the focal point or focus, which is the point where parallel rays of light converge after passing through a lens or being reflected by a mirror."""
        self.response = {
            'concept': 'Focal',
            'explanation': """Pertaining to the focal point or focus, which is the point where parallel rays of light converge after passing through a lens or being reflected by a mirror.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The focal length of a camera lens.", "Light converging at the focal point of a concave mirror.", "The focal plane where an image is formed."]
        }
        self.halt()

    @Rule(Fact(query_topic='incident_ray'))
    def rule_incident_ray(self):
        """A ray of light that strikes a surface, lens, or mirror before any reflection or refraction occurs."""
        self.response = {
            'concept': 'Incident ray',
            'explanation': """A ray of light that strikes a surface, lens, or mirror before any reflection or refraction occurs.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A laser beam hitting a prism.", "Sunlight falling onto a magnifying glass.", "Light from a bulb striking a mirror."]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_incidence'))
    def rule_angle_of_incidence(self):
        """The angle between the incident ray and the normal (a line perpendicular to the surface) at the point where the light ray strikes the surface."""
        self.response = {
            'concept': 'Angle of incidence',
            'explanation': """The angle between the incident ray and the normal (a line perpendicular to the surface) at the point where the light ray strikes the surface.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Measuring the angle of a light ray hitting a water surface.", "The angle at which light strikes a mirror.", "The angle of entry for a light ray into a glass block."]
        }
        self.halt()

    @Rule(Fact(query_topic='refraction'))
    def rule_refraction(self):
        """The bending of light (or other waves) as it passes from one medium to another due to a change in its speed."""
        self.response = {
            'concept': 'Refraction',
            'explanation': """The bending of light (or other waves) as it passes from one medium to another due to a change in its speed.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A straw placed in a glass of water appearing bent.", "Light passing through a prism to separate into colors.", "The apparent shift in position of an underwater object."]
        }
        self.halt()

    @Rule(Fact(query_topic='refractive_index'))
    def rule_refractive_index(self):
        """A dimensionless number that describes how light, or any other radiation, propagates through a medium. It is the ratio of the speed of light in a vacuum to its speed in the medium."""
        self.response = {
            'concept': 'Refractive index',
            'explanation': """A dimensionless number that describes how light, or any other radiation, propagates through a medium. It is the ratio of the speed of light in a vacuum to its speed in the medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Water having a refractive index of approximately 1.33.", "Diamond having a high refractive index of about 2.42.", "The refractive index of air being very close to 1."]
        }
        self.halt()

    @Rule(Fact(query_topic='refracted'))
    def rule_refracted(self):
        """Describing a light ray or wave that has undergone the process of refraction, meaning it has bent after passing from one medium to another."""
        self.response = {
            'concept': 'Refracted',
            'explanation': """Describing a light ray or wave that has undergone the process of refraction, meaning it has bent after passing from one medium to another.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The refracted light rays from a lens forming an image.", "The color spectrum produced by refracted sunlight through a prism.", "Observing the refracted image of a fish in a pond."]
        }
        self.halt()

    @Rule(Fact(query_topic='angle_of_refraction'))
    def rule_angle_of_refraction(self):
        """The angle between the refracted ray and the normal (a line perpendicular to the surface) at the point where the light ray leaves or enters the new medium."""
        self.response = {
            'concept': 'Angle of refraction',
            'explanation': """The angle between the refracted ray and the normal (a line perpendicular to the surface) at the point where the light ray leaves or enters the new medium.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Measuring how much light bends when entering glass from air.", "The angle at which light exits a water surface.", "The angle between the bent light ray and the normal."]
        }
        self.halt()

    @Rule(Fact(query_topic='convex_lens'))
    def rule_convex_lens(self):
        """A converging lens that is thicker in the middle and thinner at the edges, causing parallel light rays to converge to a single focal point."""
        self.response = {
            'concept': 'Convex lens',
            'explanation': """A converging lens that is thicker in the middle and thinner at the edges, causing parallel light rays to converge to a single focal point.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A magnifying glass to enlarge small objects.", "The lens in a camera focusing light onto the sensor.", "Corrective lenses for farsightedness."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_lens'))
    def rule_concave_lens(self):
        """A diverging lens that is thinner in the middle and thicker at the edges, causing parallel light rays to spread out or diverge."""
        self.response = {
            'concept': 'Concave lens',
            'explanation': """A diverging lens that is thinner in the middle and thicker at the edges, causing parallel light rays to spread out or diverge.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["A peephole in a door to provide a wide view.", "Corrective lenses for nearsightedness (myopia).", "Used in some telescopes as part of an eyepiece system."]
        }
        self.halt()

    @Rule(Fact(query_topic='convex_mirror'))
    def rule_convex_mirror(self):
        """A diverging mirror that curves outwards, reflecting light outwards and producing a wider field of view with smaller, virtual images."""
        self.response = {
            'concept': 'Convex mirror',
            'explanation': """A diverging mirror that curves outwards, reflecting light outwards and producing a wider field of view with smaller, virtual images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Rear-view mirrors in vehicles.", "Security mirrors in shops and hospitals.", "Decorative mirrors to make a room appear larger."]
        }
        self.halt()

    @Rule(Fact(query_topic='concave_mirror'))
    def rule_concave_mirror(self):
        """A converging mirror that curves inwards, reflecting light inwards to a single focal point and capable of producing both real and virtual images."""
        self.response = {
            'concept': 'Concave mirror',
            'explanation': """A converging mirror that curves inwards, reflecting light inwards to a single focal point and capable of producing both real and virtual images.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["Shaving mirrors to magnify the face.", "Headlights of a car to focus light into a beam.", "Used in reflecting telescopes to gather light from distant objects."]
        }
        self.halt()

    @Rule(Fact(query_topic='real_image'))
    def rule_real_image(self):
        """An image formed when actual light rays converge at a point, which can be projected onto a screen."""
        self.response = {
            'concept': 'Real image',
            'explanation': """An image formed when actual light rays converge at a point, which can be projected onto a screen.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The image projected onto a cinema screen.", "The image formed by a camera lens on its sensor.", "The image formed by a slide projector."]
        }
        self.halt()

    @Rule(Fact(query_topic='virtual_image'))
    def rule_virtual_image(self):
        """An image formed when light rays appear to diverge from a point, but do not actually converge. It cannot be projected onto a screen."""
        self.response = {
            'concept': 'Virtual image',
            'explanation': """An image formed when light rays appear to diverge from a point, but do not actually converge. It cannot be projected onto a screen.""",
            'topic': 'Physics',
            'subtopic': 'Geometrical Optics',
            'examples': ["The image seen in a plane mirror.", "The magnified image produced by a magnifying glass.", "The image formed by a concave lens."]
        }
        self.halt()

