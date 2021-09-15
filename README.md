# Table of Contents

- Requirements for the Task
- Overview
- API Reference
- Setup
- Creating and Adding Personal Details
- Displaying Personal Details
- Converting Personal Details
- Filtering Personal Details
- Adding a New Format
- Command Line Interface
  * PersonalDetails-add
  * Personaldetails-convert
  * Personaldetails-display
  * Personaldetails-filter
  
# Requirements for the Task

The brief is as follows:

In Python or C++ write a module or small library which shows how you would take a set of personal data, where each
record contains:

- name
- address
- phone number

And:

build a simple API allowing you to add new records, filter users (e.g "name=Joe*") based on some simple search syntax
like Glob. Support serialisation in 2 or more formats (e.g JSON, Yaml, XML, CSV etc). Display the data in 2 or more
different output formats (no need to use a GUI Framework, use e.g text output/HTML or any other human readable format).
Add a command line interface to add records, and display/convert/filter the whole data set. Write it in such a way that
it would be easy for a developer to extend the system e.g

- to add support for additional storage formats
- to query a list of currently supported formats

This should ideally show Object-Oriented Design and Design Patterns Knowledge, we’re not looking for use of advanced
Language constructs.

Please provide reasonable Unit Test coverage and basic API documentation

The task is designed to allow you some flexibility in how you design and implement it, and you should submit something
that demonstrates your abilities and/or values as a Software Engineer. 

# Overview

The set of scripts assists and contains tools and an API, which can be used to operate with personal information. The Personal information is collected and stored in the supported formats. The API helps in determining the format to be used based on the extension type, therefore you do not need to manually format.

## API Reference

API reference (Sphinx) of the package is available in `PersonalDetails/HTML/` folder.

# Setup

Add following to Python path.

- `PersonalDetails/python`

Import modules.

```python
from personlibrary import Person
from personalinfolibrary import PersonalDetails
```

Set the files, which we will use for serialization/deserialization.

```python
TEST_FOLDER = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'test'))

JSON_FILE   = os.path.join(TEST_FOLDER, 'PersonalDetails.json')

XML_FILE    = os.path.join(TEST_FOLDER, 'PersonalDetails.xml')
```

# Creating and Adding Personal Data

```python

# Create an instance of personlibrary/Person

p1 = Person(name='Steven Hosking',
            phoneNumber='02 9383 4865',
            address='22 Wallaby Way, Sydney')

# Create an instance of personalinfolibrary/PersonalDetails

pdinfo = PersonalDetails(filePath=JSON_FILE)

# Add the person

pdinfo.addByObject(p1, allowDuplicate=True)

# Serialize the data into the file

pdinfo.serialize(overwrite=True)
```

Operating on an existing files is exactly the same.

You can also use `pdinfo.add` method to provide raw
information to add a new peron.

```python
pdinfo = PersonalDetails(filePath=JSON_FILE)

pdinfo.add(name='P Sherman',
            phoneNumber='02 9383 4866',
            address='Moore Park, Fox Studios, Sydney',
            allowDuplicate=True)

pdinfo.serialize(overwrite=True)
```

# Displaying Personal Details

In order to display, you can invoke `pdinfo.display`.

```python
pdinfo = PersonalDetails(filePath=JSON_FILE)

pdinfo.deserialize()

pdinfo.display()
```

# Converting Personal Details

You can convert one format to another by using `pdinfo.convert` method.

```python
print pdinfo.getFormats()

#['JSON', 'XML']
```

Conversion is done like so;

```python
pdinfo = PersonalDetails(filePath=JSON_FILE)

pdinfo.deserialize()

pdinfo.convert(toFile=XML_FILE, overwrite=True, display=True)
```

The `convert` method accepts three arguments.

- `toFile` Destination file
- `overwrite` Whether `toFile` can be overwritten
- `display` Display data

# Filtering Personal Details

Filtering personal data is done by using `pdinfo.filter` method.

- `name`
- `phoneNumber`
- `address`

```python
pdinfo = PersonalData(filePath=JSON_FILE)

pdinfo.deserialize()

print pdinfo.filter(name='P*'))

print pdinfo.filter(name='P*', phoneNumber='2*', address='*moo'))
```

# Adding a New Format

Adding a new format is easy.

- Create a Python module named `personalinfoserializer<FORMAT>.py` in this package,
since in this example format is YAML, the name of the module must be `personalinfoserializerYAML.py`

- Create a class named `Serializing<FORMAT>` in this module that inherits `personalinfoserializerabsolute.Serializer`
abstract class.

- Overwrite `serialize` method

- Overwrite `deserialize` method

# Command Line Interface

The package comes with some useful commands that you can use.

## PersonalDetails-add

This is to add details and are saved to the file.

**Flags**

- `file`           File to be operated on.
- `-d --display`   Display data after the operation.

```shell script
PersonalDetails-add personaldetails.json -d
```

## PersonalDetails-convert

The extension of the file determines the conversion.

**Flags**

- `fromFile`          From file.
- `toFIle`            To file.
- `-o --overwrite`    Overwrite existing `toFile`
- `-d --display`      Display converted data after the operation.

```shell script
spersonaldata-convert personalData.json personalData.xml -o -d
```

## PersonalDetails-display

Displays data.

**Flags**

- `file` File being worked on.

```shell script
PersonalDetails-display personaldetails.json
```

## PersonalDetails-filter

This is to filter personal data from the file worked on. Prompts will request the name, phone number and address, none of these questions are mandatory to answer and wildcards can be used to filter.

**Flags**

- `file` File being worked on.

```shell script
PersonalDetails-filter personal.json
Name Filter: S*
Phone Number Filter: 2*
Address Filter:

# #Name        : P Sherman
# #Address     : 42 Wallaby Way, Sydney
# #Phone Number: 02 9383 4866
#
# #Name        : Steven Hosking
# #Address     : 22 Wallaby Way, Sydney
# #Phone Number: 02 9383 4866
