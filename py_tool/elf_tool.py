#!/usr/bin/env python
# coding=utf-8
# vim:ts=4:sw=4:et

#********************************************************************************************
#* Copyright (c) 2014 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: elf tool bundle.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-07-10    Larry Shen    Create this file
#********************************************************************************************

import os
import sys
import logging

file_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
main_path = os.path.abspath(os.path.join(file_path, '../..')).replace('\\', '/')
sys.path.append(main_path) # add application path to env

readelf_executant = main_path + '/bin/readelf'
fromelf_executant = 'C:/Keil_v5/ARM/ARMCC/bin/fromelf'

class ElfTool:
    @staticmethod
    def parse_elfinfo(elf):
        if elf != None:
            cmd = '"' + readelf_executant + '" -l "' + elf + '"'
            (ret, output) = Helper.interact_run(cmd)
            logging.info(output)

            if 0 == ret:
                output_arr = output.split('\n')
                for per_line in output_arr:
                    if per_line.find('LOAD') != -1:
                        flag = per_line.split('0x')[5]
                        vector_start = per_line.split()[3]
                        sp = vector_start
                        pc = hex(eval(sp) + 4)
                        if 'R E' in flag.upper() or 'RWE' in flag.upper():
                            return (0, sp, pc)
            logging.info('Fatal: cannot find entry.')
        else:
            logging.info('Fatal: cannot find elf file.')

        logging.info('Parse elf file error.')
        return (1, None, None)

    @staticmethod
    def get_entry(elf, compiler):
        if elf != None:
            cmd_pc = '"' + readelf_executant + '" -l "' + elf + '"'
            (ret_pc, output_pc) = Helper.interact_run(cmd_pc)
            logging.info(output_pc)
            pc = 0x00000004
            sp = 0x00000000
            if 0 == ret_pc:
                output_arr = output_pc.split('\n')
                for per_line in output_arr:
                    if per_line.find('Entry point') != -1:
                        vector_start = per_line.split()[2]
                        pc = vector_start
                        break
            else:
                logging.info('Fatal: cannot find entry.')

            cmd_sp = '"' + readelf_executant + '" -s "' + elf + '"'
            (ret_sp, output_sp) = Helper.interact_run(cmd_sp)
            if 0 == ret_sp:
                #please refer to link file for below stack naming
                ck = {'uv4' : 'ARM_LIB_STACK', 'kds' : '__StackTop', 'armgcc' : '__StackTop', 'mcux': '__StackTop', 'lpcx': '__StackTop', 'iar': 'CSTACK$$Limit'}
                output_arr = output_sp.split('\n')
                for per_line in output_arr:
                    if per_line.find(ck[compiler]) != -1:
                        sp_top = per_line.split()[1]
                        logging.info(sp_top)
                        #we will destry the rom code ram for now
                        sp = hex(int(sp_top, 16) - 1)
                        break
            else:
                logging.info('Fatal: cannot find stack top.')

            if 0 == ret_sp and 0 == ret_pc:
                return (0, sp, pc)
            logging.info('Fatal: cannot find entry.')
        else:
            logging.info('Fatal: cannot find elf file.')

        logging.info('Parse elf file error.')
        return (1, None, None)

    @staticmethod
    def axf2hex(axf):
        cmd = '"' + fromelf_executant + '" "' + axf + '" --i32combined --output "' + axf + '.hex"'
        (ret, output) = Helper.interact_run(cmd)
        logging.info(output)

        return ret

    @staticmethod
    def axf2srec(axf):
        cmd = '"' + fromelf_executant + '" "' + axf + '" --m32combined --output "' + os.path.splitext(axf)[0] + '.srec"'
        (ret, output) = Helper.interact_run(cmd)
        logging.info(output)
        return ret
