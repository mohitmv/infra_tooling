import os, infra_lib

configs = infra_lib.Object();
configs.package = "infra_tooling"
configs.prod_cc_flags = " -Wno-unused-function  -Wno-unused-parameter -Wno-unused-local-typedefs -Werror ";
configs.global_include_dir = [];
configs.active_remote_branch = "master";
configs.toolchain_path = os.path.expanduser("~/toolchain");
configs["CCFLAGS"] = "--std=c++14 -O0 -Wall -Wextra -Wno-sign-compare -fno-omit-frame-pointer -Wnon-virtual-dtor -mpopcnt -msse4.2 -g3 -Woverloaded-virtual -Wno-char-subscripts -Werror=deprecated-declarations -Wa,--compress-debug-sections -fdiagnostics-color=always ";

br = infra_lib.BuildRule();
configs.dependency_configs = [
  br.CppProgram("src/libx",
                hdrs = ["include/libx.hpp"],
                srcs = ["src/libx.cpp"]),
];

