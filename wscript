APPNAME = "hello"

def options(opt):
	opt.load('compiler_cxx waf_unit_test')

def configure(cgf):
	cgf.load('compiler_cxx waf_unit_test')

def build(bld):
	assemble_executable(bld)
	test(bld)

def assemble_executable(bld):
	bld.stlib(
		source=bld.path.ant_glob('src/cpp/*.cpp'),
		includes='src/cpp',
		target='hlib')
	bld.program(
		source='src/main/main.cpp', 
		target=APPNAME,
		includes='src/cpp',
		use='hlib')

def test(bld):
	bld.stlib(
        source='contrib/gtest/src/gtest-all.cc', 
        includes=['contrib/gtest', 'contrib/gtest/include'],
        target='gtest')
	bld.stlib(
		source='contrib/gmock/src/gmock-all.cc',
		includes=['contrib/gmock', 'contrib/gmock/include', 'contrib/gtest/include'],
		target='gmock',
		use='gtest')
	bld.program(
		features='test',
		source=bld.path.ant_glob('src/test/*.cpp'),
		target='unittests',
		includes=['contrib/gmock/include', 'contrib/gtest/include', 'src/cpp'],
		use=['gmock', 'hlib'])

	from waflib.Tools import waf_unit_test
	bld.add_post_fun(waf_unit_test.summary)
	bld.add_post_fun(waf_unit_test.set_exit_code)
