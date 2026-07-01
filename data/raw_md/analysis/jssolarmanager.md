---
description: 태양광 패널 배치 및 분석을 위한 JSSolarManager API 문서입니다.
---

# JSSolarManager

> 태양광 패널 배치, 설정, 분석 등을 위한 주요 인터페이스를 제공하는 클래스입니다. 건물 또는 지형 기반의 설치를 모두 지원하며, 다양한 파라미터 설정 및 결과 조회가 가능합니다.

## Methods

### setActive(isActive) → void

> 태양광 모듈 편집을 활성화 또는 비활성화합니다.

{% tabs %}
{% tab title="Information" %}
- Parameters
  - `isActive` (`boolean`): true 시 태양광 배치 활성화
{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setActive(true);
```
{% endtab %}
{% endtabs %}

### setModuleAngle(useDefault, angle) → void

> 태양광 패널의 각도를 설정합니다.

{% tabs %}
{% tab title="Information" %}
- Parameters
  - `useDefault` (`boolean`): 기본값 사용 여부
  - `angle` (`number`): 기울기 각도 (degrees)
{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setModuleAngle(true, 30.0);
```
{% endtab %}
{% endtabs %}

### setModuleImage(imageData, width, height) → boolean

> 사용자 정의 이미지를 태양광 패널 텍스처로 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type        | Description                 |
|------------|-------------|-----------------------------|
| imageData  | array       | 이미지 픽셀 데이터 (RGBA).   |
| width      | number      | 이미지의 너비 (pixels).     |
| height     | number      | 이미지의 높이 (pixels).     |

- Return  
  - true: 설정 성공.  
  - false: 설정 실패.  
  - 실패 조건  
    - imageData가 null이거나 비어 있는 경우  
    - width 또는 height가 0 이하인 경우

{% endtab %}
{% tab title="Template" %}
```javascript
let image = new Uint8Array([
  255, 0, 0, 255,     // 빨강
  0, 255, 0, 255,     // 초록
  0, 0, 255, 255,     // 파랑
  255, 255, 255, 255  // 흰색
]);
let result = Module.getSolar().setModuleImage(image, 2, 2);
```
{% endtab %}
{% endtabs %}

### setProviderMode(isProvider) → void

> 태양광 Provider Mode를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| isProvider  | boolean | true: 공급자 모드, false: 소비자 모드 |

- Return  
  - 없음

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setProviderMode(true);
```
{% endtab %}
{% endtabs %}

### setModuleMargin(include, exclude, moduleSide, moduleTopDown, arraySide, arrayTopDown) → void

> 태양광 모듈 및 어레이 배치 간격을 설정합니다.  
> 음수 값은 자동으로 0으로 처리됩니다.

{% tabs %}
{% tab title="Information" %}

| Name           | Type    | Description                             |
|----------------|---------|-----------------------------------------|
| include        | number  | 전체 배치 경계 포함 여백 (meters)       |
| exclude        | number  | 전체 배치 경계 제외 여백 (meters)       |
| moduleSide     | number  | 모듈 간 좌우 간격 (meters)              |
| moduleTopDown  | number  | 모듈 간 상하 간격 (meters)              |
| arraySide      | number  | 어레이 간 좌우 간격 (meters)            |
| arrayTopDown   | number  | 어레이 간 상하 간격 (meters)            |

- Return  
  - 없음

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setModuleMargin(1.0, 0.5, 0.1, 0.1, 0.2, 0.2);
```
{% endtab %}
{% endtabs %}

### setDownScale(enable, length) → void

> 태양광 모듈 배치 시 일정 길이 간격으로 스케일 조정 기능을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                            |
|---------|---------|----------------------------------------|
| enable  | boolean | true 시 다운스케일 기능 활성화         |
| length  | number  | 스케일 조정 기준 길이 (양수, meters 단위) |

- Return  
  - 없음

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setDownScale(true, 3.0);
```
{% endtab %}
{% endtabs %}

### getModuleCount() → number

> 현재 활성화된 객체 내에 배치된 태양광 모듈의 총 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return  
  - `number`: 배치된 모듈 수  
  - `0`: 유효한 객체가 없거나 모듈이 배치되지 않은 경우

{% endtab %}
{% tab title="Template" %}
```javascript
let count = Module.getSolar().getModuleCount();
```
{% endtab %}
{% endtabs %}

### setSouthDeploy(enable) → void

> 남향 일괄 배치를 설정합니다. 해당 설정이 활성화되면 하나의 섹션으로 모든 모듈이 남향으로 배치됩니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `enable` (`boolean`): true 시 남향 일괄 배치 적용

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setSouthDeploy(true);
```
{% endtab %}
{% endtabs %}

### clearPreview() → void

> 모든 태양광 패널의 미리보기 상태를 초기화합니다.  
> `m_bPreview` 값이 false로 설정되어, 화면에서 미리보기 모듈이 제거됩니다.

{% tabs %}
{% tab title="Template" %}
```javascript
Module.getSolar().clearPreview();
```
{% endtab %}
{% endtabs %}

### selectRoofByObject(layerName, objectKey) → boolean

> 지정한 레이어와 객체 키를 기반으로 해당 지붕을 선택합니다.  
> 선택된 지붕 정보는 이후 태양광 패널 배치 등의 작업에 사용됩니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `layerName` (`string`): 대상 객체가 속한 레이어 이름
  - `objectKey` (`string`): 대상 객체의 고유 키

- Return
  - `true`: 지붕 선택 성공
  - `false`: 지붕 선택 실패

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().selectRoofByObject("building_layer", "object_001");
```
{% endtab %}
{% endtabs %}

### getAreaPointsOnTerrain() → JSVec3Array

> 지형에 설정된 태양광 설치 영역의 경계 좌표들을 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - `JSVec3Array`: 지형에 지정된 영역의 3D 좌표 배열

{% endtab %}
{% tab title="Template" %}
```javascript
let areaPoints = Module.getSolar().getAreaPointsOnTerrain();
```
{% endtab %}
{% endtabs %}

### getModuleSetWidthGapOnTerrain() → number

> 지형에 배치된 태양광 모듈 배열 간의 가로 간격(m)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - `number`: 모듈 배열 간 가로 간격 (meters)

{% endtab %}
{% tab title="Template" %}
```javascript
let widthGap = Module.getSolar().getModuleSetWidthGapOnTerrain();
```
{% endtab %}
{% endtabs %}

### getModuleSetHeightGapOnTerrain() → number

> 지형에 배치된 태양광 모듈 배열 간의 세로 간격(m)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - `number`: 모듈 배열 간 세로 간격 (meters)

{% endtab %}
{% tab title="Template" %}
```javascript
let heightGap = Module.getSolar().getModuleSetHeightGapOnTerrain();
```
{% endtab %}
{% endtabs %}

### setDirectionOfModuleOnTerrain(isSpecific, direction) → void

> 지형에 배치된 태양광 모듈의 방향 각도를 설정합니다.  
> `_isSpecific`이 true인 경우 입력한 각도(`direction`)를 적용하며, false인 경우 자동 방향을 사용합니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `isSpecific` (`boolean`): true 시 사용자가 지정한 각도를 적용
  - `direction` (`number`): 모듈 설치 방향 각도 (0~360도, degrees)

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setDirectionOfModuleOnTerrain(true, 180.0);
```
{% endtab %}
{% endtabs %}

### rebuildModuleOnTerrain() → void

> 지형에 배치된 태양광 모듈을 현재 설정값에 따라 다시 배치합니다.  
> 방향, 간격, 여백 등의 변경사항이 반영됩니다.

{% tabs %}
{% tab title="Template" %}
```javascript
Module.getSolar().rebuildModuleOnTerrain();
```
{% endtab %}
{% endtabs %}

### setModuleSetWidthGapOnTerrain(gap) → void

> 지형에 배치되는 태양광 모듈 세트 간의 가로 간격을 설정합니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `gap` (`number`): 세트 간 가로 간격 (meters). 0보다 작은 값은 자동으로 0으로 보정됩니다.

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setModuleSetWidthGapOnTerrain(1.5);
```
{% endtab %}
{% endtabs %}

### setModuleSetHeightGapOnTerrain(gap) → void

> 지형에 배치되는 태양광 모듈 세트 간의 세로 간격을 설정합니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `gap` (`number`): 세트 간 세로 간격 (meters). 0보다 작은 값은 자동으로 0으로 보정됩니다.

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().setModuleSetHeightGapOnTerrain(1.0);
```
{% endtab %}
{% endtabs %}

### getAlignAreaAngleOnTerrain() → number

> 지형에 설정된 배치 영역의 정렬 각도를 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - `number`: 정렬 각도 (degrees 단위). 0 ~ 360 사이의 값이 반환됩니다.

{% endtab %}
{% tab title="Template" %}
```javascript
let angle = Module.getSolar().getAlignAreaAngleOnTerrain();
```
{% endtab %}
{% endtabs %}

### getCenterOfMassOnTerrain() → [CJSVector3D](../core/jsvector3d.md)

> 지형 위에 배치된 태양광 패널의 질량 중심 위치를 반환합니다.
>
> 반환되는 값은 경도, 위도, 고도 순서의 좌표입니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - [`CJSVector3D`](../core/jsvector3d.md): 질량 중심 위치 (longitude, latitude, altitude)

{% endtab %}
{% tab title="Template" %}
```javascript
let center = Module.getSolar().getCenterOfMassOnTerrain();
console.log(center.lon, center.lat, center.alt);
```
{% endtab %}
{% endtabs %}

### getTerrainModuleCount() → number

> 지형에 설치된 태양광 모듈의 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - `number`: 설치된 모듈 수

{% endtab %}
{% tab title="Template" %}
```javascript
let count = Module.getSolar().getTerrainModuleCount();
console.log("Terrain Module Count:", count);
```
{% endtab %}
{% endtabs %}

### clearModuleOnTerrain() → void

> 지형에 설치된 모든 태양광 모듈을 제거합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - 없음

{% endtab %}
{% tab title="Template" %}
```javascript
Module.getSolar().clearModuleOnTerrain();
```
{% endtab %}
{% endtabs %}

### getLayerPannelInfo(layerName) → string

> 지정한 레이어 내 태양광 패널 객체들의 정보를 JSON 문자열 형태로 반환합니다.  
> 패널 위치(위도/경도/고도), 크기, 방향, 각도 등의 상세 정보가 포함됩니다.

{% tabs %}
{% tab title="Information" %}

- Parameters
  - `layerName` (`string`): 대상 레이어 이름

- Return
  - `string`: JSON 문자열
    ```json
    [
      {
        "Pos": [경도, 위도, 고도],
        "MWidth": 패널가로길이,
        "MHeight": 패널세로길이,
        "Thickness": 패널두께,
        "MAngle": 수직각,
        "MDirection": 방향각
      },
      ...
    ]
    ```

{% endtab %}
{% tab title="Template" %}
```javascript
let jsonInfo = Module.getSolar().getLayerPannelInfo("BuildingLayer");
let data = JSON.parse(jsonInfo);
console.log(data);
```
{% endtab %}
{% endtabs %}

### SetModuleArray(nSection, nSectionCount, nSectionSet) → boolean

> 태양광 모듈의 배열 구성 정보를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name           | Type  | Description |
|----------------|-------|-------------|
| nSection       | int   | 단일 배열당 섹션 수 |
| nSectionCount  | int   | 배열 전체의 섹션 개수 |
| nSectionSet    | int   | 배열 세트 수 |

- Return  
  - `true`: 설정 성공 및 모듈 재배치 완료  
  - `false`: 설정 실패 (엔진 미초기화 또는 내부 오류)

- Description  
  - 태양광 시스템 내 모듈 배열 구성을 설정합니다.  

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    JSSolarManager : Module.getSolarManager()
};

// 예: 각 배열당 5개 섹션, 섹션 총 20개, 세트 2개 구성
var result = API.JSSolarManager.SetModuleArray(5, 20, 2);

if (!result) {
    console.error("모듈 배열 설정 실패");
}
```
{% endtab %}
{% endtabs %}
