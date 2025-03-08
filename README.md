# DiceNumbering
Code used to generate optimal and sub-optimal dice numberings

The two python scripts are used to find the dice numbering with the minimum bias vector.
For each dice you are required to input the number of dice faces, and a vector in 2D or 3D space for each face.

The "NumberingScript" checks all numberings, ignoring a multiple of d. So it actually is not 100% effecient but for dice sizes up to 12 it works well enough.

The "EvolutionNumbering" was used to find the optimal d20 numbering and uses an evolution-based approach. This means that it doesn't check every possible numbering and will not always result in finding the optimal. Again its probably not well optimised.

Both scripts should be pretty simple to use and served my purposes. I am sure people better at coding than me can improve them.

Anyway, thanks for reading!
