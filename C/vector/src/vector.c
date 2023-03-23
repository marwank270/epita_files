// Dependencies
#include <stddef.h>

typedef struct s_vector
{
    void *data_array;
    size_t sizeof_data;
    size_t array_capacity;
    size_t data_count;
}; typedef struct s_vector t_vector;

t_vector *_efvector_new(size_t sizeof_data, size_t initial_capacity)
{
    
}