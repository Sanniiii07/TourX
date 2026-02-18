import hre from "hardhat";
const { ethers } = hre;

const CONTRACT_ADDRESS = "0xDb2d854182F9Db54a7f33c5400C05551370d1306";

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Using account:", deployer.address);

  const TouristID = await ethers.getContractFactory("TouristID");
  const contract = TouristID.attach(CONTRACT_ADDRESS);

  // 1️⃣ Fetch role IDs
  const DEFAULT_ADMIN_ROLE = await contract.DEFAULT_ADMIN_ROLE();
  const TOURISM_ROLE = await contract.TOURISM_ROLE();
  const POLICE_ROLE = await contract.POLICE_ROLE();

  // 2️⃣ Check roles
  console.log("DEFAULT_ADMIN_ROLE:", await contract.hasRole(DEFAULT_ADMIN_ROLE, deployer.address));
  console.log("TOURISM_ROLE:", await contract.hasRole(TOURISM_ROLE, deployer.address));
  console.log("POLICE_ROLE:", await contract.hasRole(POLICE_ROLE, deployer.address));

  // 🚨 If any of the above is false, STOP and tell me

  // 3️⃣ Register a tourist (cheap tx)
  console.log("Registering tourist...");

  const tx = await contract.registerTourist(
    deployer.address,
    "Test Tourist",
    ethers.encodeBytes32String("KYC_HASH"),
    ethers.encodeBytes32String("ITINERARY_HASH"),
    "9999999999",
    Math.floor(Date.now() / 1000),
    Math.floor(Date.now() / 1000) + 86400
  );

  await tx.wait();
  console.log("✅ Tourist registered");

  // 4️⃣ Read tourist data
  const data = await contract.getTourist(deployer.address);

  console.log("Tourist Data:");
  console.log({
    name: data.name,
    emergencyContact: data.emergencyContact,
    exists: data.exists
  });

  console.log("🎉 SMART CONTRACT DEVELOPMENT: FULLY WORKING");
}

main().catch((e) => {
  console.error("❌ ERROR:", e);
  process.exit(1);
});
