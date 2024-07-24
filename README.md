double estimate_pi(int num_points) {
    int inside_circle = 0;
    for (int i = 0; i < num_points; ++i) {
        double x = static_cast<double>(rand()) / RAND_MAX;
        double y = static_cast<double>(rand()) / RAND_MAX;
        if (x * x + y * y <= 1) {
            inside_circle++;
        }
    }
    return 4.0 * inside_circle / num_points;  
    （Serial code to estimate the value of pi）

    Modify the previous serial code and add OpenMP directives to generate and count random points in parallel on multiple threads.

    
    #pragma omp parallel for reduction(+:inside_circle)
    for (int i = 0; i < num_points; ++i) {
        double x = static_cast<double>(rand()) / RAND_MAX;
        double y = static_cast<double>(rand()) / RAND_MAX;
        if (x * x + y * y <= 1) {
            inside_circle++;
        }
    }
    return 4.0 * inside_circle / num_points;
}

Parallel region: Use the #pragma omp parallel for directive to define a parallel region. The loops in this region will be executed in parallel by multiple threads.
Reduction operation: Use the reduction(+:inside_circle) directive to ensure that the accumulation operation on inside_circle is thread-safe.

int main() {
srand(static_cast<unsigned>(time(0))); // Set the random number seed
int num_points = 100000000; // Set the number of points
int num_threads = 6; // Set the number of threads



Thread safety means that during parallel execution, multiple threads accessing shared resources will not cause data race conditions and inconsistent results.
For shared variables that need to be accumulated or summed between multiple threads, use the reduction keyword to ensure that updates to the shared variables in the parallel region are thread-safe.

By adding #pragma omp parallel for reduction(+:inside_circle), the parallel version of the code can take advantage of the computing power of multi-core processors and speed up the Monte Carlo simulation process.
