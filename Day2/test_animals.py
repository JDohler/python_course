# Import classes from your brand new package
import animals

# Create an object of Birds class & call its method
MembBirds_dangerous = animals.dangerous.Birds()
MembBirds_dangerous.outMembers()

MembBirds_harmless = animals.harmless.Birds()
MembBirds_harmless.outMembers()

# Create an object of Mammals class & call its method
MembMammals_dangerous = animals.dangerous.Mammals()
MembMammals_dangerous.outMembers()

MembMammals_harmless = animals.harmless.Mammals()
MembMammals_harmless.outMembers()

# Create an object of Fish class & call its method
MembFish_dangerous = animals.dangerous.Fish()
MembFish_dangerous.outMembers()

MembFish_harmless = animals.harmless.Fish()
MembFish_harmless.outMembers()