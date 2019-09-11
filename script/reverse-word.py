s = "Keeper,GladiatorTrainer,TortureChamber,Gate,Keeper,GladiatorTrainer,TortureChamber,Gate,Keeper,GladiatorTrainer,TortureChamber,Gate,Keeper,GladiatorTrainer,TortureChamber,Gate,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,SoulExtractor,HeartOfDarkness,SoulExtractor,HeartOfDarkness,SoulExtractor,HeartOfDarkness,SoulExtractor,HeartOfDarkness,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,Keeper,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,TimeMachine,TimeMachine,TimeMachine,TimeMachine,TimeMachine,Keeper,Keeper,Keeper,Keeper,Keeper,GoldPit,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,GoldPit,GoldPit,GoldPit,GoldPit,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,GladiatorTrainer,GladiatorTrainer,GladiatorTrainer,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,TortureChamber,TortureChamber,Gate,SoulExtractor,HeartOfDarkness,GoblinPit,Gate,SoulExtractor,HeartOfDarkness"
words = s.split(',') 
string =[] 
for word in words: 
    string.insert(0, word) 
  
print(",".join(string)) 
