#!/usr/bin/perl
use feature 'say';
print "Hello World \n";

$employee_name="Sagar";
$employee_age=23;
$employee_salary=440.5;


# String/integer/float assignment beginning with $, they call it scalar

print "Age = $employee_age\n";
print "Name = $employee_name\n";
print "Salary = $employee_salary\n";

# Array variables are preceeded by @
@names = ("M", "MM", "TT");
@ages = (25,28,31);

print("\$ages[1] = $ages[1] \n");
print("\$ages[2] = $ages[2] \n");
print("@ages\n");

say "Hello";

# Hash: key value pair
%data = ('Danish', 28, 'Raju', 40, 'Ritesh', 25);
print "\$data{'Danish'} = $data{'Danish'}\n";
print "\$data{'Raju'} = $data{'Raju'}\n";
print "\$data{'Ritesh'} = $data{'Ritesh'}\n";


# String operations
$string1 = "potato";
$string2 = "head";
$newstring = $string1.$string2;
print "$newstring \n";

$stringvar = "abc";
$stringvar++;
print "$stringvar \n";

$newstring = "t"x5;
print "$newstring \n";

$str = "z";
$str++;
print "$str \n";

# list in perl: lists are collection of scalars
@list1 = (a,b,c,d); # list of characters
@list2 = (1,2,3,4); # list of integers
@list3 = ("this", "is", "a", "list"); # list of strings
print "@list1\n";
print "@list2\n";
print "@list3\n";

# how to access element in a list
@names = (Danish, Satish, Rajesh, Manju, Uma);
$array_element=$names[2];
print "$array_element \n";
print "$names[-1] \n";

# Slicing an array
@new_names = @names[0,2,4];
print "@new_names \n";

# sort
@list1 = (1..10);
print(@list1);
print("@list1 \n");

@list2 = (2,5..9,11);
print("@list2 \n");

@list3 = (2.1..4.5);
print("@list3 \n");

@list4 = (aa..ad);
print("@list4 \n");

@numbers = (9, 2, 8, 4, 1);
@names = (" Rosy ", " Manesh ", " ruby ");
@sorted_numb= sort @numbers;
@descend_numb = reverse sort @numbers;

print("@sorted_numb \n");
print("@descend_numb \n");

# merge the lements of an array into a single string
$string5 = join(" ", " test1 ", " test2 ", @list4);
print("$string5 \n");

# split a string into array elements
$long_string = "words::separated::by::colons";
@array_split = split(/::/, $long_string);
print("@array_split \n");

$short_string = "abcde";
@short_split = split(//, $short_string);
print("@short_split \n");

# if condition in perl
$salary = 10500;

if ($salary > 10000){
    print "Employee is Manager \n";
}
elsif ($salary < 10000){
    print "Employee is staff\n";
}

# Unless condition
$a = 22;
unless($a < 20)
{
    print ("a is greater than 20 \n");
}

# switch
#
