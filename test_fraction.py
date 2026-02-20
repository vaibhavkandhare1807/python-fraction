
import pytest
from fraction import Fraction
# Construction & Normalization

def test_basic_fraction():
    assert str(Fraction(1,2))=="1/2"

def test_basic_reduction():
    assert str(Fraction(4,8))=="1/2"

def test_large_reduction():
    assert str(Fraction(100,200))=="1/2"

def test_whole_number():
    assert str(Fraction(6,2))=="3"

def test_zero_numerator():
    assert str(Fraction(0,5))=="0"

def test_default_denominator():
    assert str(Fraction(7))=="7"

def test_denominator_one_hidden():
    assert str(Fraction(5,1))=="5"

def test_negative_numerator():
    assert str(Fraction(-1,2))=="-1/2"

def test_negative_denominator():
    assert str(Fraction(1,-2))=="-1/2"

def test_double_negative():
    assert str(Fraction(-1,-2))=="1/2"

def test_zero_denominator_raises():
    with pytest.raises(ValueError):
        Fraction(1,0)

def test_string_numerator_raises():
    with pytest.raises(TypeError):
        Fraction("1",2)

def test_list_denominator_raises():
    with pytest.raises(TypeError):
        Fraction(1,[2])

def test_none_numerator_raises():
    with pytest.raises(TypeError):
        Fraction(None)

def test_zero_denominator_raises():
    with pytest.raises(ValueError):
        Fraction(1,0)

def test_fraction_over_zero_fraction_denominator():
    with pytest.raises(ValueError):
        Fraction(1,Fraction(0))

def test_fraction_zero_float_denominator():
    with pytest.raises(ValueError):
        Fraction(1,0.0)



# Float Construction

def test_float_half():
    assert str(Fraction(0.5))=="1/2"

def test_float_quarter():
    assert str(Fraction(0.25))=="1/4"

def test_float_three_quarters():
    assert str(Fraction(0.75))=="3/4"

def test_float_negative():
    assert str(Fraction(-0.5))=="-1/2"

def test_float_whole():
    assert str(Fraction(1.0))=="1"

def test_float_numerator_int_denominator():
    assert str(Fraction(0.5,2))=="1/4"

def test_float_numerator_float_denominator():
    assert str(Fraction(0.5,0.25))=="2"

# Fraction as Numerator / Denominator

def test_fraction_over_fraction():
    assert str(Fraction(Fraction(1,2),Fraction(1,4)))=="2"

def test_int_over_fraction():
    assert str(Fraction(3,Fraction(1,4)))=="12"

def test_fraction_over_int():
    assert str(Fraction(Fraction(1,2),2))=="1/4"

# Addition

def test_addition():
    assert Fraction(1,2)+Fraction(1,3)==Fraction(5,6)

def test_addition_int():
    assert Fraction(1,2)+1==Fraction(3,2)

def test_addition_float_returns_float():
    assert type(Fraction(1,2)+0.5) is float

def test_addition_float_value():
    assert Fraction(1,2)+0.5==1.0

def test_radd_int():
    assert 1+Fraction(1,2)==Fraction(3,2)

def test_radd_float():
    assert 0.5+Fraction(1,2)==1.0

def test_addition_with_zero():
    assert Fraction(0)+Fraction(1,2)==Fraction(1,2)

def test_addition_result_negative():
    assert Fraction(1,3)+Fraction(-1,2)==Fraction(-1,6)


# Subtraction

def test_subtraction():
    assert Fraction(1,2)-Fraction(1,3)==Fraction(1,6)

def test_subtraction_int():
    assert Fraction(1,2)-1==Fraction(-1,2)

def test_subtraction_float_returns_float():
    assert type(Fraction(1,2)-0.5) is float

def test_rsub_int():
    assert 1-Fraction(1,2)==Fraction(1,2)

def test_subtraction_result_negative():
    assert Fraction(1,3)-Fraction(1,2)==Fraction(-1,6)

# Multiplication

def test_multiplication():
    assert Fraction(1,2)*Fraction(1,3)==Fraction(1,6)

def test_multiplication_int():
    assert Fraction(1,2)*2==Fraction(1)

def test_multiplication_float_returns_float():
    assert type(Fraction(1,2)*0.5) is float

def test_rmul_int():
    assert 2*Fraction(1,2)==Fraction(1)

def test_multiply_by_zero():
    assert Fraction(3,4)*0==Fraction(0)

def test_multiply_negative():
    assert Fraction(1,2)*Fraction(-1,3)==Fraction(-1,6)

