include(../../../cmake/utils.cmake)

add_executable(app "")
set(NRF52_SDK_ROOT_DIR ${CMAKE_CURRENT_LIST_DIR}/../../..)



target_sources(app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/main.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/mdk/gcc_startup_nrf52840.S
  ${NRF52_SDK_ROOT_DIR}/components/libraries/bsp/bsp.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/bsp/bsp_btn_ble.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/nrf_hw/nrf_hw_backend_init.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/nrf_hw/nrf_hw_backend_rng.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/nrf_hw/nrf_hw_backend_rng_mbedtls.c
  ${NRF52_SDK_ROOT_DIR}/components/boards/boards.c
  ${NRF52_SDK_ROOT_DIR}/integration/nrfx/legacy/nrf_drv_clock.c
  ${NRF52_SDK_ROOT_DIR}/integration/nrfx/legacy/nrf_drv_rng.c
  ${NRF52_SDK_ROOT_DIR}/integration/nrfx/legacy/nrf_drv_uart.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/soc/nrfx_atomic.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/nrfx_clock.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/nrfx_gpiote.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/prs/nrfx_prs.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/nrfx_rng.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/nrfx_uart.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/src/nrfx_uarte.c
  ${NRF52_SDK_ROOT_DIR}/modules/nrfx/mdk/system_nrf52840.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/button/app_button.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/util/app_error.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/util/app_error_handler_gcc.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/util/app_error_weak.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/scheduler/app_scheduler.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/timer/app_timer2.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/util/app_util_platform.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crc16/crc16.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/timer/drv_rtc.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/fds/fds.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/hardfault/hardfault_implementation.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/mem_manager/mem_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/util/nrf_assert.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/atomic_fifo/nrf_atfifo.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/atomic_flags/nrf_atflags.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/atomic/nrf_atomic.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/balloc/nrf_balloc.c
  ${NRF52_SDK_ROOT_DIR}/external/fprintf/nrf_fprintf.c
  ${NRF52_SDK_ROOT_DIR}/external/fprintf/nrf_fprintf_format.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/fstorage/nrf_fstorage.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/fstorage/nrf_fstorage_sd.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/memobj/nrf_memobj.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/pwr_mgmt/nrf_pwr_mgmt.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/queue/nrf_queue.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/ringbuf/nrf_ringbuf.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/experimental_section_vars/nrf_section_iter.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/sortlist/nrf_sortlist.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/strerror/nrf_strerror.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/sensorsim/sensorsim.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_backend_rtt.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_backend_serial.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_backend_uart.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_default_backends.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_frontend.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/log/src/nrf_log_str_formatter.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_aead.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_aes.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_aes_shared.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_ecc.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_ecdh.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_ecdsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_eddsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_error.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_hash.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_hkdf.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_hmac.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_init.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_rng.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/nrf_crypto_shared.c
  ${NRF52_SDK_ROOT_DIR}/components/softdevice/common/nrf_sdh.c
  ${NRF52_SDK_ROOT_DIR}/components/softdevice/common/nrf_sdh_ble.c
  ${NRF52_SDK_ROOT_DIR}/components/softdevice/common/nrf_sdh_soc.c
  ${NRF52_SDK_ROOT_DIR}/external/mbedtls/library/aes.c
  ${NRF52_SDK_ROOT_DIR}/external/mbedtls/library/ctr_drbg.c
  ${NRF52_SDK_ROOT_DIR}/external/mbedtls/library/platform_util.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/auth_status_tracker.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/common/ble_advdata.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/ble_advertising/ble_advertising.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/common/ble_conn_params.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/common/ble_conn_state.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/common/ble_srv_common.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/gatt_cache_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/gatts_cache_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/id_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/nrf_ble_gatt/nrf_ble_gatt.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/nrf_ble_lesc.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/nrf_ble_qwr/nrf_ble_qwr.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/peer_data_storage.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/peer_database.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/peer_id.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/peer_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/peer_manager_handler.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/pm_buffer.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/security_dispatcher.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager/security_manager.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_aes.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_aes_aead.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_chacha_poly_aead.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_ecc.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_ecdh.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_ecdsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_eddsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_hash.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_hmac.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_init.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_mutex.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_rng.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310/cc310_backend_shared.c
  ${NRF52_SDK_ROOT_DIR}/external/utf_converter/utf.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_bas/ble_bas.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_dis/ble_dis.c
  ${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_hrs/ble_hrs.c
  ${NRF52_SDK_ROOT_DIR}/external/segger_rtt/SEGGER_RTT.c
  ${NRF52_SDK_ROOT_DIR}/external/segger_rtt/SEGGER_RTT_Syscalls_GCC.c
  ${NRF52_SDK_ROOT_DIR}/external/segger_rtt/SEGGER_RTT_printf.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_chacha_poly_aead.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_ecc.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_ecdh.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_ecdsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_eddsa.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_hash.c
  ${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon/oberon_backend_hmac.c)



target_include_directories(app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/pca10056/s140/config
	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/generic/message
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t2t_lib
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t4t_parser/hl_detection_procedure
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_ancs_c
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_ias_c
  	${NRF52_SDK_ROOT_DIR}/components/libraries/pwm
  	${NRF52_SDK_ROOT_DIR}/external/nrf_oberon/include
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/cdc/acm
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/hid/generic
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/msc
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/hid
  	${NRF52_SDK_ROOT_DIR}/modules/nrfx/hal
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/conn_hand_parser/le_oob_rec_parser
  	${NRF52_SDK_ROOT_DIR}/components/libraries/log
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_gls
  	${NRF52_SDK_ROOT_DIR}/components/libraries/fstorage
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/text
  	${NRF52_SDK_ROOT_DIR}/components/libraries/mutex
  	${NRF52_SDK_ROOT_DIR}/components/libraries/gpiote
  	${NRF52_SDK_ROOT_DIR}/components/libraries/bootloader/ble_dfu
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/common
  	${NRF52_SDK_ROOT_DIR}/components/boards
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/generic/record
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t4t_parser/cc_file
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_advertising
  	${NRF52_SDK_ROOT_DIR}/external/utf_converter
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_bas_c
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/micro_ecc
  	${NRF52_SDK_ROOT_DIR}/modules/nrfx/drivers/include
  	${NRF52_SDK_ROOT_DIR}/components/libraries/experimental_task_manager
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_hrs_c
  	${NRF52_SDK_ROOT_DIR}/components/softdevice/s140/headers/nrf52
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/le_oob_rec
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/oberon
  	${NRF52_SDK_ROOT_DIR}/components/libraries/queue
  	${NRF52_SDK_ROOT_DIR}/components/libraries/pwr_mgmt
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_dtm
  	${NRF52_SDK_ROOT_DIR}/components/toolchain/cmsis/include
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_rscs_c
  	${NRF52_SDK_ROOT_DIR}/components/ble/common
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_lls
  	${NRF52_SDK_ROOT_DIR}/components/nfc/platform
  	${NRF52_SDK_ROOT_DIR}/components/libraries/bsp
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/nrf_hw
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/ac_rec
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_bas
  	${NRF52_SDK_ROOT_DIR}/components/libraries/mpu
  	${NRF52_SDK_ROOT_DIR}/components/libraries/experimental_section_vars
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_ans_c
  	${NRF52_SDK_ROOT_DIR}/components/libraries/slip
  	${NRF52_SDK_ROOT_DIR}/components/libraries/delay
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/cdc
  	${NRF52_SDK_ROOT_DIR}/components/libraries/memobj
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310_bl
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_nus_c
  	${NRF52_SDK_ROOT_DIR}/components/softdevice/common
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_ias
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/hid/mouse
  	${NRF52_SDK_ROOT_DIR}/components/libraries/low_power_pwm
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/conn_hand_parser/ble_oob_advdata_parser
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_dfu
  	${NRF52_SDK_ROOT_DIR}/external/fprintf
  	${NRF52_SDK_ROOT_DIR}/components/libraries/svc
  	${NRF52_SDK_ROOT_DIR}/components/libraries/atomic
  	${NRF52_SDK_ROOT_DIR}/components
  	${NRF52_SDK_ROOT_DIR}/external/nrf_cc310/include
  	${NRF52_SDK_ROOT_DIR}/components/libraries/scheduler
  	${NRF52_SDK_ROOT_DIR}/components/libraries/cli
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_lbs
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_hts
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crc16
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t4t_parser/apdu
  	${NRF52_SDK_ROOT_DIR}/components/libraries/util
  	${NRF52_SDK_ROOT_DIR}/components/libraries/csense_drv
  	${NRF52_SDK_ROOT_DIR}/components/libraries/csense
  	${NRF52_SDK_ROOT_DIR}/components/libraries/balloc
  	${NRF52_SDK_ROOT_DIR}/components/libraries/ecc
  	${NRF52_SDK_ROOT_DIR}/components/libraries/hardfault
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_cscs
  	${NRF52_SDK_ROOT_DIR}/components/libraries/hci
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/hid/kbd
  	${NRF52_SDK_ROOT_DIR}/components/libraries/timer
  	${NRF52_SDK_ROOT_DIR}/components/softdevice/s140/headers
  	${NRF52_SDK_ROOT_DIR}/integration/nrfx
  	${NRF52_SDK_ROOT_DIR}/components/libraries/stack_info
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t4t_parser/tlv
  	${NRF52_SDK_ROOT_DIR}/components/libraries/sortlist
  	${NRF52_SDK_ROOT_DIR}/components/libraries/spi_mngr
  	${NRF52_SDK_ROOT_DIR}/components/libraries/led_softblink
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/conn_hand_parser
  	${NRF52_SDK_ROOT_DIR}/components/libraries/sdcard
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t4t_lib
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/parser/record
  	${NRF52_SDK_ROOT_DIR}/modules/nrfx/mdk
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_cts_c
  	${NRF52_SDK_ROOT_DIR}/external/nrf_tls/mbedtls/nrf_crypto/config
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_nus
  	${NRF52_SDK_ROOT_DIR}/components/libraries/twi_mngr
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_hids
  	${NRF52_SDK_ROOT_DIR}/components/libraries/strerror
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crc32
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/ble_oob_advdata
  	${NRF52_SDK_ROOT_DIR}/components/nfc/t2t_parser
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/ble_pair_msg
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/optiga
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd/class/audio
  	${NRF52_SDK_ROOT_DIR}/components/libraries/sensorsim
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/nrf_sw
  	${NRF52_SDK_ROOT_DIR}/components/ble/peer_manager
  	${NRF52_SDK_ROOT_DIR}/components/libraries/mem_manager
  	${NRF52_SDK_ROOT_DIR}/components/libraries/ringbuf
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_tps
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_rscs
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/parser/message
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/mbedtls
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cc310
  	${NRF52_SDK_ROOT_DIR}/external/nrf_oberon
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_dis
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/uri
  	${NRF52_SDK_ROOT_DIR}/components/ble/nrf_ble_gatt
  	${NRF52_SDK_ROOT_DIR}/components/ble/nrf_ble_qwr
  	${NRF52_SDK_ROOT_DIR}/components/libraries/gfx
  	${NRF52_SDK_ROOT_DIR}/components/libraries/button
  	${NRF52_SDK_ROOT_DIR}/modules/nrfx
  	${NRF52_SDK_ROOT_DIR}/components/libraries/twi_sensor
  	${NRF52_SDK_ROOT_DIR}/integration/nrfx/legacy
  	${NRF52_SDK_ROOT_DIR}/components/libraries/usbd
  	${NRF52_SDK_ROOT_DIR}/external/mbedtls/include
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/ep_oob_rec
  	${NRF52_SDK_ROOT_DIR}/external/segger_rtt
  	${NRF52_SDK_ROOT_DIR}/components/libraries/atomic_fifo
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_lbs_c
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/ble_pair_lib
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_racp
  	${NRF52_SDK_ROOT_DIR}/components/libraries/fds
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/launchapp
  	${NRF52_SDK_ROOT_DIR}/components/libraries/atomic_flags
  	${NRF52_SDK_ROOT_DIR}/components/ble/ble_services/ble_hrs
  	${NRF52_SDK_ROOT_DIR}/components/libraries/crypto/backend/cifra
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/connection_handover/hs_rec
  	${NRF52_SDK_ROOT_DIR}/components/nfc/ndef/conn_hand_parser/ac_rec_parser
  	${NRF52_SDK_ROOT_DIR}/components/libraries/stack_guard
  	${NRF52_SDK_ROOT_DIR}/components/libraries/log/src)


target_link_libraries(app "${NRF52_SDK_ROOT_DIR}/external/nrf_cc310/lib/cortex-m4/hard-float/libnrf_cc310_0.9.13.a")
target_link_libraries(app "${NRF52_SDK_ROOT_DIR}/external/nrf_oberon/lib/cortex-m4/hard-float/liboberon_3.0.6.a")

target_compile_options(app PRIVATE -mcpu=cortex-m4 -mthumb -mabi=aapcs -mfloat-abi=hard -mfpu=fpv4-sp-d16)
target_compile_options(app PRIVATE $<$<COMPILE_LANGUAGE:C>:-Wall -Werror -g3 -O3 -gstrict-dwarf -ffunction-sections -fdata-sections -fno-strict-aliasing -fno-builtin -fshort-enums>)
target_compile_options(app PRIVATE $<$<COMPILE_LANGUAGE:ASM>:-x assembler-with-cpp -g3>)

target_compile_options(app PRIVATE "-fdebug-prefix-map=/app=.")
target_compile_options(app PRIVATE "-fmacro-prefix-map=/app=.")

target_compile_definitions(app PRIVATE FLOAT_ABI_HARD
	NRF52840_XXAA
	APP_TIMER_V2
	APP_TIMER_V2_RTC1_ENABLED
	BLE_STACK_SUPPORT_REQD
	BOARD_PCA10056
	__HEAP_SIZE=8192
	__STACK_SIZE=8192
	CONFIG_GPIO_AS_PINRESET
	FLOAT_ABI_HARD
	NRF_CRYPTO_MAX_INSTANCE_COUNT=1
	NRF_SD_BLE_API_VERSION=7
	S140
	SOFTDEVICE_PRESENT)

target_compile_definitions(app PRIVATE $<$<COMPILE_LANGUAGE:C>:MBEDTLS_CONFIG_FILE=\"nrf_crypto_mbedtls_config.h\">)

target_link_directories(app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/pca10056/s140/armgcc
	${NRF52_SDK_ROOT_DIR}/modules/nrfx/mdk)
target_link_options(app PRIVATE -g3 -O3 -mcpu=cortex-m4 -mthumb -mabi=aapcs -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wl,--gc-sections -lc -lm -lnosys --specs=nano.specs -Tble_app_hrs_gcc_nrf52.ld)

firmware_size(app)
generate_object(app .bin binary)

if ("${CMAKE_C_COMPILER_ID}" STREQUAL "GNU")
    generate_object(app .hex ihex)
endif()