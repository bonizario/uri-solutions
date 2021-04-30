# Remove executable and tmp files
find ./problems/c -type f ! -name "*.c" -delete
find ./problems/cpp -type f ! -name "*.cpp" -delete
find ./problems/c -type f -name "tempCodeRunnerFile.c" -delete
find ./problems/cpp -type f -name "tempCodeRunnerFile.cpp" -delete
