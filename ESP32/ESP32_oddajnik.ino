#include "sys/time.h"
#include "BLEDevice.h"
#include "BLEUtils.h"
#include "BLEServer.h"
#include "BLEBeacon.h"
#include "esp_sleep.h"

#define GPIO_DEEP_SLEEP_DURATION 2
RTC_DATA_ATTR static time_t last;
RTC_DATA_ATTR static uint32_t bootcount;

BLEAdvertising *pAdvertising;
struct timeval now;

#define BEACON_UUID "425bdf2a-32bf-474f-b82e-939f1b063e0d"

void setBeacon() {

  BLEBeacon oBeacon = BLEBeacon();
  oBeacon.setManufacturerId(0x4C00);
  oBeacon.setProximityUUID(BLEUUID(BEACON_UUID));
  oBeacon.setMajor((bootcount & 0xFFFF0000) >> 16);
  oBeacon.setMinor(bootcount & 0xFFFF);
  BLEAdvertisementData oAdvertisementData = BLEAdvertisementData();
  BLEAdvertisementData oScanResponseData = BLEAdvertisementData();

  oAdvertisementData.setFlags(0x04);

  std::string strServiceData = "";

  strServiceData += (char)26;
  strServiceData += (char)0xFF;
  strServiceData += oBeacon.getData();
  oAdvertisementData.addData(strServiceData);

  pAdvertising->setAdvertisementData(oAdvertisementData);
  pAdvertising->setScanResponseData(oScanResponseData);
}

void setup() {

  gettimeofday(&now, NULL);
  last = now.tv_sec;

  BLEDevice::init("Avto");
  BLEServer *pServer = BLEDevice::createServer();
  pAdvertising = BLEDevice::getAdvertising();
  BLEDevice::startAdvertising();
  setBeacon();
  pAdvertising->start();
  delay(100);
  pAdvertising->stop();
  esp_deep_sleep(1000000LL * GPIO_DEEP_SLEEP_DURATION);
}

void loop() {
}