# Division

def test_division():
    assert Fraction(1,2) / Fraction(1,3)==Fraction(3,2)

def test_division_int():
    assert Fraction(1,2) / 2==Fraction(1,4)

def test_division_float_returns_float():
    assert type(Fraction(1,2) / 0.5) is float

def test_rtruediv_int():
    assert 2 / Fraction(1,2)==Fraction(4)

def test_rtruediv_float():
    assert 1.0 / Fraction(1,2)==2.0

def test_division_by_zero_int():
    with pytest.raises(ZeroDivisionError):
        Fraction(1,2) / 0

def test_division_by_zero_float():
    with pytest.raises(ZeroDivisionError):
        Fraction(1,2) / 0.0

def test_division_by_zero_fraction():
    with pytest.raises(ZeroDivisionError):
        Fraction(1,2) / Fraction(0)

def test_rtruediv_zero_self():
    with pytest.raises(ZeroDivisionError):
        1 / Fraction(0)


# Chaining

def test_chain_addition():
    assert Fraction(1,2)+Fraction(1,3)+Fraction(1,6)==Fraction(1)

def test_chain_mixed():
    assert Fraction(1,2)*2-Fraction(1,4)==Fraction(3,4)


# Unary Operators

def test_negation():
    assert str(-Fraction(1,2))=="-1/2"

def test_double_negation():
    assert str(-(-Fraction(1,2)))=="1/2"

def test_positive():
    assert str(+Fraction(1,2))=="1/2"

def test_abs_positive():
    assert abs(Fraction(1,2))==Fraction(1,2)

def test_abs_negative():
    assert abs(Fraction(-1,2))==Fraction(1,2)

# Comparison Operators

def test_equal_fractions():
    assert Fraction(1,2)==Fraction(2,4)

def test_equal_int():
    assert Fraction(4,2)==2

def test_equal_float():
    assert Fraction(1,2)==0.5

def test_not_equal():
    assert Fraction(1,2)!=Fraction(1,3)

def test_less_than():
    assert Fraction(1,3)<Fraction(1,2)

def test_less_than_int():
    assert Fraction(1,2)<1

def test_greater_than():
    assert Fraction(1,2)>Fraction(1,3)

def test_greater_than_int():
    assert Fraction(3,2)>1

def test_less_than_or_equal_equal():
    assert Fraction(1,2)<=Fraction(1,2)

def test_less_than_or_equal_less():
    assert Fraction(1,3)<=Fraction(1,2)

def test_greater_than_or_equal_equal():
    assert Fraction(1,2)>=Fraction(1,2)

def test_greater_than_or_equal_greater():
    assert Fraction(1,2)>=Fraction(1,3)

def test_negative_comparison():
    assert Fraction(-1,3)<Fraction(1,2)

def test_eq_unknown_type_returns_not_implemented():
    assert Fraction(1,2).__eq__([1,2]) is NotImplemented

def test_ne_unknown_type_returns_not_implemented():
    assert Fraction(1,2).__ne__([1,2]) is NotImplemented

def test_eq_mixed_list_no_crash():
    assert Fraction(1,2) in [Fraction(1,2),"hello",42]

# Bool,Int,Float Conversions

def test_bool_nonzero_true():
    assert bool(Fraction(1,2)) is True

def test_bool_zero_false():
    assert bool(Fraction(0)) is False

def test_bool_negative_true():
    assert bool(Fraction(-1,2)) is True

def test_float_conversion():
    assert float(Fraction(1,4))==0.25

def test_int_positive_truncation():
    assert int(Fraction(7,2))==3

def test_int_truncates_toward_zero():
    assert int(Fraction(-7,2))==-3

def test_int_negative_half():
    assert int(Fraction(-1,2))==0

def test_int_exact():
    assert int(Fraction(6,2))==3

def test_int_large_no_float_precision_loss():
    assert int(Fraction(10**30+1,10**30))==1

# Hash

def test_hash_consistency_with_float():
    assert hash(Fraction(1,2))==hash(0.5)

def test_hash_consistency_with_int():
    assert hash(Fraction(2,1))==hash(2)

def test_hash_equal_fractions_same_hash():
    assert hash(Fraction(1,2))==hash(Fraction(2,4))

def test_hash_set_deduplication():
    s = {Fraction(1,2),0.5,Fraction(2,4)}
    assert len(s)==1

def test_hash_dict_lookup_by_float():
    d = {Fraction(1,2): "half"}
    assert d[0.5]=="half"

def test_hash_dict_lookup_by_int():
    d = {Fraction(2,1): "two"}
    assert d[2]=="two"

