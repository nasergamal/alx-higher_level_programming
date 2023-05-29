#include <stdio.h>
#include <Python.h>
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print some info
 * @p: pyobject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i;
	PyObject *ob;

	fflush(stdout);	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < (int)PyList_GET_SIZE(p); i++)
	{
		ob = ((PyListObject *)(p))->ob_item[i];
		printf("Element %d: %s\n", i, (ob)->ob_type->tp_name);
		if (!strcmp(ob->ob_type->tp_name, "bytes"))
			print_python_bytes(ob);
	}
}
/**
 * print_python_bytes - print some info
 * @p: pyobject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int si, i;
	char *s;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)p)->ob_sval;
	si = PyBytes_Size(p);
	printf("  size: %d\n", si);
	printf("  trying string: %s\n", s);
	si = si < 10 ? si + 1 : 10;

	printf("  first %d bytes: ", si);
	for (i = 0; i < si; i++)
	{
		if (i != si - 1)
			printf("%02hhx ", s[i]);
		else
			printf("%02hhx\n", s[i]);
	}
}

/**
 * print_python_float - print float type data details
 * @p: pyobject
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	fflush(stdout);
	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %s\n",
		(char *)(PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
		'r', 0, Py_DTSF_ADD_DOT_0, NULL)));
}
