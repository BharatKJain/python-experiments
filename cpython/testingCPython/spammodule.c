#include <stdio.h>
#include <Python.h>
/*
NOTE:
For convenience, and since they are used extensively by the Python interpreter, 
"Python.h" includes a few standard header files: <stdio.h>, <string.h>, <errno.h>, and <stdlib.h>. 
If the latter header file does not exist on your system, it declares the functions malloc(), free() and realloc() directly.
*/
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return Py_BuildValue("i", sts);
}
int main()
{

}