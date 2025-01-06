import sharp from 'sharp';
import { mkdir, copyFile } from 'fs/promises';

async function generateLogoImages() {
  try {
    const inputSvg = 'src/logo.svg';
    const outputDir = 'app/static/assets/logo';
    
    // Ensure output directory exists
    await mkdir(outputDir, { recursive: true });

    // Copy the original SVG file
    await copyFile(inputSvg, `${outputDir}/logo.svg`);

    const sizes = [
      { width: 240, height: 240, name: 'logo-240x240.png' },
      { width: 120, height: 120, name: 'logo-120x120.png' },
      { width: 96, height: 96, name: 'logo-96x96.png' },
      { width: 48, height: 48, name: 'logo-48x48.png' },
      { width: 24, height: 24, name: 'logo-24x24.png' }
    ];

    console.log('Generating logo images...');

    await Promise.all(sizes.map(({ width, height, name }) =>
      sharp(inputSvg)
        .resize(width, height)
        .png()
        .toFile(`${outputDir}/${name}`)
    ));

    console.log('All logo files generated successfully!');
  } catch (error) {
    console.error('Error:', error);
  }
}

generateLogoImages();