def test_hash_mixed_set_size():
    s = {Fraction(2,1),2,Fraction(1,2),0.5}
    assert len(s)==2

# Reciprocal

def test_reciprocal_basic():
    assert str(Fraction(1,2).reciprocal())=="2"

def test_reciprocal_fraction():
    assert str(Fraction(2,3).reciprocal())=="3/2"

def test_reciprocal_negative():
    assert str(Fraction(-1,2).reciprocal())=="-2"

def test_reciprocal_zero_raises():
    with pytest.raises(ValueError):
        Fraction(0).reciprocal()


# is_proper / is_improper

def test_is_proper_true():
    assert Fraction(1,2).is_proper() is True

def test_is_proper_false_improper():
    assert Fraction(3,2).is_proper() is False

def test_is_proper_false_equal():
    assert Fraction(1,1).is_proper() is False

def test_is_improper_true():
    assert Fraction(3,2).is_improper() is True

def test_is_improper_true_equal():
    assert Fraction(1,1).is_improper() is True

def test_is_improper_false():
    assert Fraction(1,2).is_improper() is False

def test_is_proper_negative():
    assert Fraction(-1,2).is_proper() is True

def test_is_improper_negative():
    assert Fraction(-3,2).is_improper() is True


# to_tuple / to_string

def test_to_tuple():
    assert Fraction(3,4).to_tuple()==(3,4)

def test_to_tuple_reduced():
    assert Fraction(2,4).to_tuple()==(1,2)

def test_to_string_fraction():
    assert Fraction(3,4).to_string()=="3/4"

def test_to_string_whole_number():
    assert Fraction(3,1).to_string()=="3/1"

def test_to_string_zero():
    assert Fraction(0,5).to_string()=="0/1"

# from_string

def test_from_string_fraction():
    assert str(Fraction.from_string("1/2"))=="1/2"

def test_from_string_negative():
    assert str(Fraction.from_string("-3/4"))=="-3/4"

def test_from_string_whole():
    assert str(Fraction.from_string("5"))=="5"

def test_from_string_strips_whitespace():
    assert str(Fraction.from_string("  2/4  "))=="1/2"

def test_from_string_zero():
    assert str(Fraction.from_string("0"))=="0"

def test_from_string_non_string_raises():
    with pytest.raises(TypeError):
        Fraction.from_string(123)

def test_from_string_bad_format_raises():
    with pytest.raises(ValueError):
        Fraction.from_string("1/2/3")

def test_from_string_letters_raises():
    with pytest.raises(ValueError):
        Fraction.from_string("a/b")

def test_from_string_zero_denominator_raises():
    with pytest.raises(ValueError):
        Fraction.from_string("1/0")

def test_from_string_empty_raises():
    with pytest.raises(ValueError):
        Fraction.from_string("")

def test_from_string_slash_only_raises():
    with pytest.raises(ValueError):
        Fraction.from_string("/")

# from_float

def test_from_float_half():
    assert str(Fraction.from_float(0.5))=="1/2"

def test_from_float_quarter():
    assert str(Fraction.from_float(0.25))=="1/4"

def test_from_float_negative():
    assert str(Fraction.from_float(-0.5))=="-1/2"

def test_from_float_whole():
    assert str(Fraction.from_float(1.0))=="1"

def test_from_float_non_float_raises():
    with pytest.raises(TypeError):
        Fraction.from_float(1)

def test_from_float_bad_precision_raises():
    with pytest.raises(ValueError):
        Fraction.from_float(0.5,9)

def test_from_float_non_int_precision_raises():
    with pytest.raises(TypeError):
        Fraction.from_float(0.5,2.0)

def test_from_float_precision_zero():
    assert str(Fraction.from_float(0.7,0))=="1"

def test_from_float_high_precision():
    assert Fraction.from_float(0.3,8)==Fraction(3,10)

# Edge Cases

def test_zero_plus_fraction():
    assert Fraction(0)+Fraction(1,2)==Fraction(1,2)

def test_zero_times_fraction():
    assert Fraction(0)*Fraction(1,2)==Fraction(0)

def test_very_large_fraction():
    assert str(Fraction(10**9,2*10**9))=="1/2"

def test_fraction_equals_itself():
    f = Fraction(3,4)
    assert f==f

def test_unsupported_operand_add():
    with pytest.raises(TypeError):
        Fraction(1,2)+"x"

def test_unsupported_operand_mul():
    with pytest.raises(TypeError):
        Fraction(1,2)*None
