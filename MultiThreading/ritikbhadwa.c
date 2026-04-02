#include <stdio.h>

void traverse(int arr[], int);
void insert(int arr[], int, int, int);
void insert_begin(int arr[], int, int);
void insert_end(int arr[], int, int);
void delete(int arr[], int, int);
void delete_begin(int arr[], int);
void delete_end(int arr[], int);
void update(int arr[], int, int, int);

//---------main function-----------

int main()
{
    int n;

    printf("Enter the size of array : ");
    scanf("%d", &n);

    int a[n], x, value, value1, value2, y, z, value3;

    for(int i=0; i<n; i++)
    {
        printf("Element-%d : ", i+1);
        scanf("%d", &a[i]);
    }

//-------Traverse-----------

    traverse(a, n);

//-------Insertion----------

    //------At any position--------

    printf("\nEnter the index you want to insert at and the value to insert (index value): ");
    scanf("%d %d", &x, &value);

    insert(a, n, x, value);

    //------At beginning--------

    printf("\nEnter the value to insert at beginning : ");
    scanf("%d", &value1);

    insert_begin(a, n+1, value1);

    //-------At end---------

    printf("\nEnter the value to insert at the end : ");
    scanf("%d", &value2);

    insert_end(a, n+2, value2);

//-------Deletion--------

    //-------From any position(Doubt)--------

    printf("\nEnter the index to delete : ");
    scanf("%d", &y);

    delete(a, n+2, y);

    //-------From beginning(Doubt)--------

    printf("\nArray after deleting the first element : \n");
    delete_begin(a, n-1);

    //-------From end-----------

    printf("\nArray after deleting the last element : \n");
    delete_end(a, n-2);

//---------Updation---------

    printf("\nEnter the index and value for updation(index value) : ");
    scanf("%d %d", &z, &value3);

    update(a, n-3, z, value3);

    return 0;
}

//--------Functions------------

void traverse(int arr[], int n)
{
    int i=0;
    while (i<n)
    {
        printf("%d ", arr[i]);
        i++;
    }
}

void insert(int arr[], int size, int index, int value)
{
    if(index > size)
    {
        printf("Invalid index");
    }
   
    int i = size - 1;
    size = size + 1;
    while (i >= index - 1)
    {
        arr[i+1] = arr[i];
        i--;
    }
    arr[index-1] = value;

    traverse(arr, size);
}

void insert_begin(int arr[], int size, int value)
{
    int i = size - 1;
    size = size + 1;
    while(i >= 0)
    {
        arr[i+1] = arr[i];
        i--;
    }
    arr[0] = value;

    traverse(arr, size);
}

void insert_end(int arr[], int size, int value)
{
    int i = size;
    size = size + 1;
    arr[i] = value;

    traverse(arr, size);
}

void delete(int arr[], int size, int index)
{
    if(index > size)
    {
        printf("Invalid index");
    }

  int i =index;
    while(i<size)
    {
    
            arr[i] = arr[i+1];
           
        
        i++;
    }
    // size = size - 1;

    traverse(arr, size);
}

void delete_begin(int arr[], int size)
{
    int i = 0;
    while(i < size-1)
    {
        arr[i] = arr[i+1];
        i++;
    }
    size = size - 1;

    traverse(arr, size);
}

void delete_end(int arr[], int size)
{
    size = size - 1;

    traverse(arr, size);
}

void update(int arr[], int size, int index, int value)
{
   
}