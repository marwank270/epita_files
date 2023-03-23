// Dependencies
#include <stddef.h>

typedef struct s_vector
{
    void *data_array;       // Pointer to a storage space in the memory
    size_t sizeof_data;     // Size of one element handled by the vector/array
    size_t array_capacity;  // Actual capacity of the vector/array
    size_t data_count;      // Number of elements in the vector/array
}; typedef struct s_vector t_vector;

t_vector *_efvector_new(size_t sizeof_data, size_t initial_capacity);

#define efvector_new(type, initial_capacity)